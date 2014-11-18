""" Creating a data class for the BLS Employment Situation Report """

class JobsData(object):
	def __init__(self, month, year, jobs):
		self.month = month #the month the data refers to (e.g., number of jobs created in June)
		self.year = year
		self.jobs = jobs #number of jobs created or lost in a given month in thousands

class Report(object):
	def __init__(self, current_month, first_revision, second_revision):
		self.current = current_month
		self.first_revision = first_revision
		self.second_revision = second_revision
