## Philadelphia School Budget

### Overview
This project is a set of tools to download and parse
Philadelphia School District budget pdfs.

The original pdfs can be found here:
https://apps.philasd.org/SchoolBudgets/servlet

### API
Using the API....

### Getting the raw data

There are a series of scripts to run to download and
parse all of the data. The whole process should look
something like:

```bash
# Pull down all of the pdfs
scripts/scrape.py data_dir

# Convert the files to pdf
scripts/extract_text.py data_dir

# Parse the resulting text files
find data_dir -iname \*.txt -exec scripts/parse.py {} \;

# Compile them into a SQL file
scripts/create_sql.py data_dir budget_data.sql
```

### Running the Server

There is a Vagrantfile included that can be used to start
up a new database server to work with the database

```bash

vagrant up
vagrant ssh

# Running on the vagrant box...

# Load the budget data
# Password: phillysd
psql phillysd phillysd -h localhost -f /vagrant/budget_data.sql
psql phillysd phillysd -h localhost -f /vagrant/normalize.sql

# Load extra school data
# You have to be in /vagrant/school_data for the data to load properly
cd /vagrant/school_data
psql phillysd phillysd -h localhost -f

exit
```