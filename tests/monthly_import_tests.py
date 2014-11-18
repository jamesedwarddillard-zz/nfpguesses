import unittest
import os

class TestReportReader(unittest.TestCase):
	""" Test the reading of the BLS monthly Employment Situation Report """

	def setUp(self):
		""" Test setup """
		pass

	def tearDown(self):
		""" Test teardown """
		pass

	def testReportReading(self):
	
		nfp09052014 = {}

		#testing the reading of the current month
		self.assertEqual(nfp09052014.current["month"], "08")
		self.assertEqual(nfp09052014.current["year"], "2014")
		self.assertEqual(nfp09052014.current["jobs"], 142)

		#testing the first revision of the previous month
		self.assertEqual(nfp09052014.first_revision["month"], "07")
		self.assertEqual(nfp09052014.first_revision["year"], "2014")
		self.assertEqual(nfp09052014.first_revision["jobs"], 267)

		#testing the second revision of the previous month
		self.assertEqual(nfp09052014.second_revision["month"], "06")
		self.assertEqual(nfp09052014.second_revision["year"], "2014")
		self.assertEqual(nfp09052014.second_revision["jobs"], 212)

if __name__ == "__main__":
	unittest.main()