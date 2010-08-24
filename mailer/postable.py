import logging, email, inspect
from google.appengine.ext import webapp 
from google.appengine.ext.webapp.mail_handlers import InboundMailHandler 
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.api import urlfetch
import urllib

class Postable(InboundMailHandler):
  def get_payload(self, message):
      for (mime_type, data) in message.bodies('text/html'):
        return data.decode()
        
  def receive(self, message):
      url = "http://postable.me/posts"
      body = self.get_payload(message)
      cc = ""
      try:
        cc = str(mail_message.cc)
      except:
        cc = ""

      try:
        date = str(message.date)
      except:
        date = ""

      # "original": str(message.original.as_string())
          
      form_fields = {
        "sender": str(message.sender),
        "subject": str(message.subject),
        "to": str(message.to),
        "cc": cc,
        "sent": date,
        "body": str(body)
      }
      # str(message.bodies('text/plain'))
      form_data = urllib.urlencode(form_fields)
      logging.info(form_data)
      result = urlfetch.fetch(url = url, payload = form_data, method = urlfetch.POST, headers={'Content-Type': 'application/x-www-form-urlencoded'})

application = webapp.WSGIApplication([Postable.mapping()], debug = True)

def main():
  run_wsgi_app(application)

if __name__ == "__main__":
  main()