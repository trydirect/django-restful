[![Build Status](https://travis-ci.com/trydirect/django-restful.svg?branch=master)](https://travis-ci.com/trydirect/django-restful)
[![Python 3.7](https://img.shields.io/badge/python-3.7-blue.svg)](https://www.python.org/downloads/release/python-370/)
![Docker Stars](https://img.shields.io/docker/stars/trydirect/django-restful.svg)
![Docker Pulls](https://img.shields.io/docker/pulls/trydirect/django-restful.svg)
![Docker Automated](https://img.shields.io/docker/cloud/automated/trydirect/django-restful.svg)
![Docker Build](https://img.shields.io/docker/cloud/build/trydirect/django-restful.svg)
[![Gitter chat](https://badges.gitter.im/trydirect/community.png)](https://gitter.im/try-direct/community)
	
# Django Restful API template

Django Restful API backend template - project generator/development environment.
Can be used by Python developers for quick start on building Restful API's using Django framework and django-rest-framework.
This project is aimed to simmplify development environment setup and includes many useful dev tools like RabbitMQ, Redis, Elasticsearch, Kibana, Apidoc 


## Stack includes

* RabbitMQ 
* Redis 
* Elasticsearch
* Logstash
* PostgreSQL
* Nginx
* Supervisord
* Kibana
* Apidoc

Python libraries included:
* django-rest-framework 
* uwsgi
* psycopg2 


## Installation
1. Clone this project into your work directory:
```sh
$ git clone "https://github.com/trydirect/django-restful.git"
```

2. Bring up services with docker-compose:
```sh
$ cd django-restful/v01/dockerfiles
$ docker-compose up -d
$ docker-compose exec web python manage.py migrate
```

3. Now, let's check it out
```
$ curl -i curl -i localhost/users/
HTTP/1.1 200 OK
Server: nginx/1.16.0
Date: Thu, 13 Jun 2019 10:39:46 GMT
Content-Type: application/json
Content-Length: 52
Connection: keep-alive
Vary: Accept, Cookie
Allow: GET, POST, HEAD, OPTIONS
X-Frame-Options: SAMEORIGIN

{"count":0,"next":null,"previous":null,"results":[]}
```

```
$ docker-compose ps

Name                  Command                          State          Ports
------------------------------------------------------------------------------------------------------------------------------
db                    docker-entrypoint.sh postgres    Up (healthy)   5432/tcp
elasticsearch         /docker-entrypoint.sh elas ...   Up             9200/tcp, 9300/tcp
kibana                /docker-entrypoint.sh kibana     Up             0.0.0.0:5601->5601/tcp
logstash              /docker-entrypoint.sh -e         Up             0.0.0.0:5044->5044/tcp
mq                    docker-entrypoint.sh rabbi ...   Up (healthy)   15671/tcp, 0.0.0.0:21072->15672/tcp, 25672/tcp, 4369/tcp, 5671/tcp, 0.0.0.0:2172->5672/tcp,0.0.0.0:32770->5672/tcp
nginx                 /usr/bin/supervisord -c /e ...   Up             0.0.0.0:443->443/tcp, 0.0.0.0:80->80/tcp
redis                 docker-entrypoint.sh redis ...   Up (healthy)   6379/tcp
web                   /usr/bin/supervisord -c /e ...   Up             0.0.0.0:8000->8000/tcp   
```

## Generate Api Doc
```.env
$ sh ./djangorest/scripts/apidoc.sh
```


## Contributing

1. Fork it (https://github.com/trydirect/django-restful/fork)
2. Create your feature branch (git checkout -b feature/fooBar)
3. Commit your changes (git commit -am 'Add some fooBar')
4. Push to the branch (git push origin feature/fooBar)
5. Create a new Pull Request


## Support Development

[![Donate](https://img.shields.io/badge/Donate-PayPal-green.svg)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=2BH8ED2AUU2RL)
