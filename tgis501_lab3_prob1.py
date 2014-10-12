#============================================
# Project: T GIS 501 a: Lab 3, Problem 1
# Purpose: Renaming files in a directory
# Author:  Kris Symer
# Date:    2014-10-11
#============================================

#input variables
path = 'text_files' #relative to this script location
extension = '.txt'

#import library
import os

#navigate to folder
os.chdir(path)
print 'Renaming files in folder: ' + os.getcwd()

#create list of files in folder
file_list = os.listdir(os.getcwd())

#loop through files
for item in file_list:
	this_file = item.split('.') #split into filename and extension
	new_filename = this_file[0].lower() #convert filename to lowercase
	new_filename = new_filename + extension #append new extension
	print item + ' renamed to ' + new_filename
	os.rename(item, new_filename) #rename file

#confirm task complete
print 'All files renamed in: ' + os.getcwd()