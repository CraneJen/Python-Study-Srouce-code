import datetime
today = datetime.date.today()
print(today)

nextweek = today + datetime.timedelta(weeks=1)
print(nextweek)

# fmt = '%Y-%m-%d %H-%M-%S'
# now = datetime.datetime.now().strftime(fmt)
now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print(now)
