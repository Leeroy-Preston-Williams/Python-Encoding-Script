#!/usr/bin/python

import sys
from sys import argv
from os.path import exists

script, filename = argv

print "Hello dear user please may you fill in the following details for a questioneer."
print "Opening file for adding text..."
file = open(filename, 'w')
print "To proceed press ENTER or Ctr^C to quit."

line1 = raw_input("Name: ")
line1 = line1.encode('base64','strict');
print "Do you want to see the encoded text?"
choice = raw_input("> ")
if (choice != 'yes'):
	print "goodbye"
	sys.exit()
else:
	print "Good"

print "Encoded String: " + line1;
print "Thank for inputing a valid name"

print "I'm now going to store the information you've given me in a document."
file.write(line1)
file.write("\n")
print "Goodbye"
file.close()