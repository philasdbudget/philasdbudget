import sys
import os

file_list = os.listdir('./data/')

print file_list[0].split(".")[0]
for f in file_list:
	f_name = f.split(".")[0]
	os.system('pdftotext -layout %s.pdf')