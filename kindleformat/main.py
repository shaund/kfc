#!/usr/bin/env python

from __future__ import with_statement

import cgi, os, sys
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template
from google.appengine.api import users

t = ''
title= ''
length = ''

class BaseRequestHandler(webapp.RequestHandler):
	def generate (self, fileIn, values):
		template_values={}
		template_values.update(values)
		path = os.path.join(os.path.dirname(__file__), fileIn)
		self.response.out.write(template.render(path, template_values))
		
class Loader(BaseRequestHandler):
	def get(self):
		values = {"length": length, "title": title}
		self.generate("load.html", values)
		
class Load(BaseRequestHandler):
	def post(self):
		page = int(self.request.get("page")) * 160
		if page >= 0:
			text = ' '.join(t[page:page+160])
		else:
			page += 159
			text = ' '.join(t[page-160:page])
			
		self.response.out.write(text)
		
# class MyHandler(BaseRequestHandler):
    # def get(self):
		# self.redirect(users.create_login_url(self.request.uri))
		# user = users.get_current_user()
		# if user:
			# values = {"length": length, "title": title}
			# self.generate("load.html", values)
			# greeting = ("Welcome, %s! (<a href=\"%s\">sign out</a>)" % (user.nickname(), users.create_logout_url("/")))
		# else:
			# self.redirect(users.create_login_url(self.request.uri))

application = webapp.WSGIApplication([('/a', Loader), ('/load', Load)])

def main():
	global t, title, length
	loc = './text.htm'
	with open(loc, 'rb') as f: 
		t = f.read()
		title = t[:t.find('\n')]
	t = t.split()
	length = int(len(t)/160)
	
		# template_values = {
			# 't': t
		# }
	run_wsgi_app(application)
if __name__ == "__main__":
	main()
