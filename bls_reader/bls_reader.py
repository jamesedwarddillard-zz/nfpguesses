""" Creating a function which reads in html of a BLS report website and
returns the key monthly jobs added as a Report data class """

from bs4 import BeautifulSoup
from bls_report_classes import *

def nfp_table_finder(report_soup):
	""" Identifies and returns the proper table on the Employment Situation Release """
	report_tables = report_soup.find_all('table')
	nfp_table = report_tables[1] #Table with NFP data is Summary Table B, the second table listed
	return nfp_table

def nfp_month_finder(nfp_table, report):
	""" Finds the relevant months on the Employment Situation Release a
	Report object with that information """

	nfp_table.header = nfp_table.thead.tr.find_all('th') #Turns the table header into a list of lists

	report.current.month = str(nfp_table.header[4].contents[0])
	report.current.year = str(nfp_table.header[4].contents[2])
	report.first_revision.month = str(nfp_table.header[3].contents[0])
	report.first_revision.year = str(nfp_table.header[3].contents[2])
	report.second_revision.month = str(nfp_table.header[2].contents[0])
	report.second_revision.year = str(nfp_table.header[2].contents[2])

	return report

def nfp_jobs_finder(nfp_table, report):
	jobs_list = [] #blank list to hold jobs values that come out
	nfp_jobs_subtable = nfp_table.find_all('tr')[2].find_all('td')
	for td in nfp_jobs_subtable:
		jobs_list.append(int(td.span.string))
	report.current.jobs = jobs_list[1]
	report.first_revision.jobs = jobs_list[2]
	report.second_revision.jobs = jobs_list[3]

	return report


def bls_report_reader(html_file):
	""" function that reads the html version of the BLS Employment Situation
	report, identifies the key data and returns a job report data class 
	"""
	#create JobsData objects
	current = JobsData()
	first_revision = JobsData()
	second_revision = JobsData()
	#create a Report object
	report = Report(current, first_revision, second_revision)

	report_soup = BeautifulSoup(html_file)
	nfp_table = nfp_table_finder(report_soup)
	report = nfp_month_finder(nfp_table, report)
	report = nfp_jobs_finder(nfp_table, report)
	return report
