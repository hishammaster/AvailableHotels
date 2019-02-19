import sys
from datetime import date

from hotelsAPI.api.views.requestsHandler import requestHandlerWithParams

if __name__ == '__main__':
    if (len(sys.argv) <= 1):
        print(
            'Please provide URLS for APIs with parameters to be used ["from date", "to date", "city","number of adults"] i.e: http://api1.com http://api2.com {} {} {} {}'.format(
                date.today(), date.today(), "Amman", "5"))
    elif len(sys.argv) == 7:
        requestHandlerWithParams(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6])
    else:
        print("Mismatch parameters , should be 6 parameters")
        print(
            'Please provide URLS for APIs with parameters to be used ["from date", "to date", "city","number of adults"] i.e: http://api1.com http://api2.com {} {} {} {}'.format(
                date.today(), date.today(), "Amman", "5"))
