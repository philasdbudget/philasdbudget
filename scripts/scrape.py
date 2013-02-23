#!/usr/bin/python

import os
import sys
import urllib2
from multiprocessing import Pool

from schools import SCHOOLS

SNAPSHOTS = {"181": "FY13 School Budgets",
             "161": "FY12 School Budgets",
             "141": "FY11 School Budgets",
             "121": "FY10 School Budgets",
             "101": "FY10 School Budgets",
             "61": "Y09 School Budgets"}

def read_pdf_to_file(ulcs, snapshot, output_dir):
    url_template = "https://apps.philasd.org/SchoolBudgets/servlet?handler=us.pa.k12.phila.SchoolBudgets.handler.BuildNoAuthReportHandler&PARAM_ULCS=%s&PARAM_SNAPSHOT_ID=%s&PARAM_REPORT_NAME=public_budget_report"

    output = "%s/budgetpurchase_%s_%s.pdf" % (output_dir, ulcs, snapshot)

    if os.path.exists(output):
        return

    print "Writing to %s" % output

    url = url_template % (ulcs, snapshot)

    try:
        response = urllib2.urlopen(url)
        pdf = response.read()

        f = file(output,'w')
        f.write(pdf)
        f.flush()
        f.close()
    except Exception, e:
        print "Error %s %s" % (ulcs, snapshot)

def usage_and_die():
    print 'Usage: scrape.py output_dir [ulcs] [snapshot]'
    exit(1)

def read_pdf_to_file_wrapper(args):
    read_pdf_to_file(args[0], args[1], args[2])

if __name__ == '__main__':
    if len(sys.argv) < 2:
        usage_and_die()

    output_dir = sys.argv[1]
    ulcses = SCHOOLS
    snapshots = SNAPSHOTS.keys()
    if len(sys.argv) >= 3:
        ulcses = sys.argv[2]
    if len(sys.argv) >= 4:
        snapshots = [sys.argv[3]]
    if len(sys.argv) > 4:
        usage_and_die()

    jobs = []
    for ulcs in ulcses:
        for snapshot in snapshots:
            jobs.append([ulcs, snapshot, output_dir])

    print "About to process %s records" % len(jobs)

    p = Pool(10)
    p.map(read_pdf_to_file_wrapper, jobs)
