#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import docker
import requests

client = docker.from_env()
time.sleep(10)  # we expect all containers are up and running in 10 secs

for c in client.containers.list():
    print("{}: {}".format(c.name, c.status))
    if 'running' not in c.status:
        print(c.logs())

# NGINX
nginx = client.containers.get('nginx')
nginx_cfg = nginx.exec_run("/usr/sbin/nginx -T")
assert nginx.status == 'running'
assert 'the configuration file /etc/nginx/nginx.conf syntax is ok' in nginx_cfg.output.decode()
assert 'HTTP/1.1" 500' not in nginx.logs()

# test restart
nginx.restart()
time.sleep(3)
assert nginx.status == 'running'

web = client.containers.get('web')
assert 'uWSGI http bound on :8000' in web.logs()
assert 'spawned uWSGI worker 1' in web.logs()
assert web.status == 'running'

db = client.containers.get('db')
assert db.status == 'running'
cnf = db.exec_run('psql -U django -h 127.0.0.1 -p 5432 -c "select 1"')
log = db.logs()
assert "database system is ready to accept connections" in log.decode()

response = requests.get("http://localhost/users/?format=json")
assert response.status_code == 200
assert '{"count":0,"next":null,"previous":null,"results":[]}' in response.text
