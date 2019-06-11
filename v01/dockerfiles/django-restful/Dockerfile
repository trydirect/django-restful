FROM python:3.7
LABEL maintainer="info@optimum-web.com"

ENV TZ=America/Los_Angeles
RUN  groupadd -r -g 2000 django; useradd -r -u 2000 -g 2000 -m -c "app account" -d /home/django -s /bin/bash django
RUN apt-get update -y && DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y \
curl locales gcc libpq5 git curl lsof libpq-dev libffi-dev supervisor unzip make procps libc6-dev \
uwsgi uwsgi-src uuid-dev libcap-dev && apt-get clean && rm -rf /var/lib/apt/lists/*;

RUN sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen && \
    locale-gen
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY supervisord.conf /etc/supervisord.conf

RUN django-admin startproject django_restful
WORKDIR /app/django_restful
RUN django-admin startapp quickstart
COPY configs/serializers.py /app/django_restful/quickstart/serializers.py
COPY configs/views.py /app/django_restful/quickstart/views.py
COPY configs/settings.py /app/django_restful/django_restful/settings.py
