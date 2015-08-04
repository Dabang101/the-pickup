#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from google.appengine.api import users
import webapp2
import jinja2
import os
from google.appengine.ext import ndb

jinja_environment = jinja2.Environment(loader=
    jinja2.FileSystemLoader(os.path.dirname(__file__)))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        sport = self.request.get("sport_form")
        location = self.request.get("location")
        home_template = jinja_environment.get_template('templates/home.html')

        user = users.get_current_user()
        if user:
            nickname=user.nickname()
            logout=users.create_logout_url('/')
            greeting = ('Welcome, %s! (<a href="%s">sign out</a>)'%(nickname, logout))
            temp_dic ={"signORlogout": greeting}
        else:
            login=users.create_login_url('/')
            greeting = ('<a href="%s">Sign in or register</a>.' %login)
            #self.response.out.write(greeting)
            temp_dic ={"signORlogout": greeting}

        self.response.out.write(home_template.render(temp_dic))

class Sport(ndb.Model):
    name = ndb.StringProperty()

class Location(ndb.Model):
    name = ndb.StringProperty()
    address = ndb.StringProperty()
    sports = ndb.KeyProperty(Sport, repeated = True)

basketball = Sport(name = "basketball")
basketball.put()
ultimate = Sport(name = "ultimate")
ultimate.put()
tennis = Sport(name = "tennis")
tennis.put()
soccer = Sport(name = "soccer")
soccer.put()
baseball = Sport(name = "baseball")
baseball.put()

class Player(ndb.Model):
    #link this to the Users API
    name = ndb.StringProperty()
    age = ndb.IntegerProperty()
    home_park = ndb.KeyProperty(Location)

class PickUpGame(ndb.Model):
    sport = ndb.StringProperty()
    time = ndb.StringProperty()
    location = ndb.KeyProperty(Location)
    players = ndb.KeyProperty(Player, repeated=True)


class SearchHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write("Go back...you forgot to enter your sport and/or location")
    def post(self):
        search_template = jinja_environment.get_template('templates/search.html')
        search_vars= {"sport": self.request.get("sport_form"),
                      "location": self.request.get("location_form"),

                     }
        self.response.out.write(search_template.render(search_vars))



montrose_beach = Location(address="555 N Lake Shore Drive")
wicker_park = Location(name="Wicker Park", address="1600 N. Ashland", sports=[basketball.key, ultimate.key])
player1 = Player(name="nicki", age=17)
    #, home_park=wicker_park.key)
player2 = Player(name="miles", age=16)
    #, home_park=montrose_beach.key)
bball1 = PickUpGame(sport = "basketball", time="5:00 pm")
    #, location = montrose_beach.key,
    #players= [player1.key, player2.key])


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/search', SearchHandler),
    #("/user", UserHandler)
], debug=True)
