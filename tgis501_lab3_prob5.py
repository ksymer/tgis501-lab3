#============================================
# Project: T GIS 501 a: Lab 3, Problem 5
# Purpose: Counting unique words and word frequency
# Author:  Kris Symer
# Date:    2014-10-12
#============================================

#import string
from collections import Counter
# coding=utf-8

#input variables
file_name = 'data/pg31469_clean.txt' #may include relative path
mode = 'r' #read only access
words = ['uncle', 'athen\xc3\xa6um'] #added utf encoded word athenaeum after running
replace_strings = ['.', '&', '_', ',', ':', ';', '"', '!', '*', '--', '\xef\xbb\xbf'] #\xef\xbb\xbf = UTF BOM

#open and read file               ; convert text to lowercase
myfile = open(file_name, mode)
print 'Reading file: ' + myfile.name
read_file = myfile.read()

#replace certain punctuation characters with space
#retain hyphenated words and contractions (omit hyphen and apostrophe)
clean_file = read_file
for chars in replace_strings:
	clean_file = clean_file.replace(chars, ' ')

#convert to lowercase and split text into list
mylist = clean_file.lower().split()
wcount = Counter(mylist)
print wcount
print 'This document contains ' + str(len(wcount)) + ' uniqe words.' #count list items


#count occurrences of specific items (words) in list
print 'Case insensitive search:'
for word in words:
	print '\tThe word "' + word + '" appears ' + str(mylist.count(word)) + " times."


#close file when finished
myfile.close()