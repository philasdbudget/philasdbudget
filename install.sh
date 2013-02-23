#!/bin/bash

# This script should install all dependencies for the project


# must be run as root
if [ `whoami` != "root" ]; then
  echo "This installation must be run as root."
  exit 1
fi

LOG=$PWD/_install.log
echo -n "" > $LOG

# install requirements via apt-get
echo -e "\nInstalling required packages with 'apt'"
apt-get install -q -y postgresql-9.1-postgis gdal-bin libgdal1 libgeos-c1 python-psycopg2 &>> $LOG

service postgresql start &>> $LOG

easy_install pip &>> $LOG
pip install -r requirements.txt &>> $LOG

# configure postgis
echo -e "\n##\n## Messages from setting up postgis:\n##" &>> $LOG
su postgres -c "psql -f install.sql" &>> $LOG


