#!/usr/bin/python
#
# Create a SQL file to load budget data
#

import os
import sys

def load_csv_data(base):
    loaded = []
    files = os.listdir(base)

    for filename in files:
        if filename.endswith(".csv"):
            parts = filename.split('.')[0].split('_')
            ulcs = parts[1]
            snapshot = parts[2]

            loaded.append({
                'ulcs': ulcs,
                'snapshot': snapshot,
                'lines': file("%s/%s" % (base, filename)).read().split('\n')
            })

    return loaded

def create_sql_string(table, ulcs, snapshot, lines):
    if lines is None or len(lines) is 0 or (len(lines) == 1 and lines[0] == ' '):
        return "-- ULCS %s SNAPSHOT %s has no data --" % (ulcs, snapshot)

    templ = "INSERT INTO %s (ulcs, snapshot, item, amount)"\
            "VALUES ('%s', '%s', '%s', '%s');"

    strs = []
    for line in lines[0:-1]:
        cat,amt = line.split(',')
        strs.append(templ % (table, ulcs, snapshot, cat, amt))

    return '\n'.join(strs)

def create_table_string(table):
    return """
CREATE TABLE %s (
     id       SERIAL,
     ulcs     varchar(40) NOT NULL,
     snapshot varchar(10) NOT NULL,
     item     varchar(250) NOT NULL,
     amount   integer
);
""" % table

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print """
Usage: create_sql.py <input directory> <output file>

Parse CSV files into a sql 'create table' statement
and a bunch of sql 'insert' statements.
"""
        exit(1)

    data_dir = sys.argv[1]
    output_file = sys.argv[2]
    data = load_csv_data(data_dir)

    writer = file(output_file,'w')
    writer.write(create_table_string('budget_items'))

    for opts in data:
        sql = create_sql_string('budget_items', **opts)
        writer.write(sql)
        writer.write('\n\n')

    writer.close()
