""" Creating a data class for the BLS Employment Situation Report """

class JobsData(object):
	def __init__(self):
		self.month = None #the month the data refers to (e.g., number of jobs created in June)
		self.year = None
		self.jobs = None #number of jobs created or lost in a given month in thousands


class Report(object):
	def __init__(self, current_month, first_revision, second_revision):
		self.current = current_month
		self.first_revision = first_revision
		self.second_revision = second_revision
		self.release_time = None
		self.url = "" #url of the jobs report; blank by default
