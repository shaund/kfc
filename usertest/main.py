import cgi
import sys
import datetime
import urllib
# mispelled import wsgrief.handlers
#import toHTML working on script processing with out opening files doesn't work on appeng.

from google.appengine.ext import db
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app


#class TestBook(db.Model):
	#author = db.UserPropertry()
	#content = db.StringPropery(multiline=True)
	#date = db.DateTimePropertry(auto_now_add=True)

class MainPage(webapp.RequestHandler):
	def get(self):
		self.response.out.write("""
          <html>
            <body>
              <form action="/output" method="post">
                <div><textarea name="content" rows="50" cols="60"></textarea></div>
                <div><input type="submit" value="Test"></div>
              </form>
            </body>
          </html>""")
          
class TestText(webapp.RequestHandler):
	def post(self):
		self.response.out.write('<html><body>Your formatted text:<pre>')
		file=cgi.escape(self.request.get('content'))
		#tried to just pass a large string but it fail because we can't pass the string 
		#to the perl scripts without some modification as far as I got before bed
		self.response.out.write(file)
		self.response.out.write('</pre></body></html>')
		
application = webapp.WSGIApplication([('/', MainPage), ('/output', TestText)], debug=True)

def main():
	run_wsgi_app(application)

if __name__ == "__name__":
	main()

