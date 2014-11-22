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

	def testPastReportReading(self):
		#importing a past report (sept 2014) for a test
		sept_2014_html = open(os.path.abspath('../past_reports/09052014.html'))
		oct_2014_html = open(os.path.abspath('../past_reports/10032014.html'))
		nov_2014_html = open(os.path.abspath('../past_reports/11072014.html'))
    
		sept_2014_report = bls_report_reader(sept_2014_html)
		oct_2014_report = bls_report_reader(oct_2014_html)
		nov_2014_report = bls_report_reader(nov_2014_html)

		#testing the reading of the current month
		self.assertEqual(sept_2014_report.current.month, "Aug.")
		self.assertEqual(sept_2014_report.current.year, "2014")
		self.assertEqual(sept_2014_report.current.jobs, 142)

		self.assertEqual(oct_2014_report.current.month, "Sept.")
		self.assertEqual(oct_2014_report.current.year, "2014")
		self.assertEqual(oct_2014_report.current.jobs, 248)

		self.assertEqual(nov_2014_report.current.month, "Oct.")
		self.assertEqual(nov_2014_report.current.year, "2014")
		self.assertEqual(nov_2014_report.current.jobs, 214)

		#testing the first revision of the previous month
		self.assertEqual(sept_2014_report.first_revision.month, "July")
		self.assertEqual(sept_2014_report.first_revision.year, "2014")
		self.assertEqual(sept_2014_report.first_revision.jobs, 212)

		self.assertEqual(oct_2014_report.first_revision.month, "Aug.")
		self.assertEqual(oct_2014_report.first_revision.year, "2014")
		self.assertEqual(oct_2014_report.first_revision.jobs, 180)

		self.assertEqual(nov_2014_report.first_revision.month, "Sept.")
		self.assertEqual(nov_2014_report.first_revision.year, "2014")
		self.assertEqual(nov_2014_report.first_revision.jobs, 256)

		#testing the second revision of the previous month
		self.assertEqual(sept_2014_report.second_revision.month, "June")
		self.assertEqual(sept_2014_report.second_revision.year, "2014")
		self.assertEqual(sept_2014_report.second_revision.jobs, 267)

		self.assertEqual(oct_2014_report.second_revision.month, "July")
		self.assertEqual(oct_2014_report.second_revision.year, "2014")
		self.assertEqual(oct_2014_report.second_revision.jobs, 243)

		self.assertEqual(nov_2014_report.second_revision.month, "Aug.")
		self.assertEqual(nov_2014_report.second_revision.year, "2014")
		self.assertEqual(nov_2014_report.second_revision.jobs, 203)

	def testCurrentReportReading(self):
		#importing an example of a current report (nov 2014) for a test
		nov_2014_html = open(os.path.abspath('../past_reports/09052014.html'))

		nov_2014_report = bls_report_reader(nov_2014_html)

		#testing the reading of the current month
		self.assertEqual(nov_2014_report.current.month, "Oct.")
		self.assertEqual(nov_2014_report.current.year, "2014")
		self.assertEqual(nov_2014_report.current.jobs, 214)

		#testing the first revision of the previous month
		self.assertEqual(nov_2014_report.first_revision.month, "Sept.")
		self.assertEqual(nov_2014_report.first_revision.year, "2014")
		self.assertEqual(nov_2014_report.first_revision.jobs, 256)

		#testing the second revision of the previous month
		self.assertEqual(nov_2014_report.second_revision.month, "Aug.")
		self.assertEqual(nov_2014_report.second_revision.year, "2014")
		self.assertEqual(nov_2014_report.second_revision.jobs, 203)

	def testNoTableError(self):
		not_a_jobs_report_html = open(os.path.abspath('../past_reports/not_a_jobs_report.html'))

		not_a_jobs_report = bls_report_reader(not_a_jobs_report_html)

		pass



if __name__ == "__main__":
	unittest.main()