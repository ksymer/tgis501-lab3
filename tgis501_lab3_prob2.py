#============================================
# Project: T GIS 501 a: Lab 3, Problem 2
# Purpose: Counting words in a text document
# Author:  Kris Symer
# Date:    2014-10-11
#============================================

#input variables
file_name = 'data/GIS_is_the_best.txt' #may include relative path
mode = 'r' #read only access
words = ['systems', 'science']

#open and read file; convert text to lowercase
myfile = open(file_name, mode)
print 'File Name = ' + myfile.name
read_file = myfile.read().lower()

#split text into list, then get list length
mylist = read_file.split()
print 'Total Words = ' + str(len(mylist)) #count list items

#count occurrences of specific items (words) in list
print 'Case insensitive search:'
for word in words:
	print '\tThe word "' + word + '" appears ' + str(mylist.count(word)) + " times."

#close file when finished
myfile.close()