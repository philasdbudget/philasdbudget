#!/bin/bash

# must be run as root
if [ `whoami` != "root" ]; then
  echo "This installation must be run as root."
  exit 1
fi

set -x

DB_USER='phillysd'
DB_PASS='phillysd'
DB_DATABASE='phillysd'

sudo update-locale LANG=en_US.utf8

echo "locale update line passed"

apt-get install -y postgresql-9.1 postgresql-9.1-postgis postgis postgresql postgresql-server-dev-9.1 nginx
apt-get install -y python-setuptools build-essential python-dev

sudo -u postgres psql -c '\du' | grep "^ $DB_USER"
if [ $? -eq 1 ] ; then
    sudo -u postgres psql -c "CREATE USER $DB_USER ENCRYPTED PASSWORD '$DB_PASS'"
fi

sudo -u postgres psql -c '\list' | grep "^ template_postgis"
if [ $? -eq 1 ]; then
    sudo -u postgres psql <<EOF
create database template_postgis with encoding='UTF8';

\c template_postgis;
\i /usr/share/postgresql/9.1/contrib/postgis-1.5/postgis.sql;
\i /usr/share/postgresql/9.1/contrib/postgis-1.5/spatial_ref_sys.sql

EOF

fi

sudo -u postgres psql -c '\list' | grep "^ $DB_DATABASE"
if [ $? -eq 1 ] ; then
    sudo -u postgres psql -c "CREATE DATABASE $DB_DATABASE OWNER $DB_USER TEMPLATE template_postgis"
    sudo -u postgres psql $DB_DATABASE -c "alter table spatial_ref_sys owner to $DB_USER";
    sudo -u postgres psql $DB_DATABASE -c "alter table geometry_columns owner to $DB_USER";
    sudo -u postgres psql $DB_DATABASE -c "alter view geography_columns owner to $DB_USER";

fi

NGINX_DEF="/etc/nginx/sites-available/phillysd"
NGINX_AVAIL="/etc/nginx/sites-enabled/000_phillysd"

if [ ! -e $NGINX_DEF ];
then
    cat > $NGINX_DEF <<EOF
server {
    listen       80;
    server_name  _;

    root /vagrant/static;

    location / { try_files $uri @flaskapp; }
    location @flaskapp {
      proxy_pass http://127.0.0.1:5000;
    }
}
EOF

fi

if [ ! -e $NGINX_AVAIL ];
then
    ln -s $NGINX_DEF $NGINX_AVAIL
    sudo service nginx restart
fi

UPSTART_FILE="/etc/init/phillysd.conf"
if [ ! -e $UPSTART_FILE ];
then
    cat <<EOF > $UPSTART_FILE
description "unicorn"

start on runlevel [2345]
stop on runlevel [06]

chdir /vagrant/wsgi
exec /home/vagrant/envs/phillysd/bin/gunicorn app:app -b 0.0.0.0:5000

EOF
    service phillysd start
fi
