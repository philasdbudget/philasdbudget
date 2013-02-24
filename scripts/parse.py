#!/usr/bin/python
import os
import sys
import re

def parse_file(afile):
    data = file(afile).read().split('\n')
    lines = []

    found_header = False
    base_re = '([&a-zA-Z/\\ -]+).*?([0-9][0-9,.]*)$'

    # Some lines start with a page break
    # so we strip those characters in the match
    for line in data:
        if re.search('School District of Philadelphia', line):
            found_header = False
        # Generally found_header is set to None after a page
        # and set back to True when the magic header (FTS
        # amount is found. However, certain totals don't
        # have any mor headers. That's what the second part
        # of the ~OR~ statement does
        elif found_header or re.match('Total.*?[0-9,.]+$', line.strip()):
            match = re.match(base_re, line.strip())
            if match:
                cat = match.group(1).strip()
                total = int(match.group(2).replace(',',''))

                if line.endswith("-%s" % match.group(2)):
                    cat = cat[0:-1].strip()
                    total *= -1

                if total != 0:
                    lines.append((cat, total))
        else:
            found_header = re.search('FTE\s+Amount', line) != None

    return lines

def verify(lines):
    total = 0
    subtotal = 0

    cats = []

    for line in lines:
        cat, amt = line
        #print "-- %s | %s | %s | %s" % (cat, amt, subtotal, total)
        if re.search('sub total', cat.lower()):
            #print "%s == %s?" % (subtotal, amt)
            if subtotal == amt: # Reject subtotal line
                #print "Reject %s" % cat
                subtotal = 0
            else: # Include this line
                #print "Accept %s" % cat
                total += amt
                subtotal = 0

                cats.append(line)
        else:
            cats.append(line)
            total += amt
            subtotal += amt

    if len(cats) > 0:
        final_total = cats[-1][1]

        if final_total != total/2:
            print "Verify error: %s != %s" % (final_total, total/2)
            return None

    return cats

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print """
Usage:
parse.py path/to/file.txt

Attempts to parse the output of a pdftotext result from a
philadelphia school district budget form. The output from
this program is either:
  path/to/file.txt.csv  or
  path/to/file.txt.err

The csv file contains budget lines. Subtotal lines are
ignored *unless* there are no budget items for a given
subtotal.

The last line in the file is the total as parsed from the
pdf and it should be equal to the sum of all of the other
lines in the file.
"""
        exit(1)

    filetoparse = sys.argv[1]
    output = "%s.csv" % filetoparse
    err = "%s.err" % filetoparse

    if os.path.exists(output):
        exit(0)

    lines = parse_file(filetoparse)
    lines = verify(lines)

    if lines is None:
        errf = file(err,'w')
        errf.write(' ')
        errf.close()
        exit(0) # Error

    if len(lines) == 0:
        outputf = file(output,'w')
        outputf.write(' ')
        outputf.close()
    elif lines:
        outputf = file(output,'w')
        for line in lines:
            outputf.write("%s,%s\n" % line)

        outputf.close()
