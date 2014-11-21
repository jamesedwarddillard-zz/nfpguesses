import unittest
import os
import sys

sys.path.append(os.path.abspath('../bls_reader'))
sys.path.append(os.path.abspath('../past_reports'))

from bls_report_classes import *
from bls_reader import *


class TestReportReader(unittest.TestCase):
	""" Test the reading of the BLS monthly Employment Situation Report """

	def setUp(self):
		""" Test setup """
		pass

	def tearDown(self):
		""" Test teardown """
		pass

def testReportReading(self):

		#importing a past report for a test
		sept_2014_html = open(os.path.abspath('../past_reports/09052014.html'))
    
		sept_2014_report = bls_report_reader(sept_2014_html)

		#testing the reading of the current month
		self.assertEqual(sept_2014_report.current.month, "Aug.")
		self.assertEqual(sept_2014_report.current.year, "2014")
		self.assertEqual(sept_2014_report.current.jobs, 142)

		#testing the first revision of the previous month
		self.assertEqual(sept_2014_report.first_revision.month, "July")
		self.assertEqual(sept_2014_report.first_revision.year, "2014")
		self.assertEqual(sept_2014_report.first_revision.jobs, 212)

		#testing the second revision of the previous month
		self.assertEqual(sept_2014_report.second_revision.month, "June")
		self.assertEqual(sept_2014_report.second_revision.year, "2014")
		self.assertEqual(sept_2014_report.second_revision.jobs, 267)

if __name__ == "__main__":
	unittest.main()