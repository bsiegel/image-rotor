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
import random
import re
from google.appengine.api import urlfetch
from google.appengine.ext import webapp
from google.appengine.ext.webapp import util


def getImageURIs():
    pageURI = 'http://www.redbubble.com/people/rpgesus/journal/3882072-zombiemon'
    result = urlfetch.fetch(pageURI)
    if result.status_code == 200:
        body = result.content
        URIs = re.findall('http://images-?\d?\.redbubble\.net/img/clothing[^"]+\.jpg', body)
        return URIs

class MainHandler(webapp.RequestHandler):
    def get(self):
        imgURIs = getImageURIs()
        imgData = urlfetch.fetch(random.choice(imgURIs))
        self.response.headers['Content-Type'] = 'image/jpeg'
        if imgData.status_code == 200:
            self.response.out.write(imgData.content)


def main():
    application = webapp.WSGIApplication([('/zombiemon.jpg', MainHandler)],
                                         debug=True)
    util.run_wsgi_app(application)


if __name__ == '__zombiemon__':
    main()
