import math # You can import the entire library

from math import sqrt # Or you can import specific functions from a library

from datetime import date, time, timedelta, timezone # You can import multiple functions from a library

import datetime as dt # You can represent imports with an alias (nickname)

from random import seed

print('\nSquare root of 49 is:', math.sqrt(49))
print('\nSquare root of 49 is:', sqrt(49))
print('\nWorking with datetime alias', dt.datetime.strftime(dt.datetime.now(), '%Y-%m-%d'))
