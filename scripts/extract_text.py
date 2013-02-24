#!/usr/bin/python
import sys
import os

if len(sys.argv) != 2:
    print """
Usage: extract_text.py <data_dir>
"""
    exit(1)

base = sys.argv[1]
file_list = os.listdir(base)

for f in file_list:
    f_name = f.split(".")[0:-1]
    os.system('pdftotext -layout %s/%s.pdf %s/%s.txt' %
              (base, f_name, base, f_name))
