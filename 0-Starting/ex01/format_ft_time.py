import datetime

date = datetime.datetime.now()

date_sec = date.timestamp()

print("Seconds since January 1, 1970:", '{0:,.4f}'.format(date_sec), "or", "{:.2e}".format(date_sec) , "in scientific notation")
print(date.strftime("%b %d %Y"))