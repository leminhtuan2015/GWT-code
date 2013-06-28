import cgi
import datetime
import wsgiref.handlers

from google.appengine.ext import db
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import blobstore
from google.appengine.ext.webapp import blobstore_handlers
from google.appengine.api import images
from google.appengine.api import users
#from user import Login
#from user import User

class FlashCardDB(db.Model):
    cardid = db.IntegerProperty()
    #userid = db.IntegerProperty()
    userid = db.StringProperty()
    type = db.IntegerProperty()
    cardsetid = db.IntegerProperty()
    boxnum = db.IntegerProperty()
    question = db.StringProperty(multiline=True)
    answer = db.StringProperty(multiline=True)
    createddate = db.DateProperty(auto_now_add=True)
    createdtime = db.TimeProperty(auto_now_add=True)

class CardSetDB(db.Model):
    #cardsetid = db.IntegerProperty()
    #userid = db.IntegerProperty()
    userid = db.StringProperty()
    title = db.StringProperty()
    description = db.StringProperty(multiline=True)
    tags = db.StringProperty(multiline=True)
    #private = db.BooleanProperty()
    createddate = db.DateProperty(auto_now_add=True)
    createdtime = db.TimeProperty(auto_now_add=True)
    
class Photo(db.Model):
	avatar = db.BlobProperty()
    
class UserDB(db.Model):
    user = db.UserProperty()
    
class MainPage(webapp.RequestHandler):
    def get(self):
      #self.response.headers['Content-Type'] = 'text/plain'
      user = users.get_current_user()
      if not user:
        self.redirect('/')        

      cardSet = db.GqlQuery("SELECT * FROM FlashCardDB WHERE userid= :1 ORDER BY __key__ DESC", user.user_id())
      self.response.out.write('<cardset>')
      #self.response.out.write('<totalcardnum>%s</totalcardnum>' % str(db.Query(FlashCardDB).count()))
      #self.response.out.write('<totalcardnum>%s</totalcardnum>' % str(cardSet.count()))
      self.response.out.write('<username>%s</username>' % user.nickname())
      #self.response.out.write('<cardsetid>%s</cardsetid>' % card.cardsetid)
      self.response.out.write('<cardnum>%s</cardnum>' % str(cardSet.count()))
      for card in cardSet:
        self.response.out.write('<card>')
        self.response.out.write('<cardid>%s</cardid>' % card.key().id())
        self.response.out.write('<question>%s</question>' % card.question)
        self.response.out.write('<answer>%s</answer>' % card.answer)
        self.response.out.write('<boxnum>%s</boxnum>' % card.boxnum)
        self.response.out.write('<date>%s</date>' % card.createddate)
        self.response.out.write('<time>%s</time>' % card.createdtime)
        self.response.out.write('</card>')
      self.response.out.write('</cardset>')

class getUser(webapp.RequestHandler):
    def get(self):
      user = users.get_current_user()
      if not user:
        self.redirect('/')        

      self.response.out.write('<user>')
      self.response.out.write('<username>%s</username>' % user.nickname())
      self.response.out.write('</user>')	
	
class SaveCard(webapp.RequestHandler):
    def post(self):
      user = users.get_current_user()
      if not user:
        self.redirect('/')        

      cardsetid = int(self.request.get('cardsetid'))
      if cardsetid > 0:
          cardSet = db.GqlQuery("SELECT * FROM FlashCardDB WHERE cardsetid = :1", cardsetid)
          for card in cardSet:
              card.delete()
      else :
          cardSet = CardSetDB()
          #cardSet.cardsetid = cardSetId
          cardSet.userid = user.user_id()
          #cardSet.userid = "1"
          cardSet.title = "CardSet Title"
          cardSet.description = "CardSet Description"
          cardSet.tags = "tags"
          #cardSet.private = false;
          cardSet.put()
          cardsetid = cardSet.key().id()
          
      cardNum = int(self.request.get('cardnum'))
      for i in range(1, cardNum + 1):
          card = FlashCardDB()
          card.cardid = 1;
          card.cardsetid = cardsetid;
          card.boxnum = 1;
          card.type = 1;
          card.userid = user.user_id();
          card.question = self.request.get('question' + str(i))
          card.answer = self.request.get('answer' + str(i))
          card.put()
      #send(self)
      self.response.out.write('<cardset>')
      self.response.out.write('<cardsetid>%s</cardsetid>' % cardsetid)
      self.response.out.write('</cardset>')
      #self.redirect('/savecard?show=true')


class UpdateCard(webapp.RequestHandler):
    def post(self):
      user = users.get_current_user()
      if not user:
        self.redirect('/') 
          
      cardid = int(self.request.get('cardid'))
      #card = db.get(Key.from_path("FlashCardDB", cardid))
      card = FlashCardDB.get_by_id(cardid)
      #if not card:
         #card = FlashCardDB(cardid=1, cardsetid=??, boxnum=1, type=1, userid=user.user_id(), 
         #           question=self.request.get('question'), answer=self.request.get('answer'))
      if card:
        card.question = self.request.get('question')
        card.answer = self.request.get('answer')
        card.put()

class DeleteCard(webapp.RequestHandler):
    def post(self):
      user = users.get_current_user()
      if not user:
        self.redirect('/') 
          
      cardid = int(self.request.get('cardid'))
      #card = db.get(Key.from_path("FlashCardDB", cardid))
      card = FlashCardDB.get_by_id(cardid)
      #if not card:
         #card = FlashCardDB(cardid=1, cardsetid=??, boxnum=1, type=1, userid=user.user_id(), 
         #           question=self.request.get('question'), answer=self.request.get('answer'))
      if card:
        card.delete()

class UpdateBox(webapp.RequestHandler):
    def post(self):
      user = users.get_current_user()
      if not user:
        self.redirect('/') 
          
      cardnum = int(self.request.get('cardnum'))
      
      for i in range(1, cardnum + 1):
        cardid = int(self.request.get('cardid' + str(i)))
        card = FlashCardDB.get_by_id(cardid)
        if card:
          card.boxnum = int(self.request.get('boxnum' + str(i)))
          card.put()

class upload(blobstore_handlers.BlobstoreUploadHandler):
    def post(self):
      greeting = Photo()
      greeting.content = self.request.get("content")
      avatar = self.request.get("img")
      greeting.avatar = db.Blob(avatar)
      #avatar = images.resize(self.request.get("img"), 32, 32)
      greeting.put()
      self.redirect('/')
      #upload_files = self.get_uploads('myPicture')
      #blob_info = upload_files[0]
      #self.redirect('/serve/%s' % blob_info.key())

class showPhoto(webapp.RequestHandler):
    def get(self):
      query_str = "SELECT * FROM Photo ORDER BY __key__ DESC LIMIT 10"
      greetings = db.GqlQuery (query_str)
      for greeting in greetings:
          self.response.out.write("<div><img src='img?img_id=%s'></img>" % greeting.key())

class Image(webapp.RequestHandler):
    def get(self):
        greetinggs = db.GqlQuery("SELECT * FROM Photo WHERE __key__= :1", db.Key(self.request.get("img_id")))
        self.response.out.write(greetinggs.count())
        for greeting in greetinggs:
          if greeting.avatar:
            self.response.headers['Content-Type'] = "image/png"
            self.response.out.write("Photo")
            self.response.out.write(greeting.avatar)
          else:
            self.response.out.write("No image")
	
class DeleteCards(webapp.RequestHandler):
    def get(self):
      user = users.get_current_user()
      if not user:
        self.redirect('/')        

      #self.response.headers['Content-Type'] = 'text/plain'
      cards = db.GqlQuery("SELECT * FROM FlashCardDB WHERE userid= :1", user.user_id())
      for card in cards:
        card.delete()

      cards = db.GqlQuery("SELECT * FROM CardSetDB WHERE userid= :1", user.user_id())
      for card in cards:
        card.delete()
        
class User(webapp.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            self.response.headers['Content-Type'] = 'text/plain'
            self.response.out.write('Hello, ' + user.nickname())
        else:
            self.redirect(users.create_login_url(self.request.uri))
            
class Login(webapp.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            greeting = ("Welcome, %s with id %s! (<a href=\"%s\">sign out</a>)<br>" % (user.nickname(), user.user_id(), users.create_logout_url("/logout")))
            greeting += ("<a href=\"/create/\">Create</a> new cards<br>")
            greeting += ("<a href=\"/flashcard/\">Study</a> your cards<br>")
            #self.redirect('/flashcard/')
        else:
            greeting = ("<a href=\"%s\">Sign in or register</a>." % users.create_login_url("/"))
        self.response.out.write("<html><body>%s</body></html>" % greeting)        

class Logout(webapp.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            greeting = ("Welcome, %s with id %s! (<a href=\"%s\">sign out</a>)" % (user.nickname(), user.user_id(), users.create_logout_url("/logout")))
        else:
            greeting = ("<a href=\"%s\">Sign in or register</a>." % users.create_login_url("/"))
        self.response.out.write("<html><body>%s</body></html>" % greeting)        

application = webapp.WSGIApplication([
	('/', Login),
    ('/logout', Logout),
    ('/getuser', getUser),
    ('/view', MainPage),
    ('/savecard', SaveCard),
    ('/updatecard', UpdateCard),
    ('/updatebox', UpdateBox),
    ('/deletecards', DeleteCards),
    ('/deletecard', DeleteCard)
], debug=True)

def main():
    wsgiref.handlers.CGIHandler().run(application)

if __name__ == '__main__':
    main()
