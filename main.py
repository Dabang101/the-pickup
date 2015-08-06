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


class Sport(ndb.Model):
    name = ndb.StringProperty()

class Location(ndb.Model):
    name = ndb.StringProperty()
    address = ndb.StringProperty()
    sports = ndb.KeyProperty(Sport, repeated = True)


class MainHandler(webapp2.RequestHandler):


    def get(self):

        if Sport.query().fetch() !=[]:
            pass
        else:
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
            montrose_beach = Location(name="Montrose Beach", address="555 N Lake Shore Drive", sports = [soccer.key, ultimate.key])
            montrose_beach.put()
            wicker_park = Location(name="Wicker Park", address="1600 N. Ashland 60622", sports=[basketball.key, ultimate.key, baseball.key])
            wicker_park.put()
            humboldt_park = Location(name="Humboldt Park", address="1400 N Humboldt Dr 60622" ,sports=[tennis.key, basketball.key, ultimate.key])
            humboldt_park.put()
            smith_park = Location(name="Smith Park",address="2526 W Grand Ave 60612" ,sports=[basketball.key, ultimate.key])
            smith_park.put()

        sport = self.request.get("sport_form")
        location = self.request.get("location")
        home_template = jinja_environment.get_template('templates/home.html')

        user = users.get_current_user()
        if user:
            nickname=user.nickname()
            logout=users.create_logout_url('/')
            greeting = ('<a href="%s"> Welcome, %s! sign out</a>'%(logout, nickname))
            temp_dic ={"signORlogout": greeting}
        else:
            login=users.create_login_url('/')
            greeting = ('<a href="%s">Sign in or register</a>' %login)
            #self.response.out.write(greeting)
            temp_dic ={"signORlogout": greeting}

        self.response.out.write(home_template.render(temp_dic))


class ResultsHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write("Go back...you forgot to enter your sport and/or location")
    def post(self):
        results_template = jinja_environment.get_template('templates/results.html')
        sport_key = Sport.query(Sport.name== self.request.get("sport_form")).fetch()[0].key
        result_location = Location.query(Location.sports == sport_key).fetch()
        results_vars = {"sport": self.request.get("sport_form"),
                        "location": self.request.get("location_form"),
                        "results": result_location
                       }
        self.response.out.write(results_template.render(results_vars))

class AddedHandler(webapp2.RequestHandler):
    def get(self):
        sport_key = None
        sportadded = self.request.get("addsport").lower()
        add_template = jinja_environment.get_template('templates/add.html')
        self.response.out.write(add_template.render())
        # if the sport exists, sport_key is known
        # self.response.write(Sport.query(Sport.name == sportadded).fetch())
        if Sport.query(Sport.name == sportadded).fetch():
            sport_key = Sport.query(Sport.name == sportadded).fetch()[0].key
            #self.response.write("Your sport already exists")
        # else, add sport and get new key
        else:
            sport = Sport(name=sportadded)
            sport.put()
            sport_key = sport.key
        addeditem = Location(name = self.request.get("addname"),
                              address = self.request.get("addlocation"),
                              sports = [sport_key])
        addeditem.put()

class Thank_youHandler(webapp2.RequestHandler):
    def get(self):
        Thank_you_template = jinja_environment.get_template('templates/Thank_you.html')
        self.response.out.write(Thank_you_template.render())
        sport_key = None
        sportadded = self.request.get("addsport").lower()
        # if the sport exists, sport_key is known
        # self.response.write(Sport.query(Sport.name == sportadded).fetch())
        if Sport.query(Sport.name == sportadded).fetch():
            sport_key = Sport.query(Sport.name == sportadded).fetch()[0].key
            #self.response.write("Your sport already exists")
        # else, add sport and get new key
        else:
            sport = Sport(name=sportadded)
            sport.put()
            sport_key = sport.key
        addeditem = Location(name = self.request.get("addname"),
                             address = self.request.get("addlocation"),
                             sports = [sport_key])
        addeditem.put()


class AboutHandler(webapp2.RequestHandler):
    def get(self):
        about_template = jinja_environment.get_template('templates/about.html')
        self.response.out.write(about_template.render())


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/results', ResultsHandler),
    ('/added', AddedHandler),
    ('/about', AboutHandler),
    ("/Thank_you", Thank_youHandler)
], debug=True)
