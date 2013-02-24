DB_USER='phillysd'
DB_PASS='phillysd'
DB_DATABASE='phillysd'

apt-get install -y postgresql-9.1 postgresql-9.1-postgis postgis postgresql postgresql-server-dev-9.1

sudo -u postgres psql -c '\du' | grep "^ $DB_USER"
if [ $? -eq 1 ] ; then
    sudo -u postgres psql -c "CREATE USER $DB_USER ENCRYPTED PASSWORD '$DB_PASS'"
fi

sudo -u postgres psql -c '\list' | grep "^ $DB_DATABASE"
if [ $? -eq 1 ] ; then
    sudo -u postgres psql -c "CREATE DATABASE $DB_DATABASE OWNER $DB_USER"
fi
