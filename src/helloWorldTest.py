#!usr/bin/python

import re
import sys
import unittest

submissions_dir = re.sub('/src', '/submissions', sys.path[0])
sys.path.insert(0, submissions_dir)

import helloWorld as hw

class FirstTest(unittest.TestCase):

	def test_helloWorld(self):
		self.assertEquals(hw.funtest(), 'Hello World!')

if __name__ == '__main__':
	unittest.main()