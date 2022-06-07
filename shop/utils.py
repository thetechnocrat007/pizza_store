from numpy import busday_offset
from datetime import datetime
from pandas import Timestamp
from django.utils import timezone


def getBusinessDate():
    print(datetime.now())
    dt=busday_offset(datetime.now().date(), 0, roll='forward')
    tm = datetime.now().time()
    business_date = datetime.combine(Timestamp(dt).date(), tm)
    return business_date