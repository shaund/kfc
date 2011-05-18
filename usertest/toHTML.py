#!/usr/bin/python

#in progress attempt to pair down the strip script into a class and pass a single object 
#from the html form, have to build some data basing features in
from __future__ import with_statement

import re
import os
import sys
import platform
from subprocess import Popen, PIPE

class toHTML
	clist = []
	CHAPTER = '<mbp:section>\n##'
	
	def process(text):
		stripedtext = find_chapters(gb_strip(text))
		return to_html(stripedtext)
	
	def to_html(text):
	
		markdown = sys.path[0]+'/Markdown.pl'
		smartypants = sys.path[0]+'/SmartyPants.pl'
		
		tfile = sys.path[0]+'/text.txt' # print markdown
		htmlfile = sys.path[0]+'/text.htm'
		output = ''
		
		if platform.system == 'Windows':
			perl = "cmd /c perl"
		elif platform.system == 'Darwin':
			perl = "perl"
		elif platform.system == 'Linux':
			perl = "perl"
		else :
			perl = "perl"
			
		#added some system compatability and fixed a writing error when no html file exsists	
		# os.system('"cmd /c perl "' + markdown + '" "' + tfile + '" > text.htm')
		
		with open(tfile, 'wb') as f: f.writelines(text)
		cmd = perl+' '+ markdown +' '+ tfile
		p = Popen([cmd], shell=True, stdin=PIPE, stdout=PIPE)
		output = p.stdout.read()
		with open(htmlfile, 'wb+') as f: f.writelines(output)	
		
		cmd = perl+' '+ smartypants +' '+ htmlfile
		p = Popen([cmd], shell=True, stdin=PIPE, stdout=PIPE)
		output = p.stdout.read()
		with open(htmlfile, 'rb+') as f: f.writelines(output)	
			
		
		return 'OKAY!'
		
	
		
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
		
		