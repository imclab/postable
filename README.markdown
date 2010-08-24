# Postable.me

> Blog Anywhere via Email

## SMTP to HTTP

It all boils down to that.  Convert an email into a `POST` email request, and you're golden.  But good luck setting up a scalable email server! ;)  Google has stepped in an done this for us already.

The email as params looks like this:

    {"cc"=>"", "body"=>"Hello World!\n\nConvert my email to a POST!\n\n<em>Super Cool</em>", "sent"=>"Tue, 24 Aug 2010 00:54:26 -0500", "sender"=>"foo@bar.com", "to"=>"lance@viatropos2.appspot.com", "subject"=>"Testing... testing!"}
  
That's so cool!

## Install

First, you need to get up and running with Google App Engine (I know, I know).  Here's a helpful [getting started with GAE article on Squidoo](http://www.squidoo.com/Google-App-Engine).  I followed [this tutorial](http://www.digitalistic.com/2008/06/09/10-easy-steps-to-use-google-app-engine-as-your-own-cdn/) for setting up GAE as a CDN.

Once you get [Google App Engine installed](http://code.google.com/appengine/downloads.html), open the terminal and check to see if the commands work:

    cd postable/mailer
    appcfg.py update . # deploy app
    dev_appserver.py . # run dev server at http://localhost:8080/
    
Once you get the cdn setup, or the `dev_appserver.py` running, go to [http://localhost:8080/_ah/admin/inboundmail](http://localhost:8080/_ah/admin/inboundmail).  From there you an send mail.

Read the rest of the source to get going.

It should be able to send email pretty easily too.  Here are the [quotas/limits](http://code.google.com/appengine/docs/quotas.html) of sending/receiving emails on GAE.

Heroku has a [Sendgrid Addon](http://docs.heroku.com/sendgrid#sendgrid-free) which allows you to send 200 emails/day for free.  GAE lets you send 2000 emails a day for free.  Both are probably more than enough for the one-man shop.  But with GAE you can handle incoming emails (incoming vs. outgoing emails).  You can also [send email for free on heroku using gmail](http://blog.heroku.com/archives/2009/11/9/tech_sending_email_with_gmail/).

Just found [this](http://github.com/statianzo/yellowbrick.git) [blogging](http://jxs.me/2010/08/06/yellowbrick-an-email-blogging-example/).  [Sendgrid](http://wiki.sendgrid.com/doku.php). [Parse API](http://wiki.sendgrid.com/doku.php?id=parse_api).

> Point a subdomain MX record to our server, we parse incoming emails and post attachments and body contents to your web forms. Useful to have uploads@subdomain.yourdomain.com or interact with users through email.

## Resources

- http://docs.heroku.com/bamboo