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
import webapp2
import jinja2
import os
from google.appengine.ext import ndb

jinja_environment = jinja2.Environment(loader=
    jinja2.FileSystemLoader(os.path.dirname(__file__)))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')
        template = jinja_environment.get_template('templates/template.html')
        self.response.out.write(template.render())


class PickUpGame(ndb.Model):
    sport = ndb.StringProperty()
    time = ndb.DateTimeProperty()
    location = ndb.KeyProperty(Location)
    players = ndb.KeyProperty(Player, repeated=True)

class Location(ndb.Model):
    address = ndb.StringProperty()

class Player(ndb.Model):
    #link this to the Users API
    nick_name = ndb.StringProperty()
    age = ndb.IntegerProperty()
    home_park = ndb.KeyProperty(Location)

montrose_beach=Location(address="555 N Lake Shore Drive")
wicker_park=Location(address="1600 N. Ashland")
player1=Player(name="nicki", age="17", home_park=wicker_park.key)
player2=Player(name="miles", age ="16", home_park=montrose_beach.key)
bball1 = PickUpGame(sport = "basketball", time="5:00", location = montrose_beach.key, players= [player1.key, player2.key])


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
