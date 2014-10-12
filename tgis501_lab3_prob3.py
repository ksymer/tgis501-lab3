#============================================
# Project: T GIS 501 a: Lab 3, Problem 3
# Purpose: Replacing words in a text document
# Author:  Kris Symer
# Date:    2014-10-11
#============================================

#input variables
file_name = 'data/GIS_is_the_best.txt' #may include relative path
file_name_new = 'data/GIS_is_the_best.replaced.txt'
#enter any number of string replacement pairs
pairs = [['Science', 'Systems'], ['science', 'systems']]

#open and read existing file
old_file = open(file_name, 'r') #read only access
temp_content = old_file.read()
old_file.close()
print '1. Reading from existing file: ' + old_file.name

print '2. Replacing string pairs:'
#loop through pairs list, replacing strings 
for pair in pairs:
 	temp_content = temp_content.replace(pair[0],pair[1])
	print '\tReplaced "' + pair[0] + '" with "' + pair[1] + '"'

#save replaced content to new file
new_file = open(file_name_new, 'w+')
new_file.write(temp_content)
new_file.close()

print '3. Saving changes to: ' + new_file.name