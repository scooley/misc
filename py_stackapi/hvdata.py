from stackapi import StackAPI, StackAPIError
from datetime import datetime, timedelta, date

try:
	site = StackAPI('stackoverflow')
except StackAPIError as e:
	print ("Error message: %s" % (e.message)) 

today = date.today()
year = timedelta(days=365)

# Questions related to Hyper-V

years = range(2016, 2005, -1)

tod = today
fromd = today - year

for y in years:
	questions = site.fetch('questions', tagged='hyper-v', fromdate=fromd, todate=tod, sort='votes')
	print '{0:5d} questions in {1}'.format(len(questions['items']), fromd)
	tod = tod - year
	fromd = fromd - year

