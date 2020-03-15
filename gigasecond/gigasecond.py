import datetime

def add(moment):
	gs = datetime.timedelta(seconds=1000000000)
	day = moment + gs

	return day