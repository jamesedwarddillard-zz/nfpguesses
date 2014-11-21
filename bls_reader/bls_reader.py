""" Creating a function which reads in html of a BLS report website and
returns the key monthly jobs added as a Report data class """

from bs4 import BeautifulSoup
from bls_report_classes import *

def nfp_table_finder(report_soup):
	""" Identifies and returns the proper table on the Employment Situation Release """
	report_tables = report_soup.find_all('table')
	nfp_table = report_tables[1] #Table with NFP data is Summary Table B, the second table listed
	return nfp_table

def nfp_month_finder(nfp_table):
	""" Finds the relevant months on the Employment Situation Release and returns them 
	as JobsData objects """

	#create the JobsData objects
	current = JobsData()
	first_revision = JobsData()
	second_revision = JobsData()

	nfp_table.header = nfp_table.thead.tr.find_all('th') #Turns the table header into a list of lists

	current.month = nfp_table.header[4].contents[0]
	current.year = nfp_table.header[4].contents[2]
	first_revision.month = nfp_table.header[3].contents[0]
	first_revision.year = nfp_table.header[3].contents[2]
	second_revision.month = nfp_table.header[2].contents[0]
	second_revision.year = nfp_table.header[2].contents[0]
	
	nfp_months = {'current': current, 'first_revision': first_revision, 'second_revision': second_revision}
	return nfp_months

def bls_report_reader(html_file):
	""" function that reads the html version of the BLS Employment Situation
	report, identifies the key data and returns a job report data class 
	"""

	report_soup = BeautifulSoup(html_file)
	nfp_table = nfp_table_finder(report_soup)
	nfp_months = nfp_month_finder(nfp_table)
