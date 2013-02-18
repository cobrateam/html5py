from unittest import TestCase

import html5py
import urllib2


class ParseTest(TestCase):
    def test_parse(self):
        doc = html5py.Parse(urllib2.urlopen("http://www.andrewsmedina.com").read())
        for node in doc.xpath('//h3/a'):
            print(node.text)
