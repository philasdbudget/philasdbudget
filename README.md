## Philadelphia School Budget

### Overview
This project is a set of tools to download and parse
Philadelphia School District budget pdfs.

The original pdfs can be found here:
https://apps.philasd.org/SchoolBudgets/

### API
```
/api/schools
```

```json
[{
  "school_name2": "GIRARD ACADEMIC MUSIC PROGRAM",
  "school_name": "GIRARD ACADEMIC MUSIC PROGRAM",
  "geom": [
    "-75.18256",
    "39.92219"
    ],
    "link": "http://localhost:9449/api/budget/2410",
    "address": "2136 W. RITNER ST.",
    "ulcs": "2410"
},
...]
```

```
/api/budget/{schoolid}
/api/budget/2410
```
```json
{
  "61": {
    "link": "http://localhost:9449/api/budget/2410/61",
    "description": "FY09 School Budgets (February 2009)"
  },
  ...
}
```

```
/api/budget/{schoolid}/{snapshot}
/api/budget/2410/101
```

```json
{
  "school": {
    "ulcs": "2410",
    "link": "http://localhost:9449/api/budget/2410"
    },
  "snapshot": "101",
  "items": [
  {
    "item": "Books & Instructional Aids",
    "amount": 48350,
    "link": "http://localhost:9449/api/budgetitem/5",
    "id": 5
  },
  ...]
}
```

```
/api/schxools/totals/<snapshot>
/api/dates
/api/budgetitem/
/api/budgetitem/<itemid>
```

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

If you don't want to use vagrant, the script in 'scripts/bootstrap.sh'
should be more-or-less safe to run on your own machine.

#### Vagrant & Database

```bash

vagrant up
vagrant ssh

# Running on the vagrant box...

# You can use the pre-saved budget data if you don't want
# to deal with the above steps
cd /vagrant/school_data
gunzip budget_data.sql.gz

# Load the budget data
# Password: phillysd
psql phillysd phillysd -h localhost -f /vagrant/school_data/budget_data.sql
psql phillysd phillysd -h localhost -f /vagrant/scripts/normalize.sql

# Load extra school data
# You have to be in /vagrant/school_data for the data to load properly
cd /vagrant/school_data
psql phillysd phillysd -h localhost -f philasd.sql

exit
```

#### Python

Create a virtualenv

```bash
# If you're using vagrant 'vagrant ssh' first:
vagrant ssh

# If you don't have pip or virtualenv installed
sudo easy_install pip
sudo pip install virtualenv

# Create a new virtualenv wherever you want
mkdir ~/envs/
virtualenv ~/envs/phillysd

# Activate it
source ~/envs/phillysd/bin/activate

# Install requirements
cd /vagrant
pip install -r requirements.txt

# Copy settings file
cp wsgi/settings.py.default wsgi/settings.py

# If you did the normal vagrant install then the default
# settings are fine, otherwise you should fix them up:
vim wsgi/settings.py