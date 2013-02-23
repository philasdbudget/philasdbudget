#!/usr/bin/perl -w
#
use strict;
use Getopt::Std;

sub usage();

my %opts;
getopts('i:', \%opts);

$opts{i} || usage();

open (IN, $opts{i}) || die "can't open $opts{i}";

my $final_total;
my $in_body;
my $running_total;
my $running_subtotal;

while (<IN>) {
    chomp;

    next if (/^\s*$/);

    if (/FTE\s+Amount\s+FTE/) {
	$in_body = 1;
	next;
    }

    if (/School District of Philadelphia/) {
	$in_body = 0;
	  next;
    }

    if ($in_body) {
	/^([a-zA-Z\s\-\/]+)/;
	my $desc = $1;

	$desc =~ s/\s+$//;
	
	/([\-0-9\,\.]+)\s*$/;
	my $line_total = $1;
	
	my $work_total = $line_total;
	$work_total =~ s/[\,\.]+//g;

	if ($desc eq "Total") {
	    $final_total = $line_total;
	    $in_body = 0;
	    next;
	} elsif (/Sub Total/) {
	    if ($work_total != $running_subtotal) {
		#print "--sub total mismatch: $desc $work_total $running_subtotal\n";
		$running_total += $work_total;
		$running_subtotal += $work_total;
		print "$desc $line_total\n";
	    } else {
		$running_subtotal = 0;
	    }
	    next;
	} else {
	    $running_total += $work_total;
	    $running_subtotal += $work_total;
	}
	
	print "$desc,$line_total\n";
    }
}

exit if (!defined $final_total);

$final_total =~ s/[\,\.]+//g;
if ($running_total != $final_total) {
    print "--totals mis-match! calculated: $running_total, total: $final_total, difference: ", $final_total - $running_total, "\n";
#    exit 1;
}
#print "final total: $final_total\n";


sub usage() {
    print "\n";
    print "usage: $0 -i <input file>\n";
    exit 0;
}
