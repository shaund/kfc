#! /usr/bin/python

from __future__ import with_statement

import re
import os
import sys
# import subprocess
from subprocess import Popen, PIPE

clist = []
CHAPTER = '<mbp:section>\n##'

def to_html(text):
	markdown = sys.path[0]+'/Markdown.pl'
	smartypants = sys.path[0]+'/SmartyPants.pl'
	# print markdown
	tfile = sys.path[0]+'/text.txt'
	htmlfile = sys.path[0]+'/text.htm'
	output = ''
	with open(tfile, 'wb') as f: f.writelines(text)
		
	# os.system('"cmd /c perl "' + markdown + '" "' + tfile + '" > text.htm')
	
	cmd = 'cmd /c perl '+ markdown +' '+ tfile
	p = Popen([cmd], shell=True, stdin=PIPE, stdout=PIPE)
	output = p.stdout.read()
	with open(htmlfile, 'rb+') as f: f.writelines(output)	
	
	cmd = 'cmd /c perl '+ smartypants +' '+ htmlfile
	p = Popen([cmd], shell=True, stdin=PIPE, stdout=PIPE)
	output = p.stdout.read()
	with open(htmlfile, 'rb+') as f: f.writelines(output)	
	
	
	return 'OKAY!'
	
	
	# var = "world"
	# pipe = subprocess.Popen(["./x.pl", var], stdout=subprocess.PIPE)
	# result = pipe.stdout.read()

# print result
	# cmd /c perl "C:\_scripts\Markdown.pl" "$(FULL_CURRENT_PATH)" > "$(CURRENT_DIRECTORY)\$(NAME_PART).htm"
# cmd /c perl "C:\_scripts\SmartyPants.pl" "$(CURRENT_DIRECTORY)\$(NAME_PART).htm" > "$(CURRENT_DIRECTORY)\$(NAME_PART).html"

def insert_images(text):
	pass

	
def apply_template(text):
	pass
	# <p class="noindent">

	
def gb_strip(text):
	begin = r'\*\*\* START OF THIS PROJECT GUTENBERG EBOOK .*'
	end = r"End of Project Gutenberg's"
	
	m = re.search(begin, text)
	text = text[m.end():]
	m = re.search(end, text)
	text = text[:m.start()]
	
	return text
	
	
def find_chapters(text, markers=False):
	cmark = '@@@@'
	tlist = text.split('\n\n')
	i = 0
	last = ''
	temp = []
	for p in tlist:
		# if starting a new chapter
		c = last.find('chapter')
		# add chapter mark
		if c is not -1:
			mark = cmark+p if markers else p
			temp.append(mark)
			clist.append(i-1)
		else: temp.append(p)
		
		i += 1
		last = p.lower()
		# print last
		last = last.strip()
		# print last
		# if i>15: break
		
	
	for x in clist: temp[x] = CHAPTER+temp[x].strip()
	return '\n\n'.join(temp)
	# return temp
	# print cbreaks
	
	

if __name__ == '__main__':
	fname = sys.path[0]+'/pg11.txt'
	
	with open(fname, 'r') as f:
		text = find_chapters(gb_strip(f.read()))
	
	# print text
	# print clist
	# for x in clist: print text[x].strip()
	print to_html(text)
		
		