from operator import attrgetter
from datetime import date
import requests
import json
from django.http import JsonResponse

from hotelsAPI.api.hotels.BestHotels import BestHotelsResponse
from hotelsAPI.api.hotels.CrazyHotels import CrazyHotelsResponse

CITY_ATT = 'city'
FROM_ATT = 'from'
TO_ATT = 'to'
ADULTS_ATT = 'adultsNum'


def requestHandler(request):
    if request.method == 'GET':
        city = request.GET.get(CITY_ATT)
        fromDate = request.GET.get(FROM_ATT)
        toDate = request.GET.get(TO_ATT)
        adultsCount = request.GET.get(ADULTS_ATT)
        sortedResults, errors = getSortedResponse(None, None, fromDate, toDate, city, adultsCount)
        return sortedResults, errors


def requestHandlerWithParams(api1, api2, fromDate, toDate, city, adultsCount):
    sortedResults, errors = getSortedResponse(api1, api2, fromDate, toDate, city, adultsCount)
    if (errors is not None):
        for error in errors:
            print(error)
    for result in sortedResults:
        print(result.printResponse())
    return sortedResults, errors


def getSortedResponse(api1, api2, fromDate, toDate, city, adultsCount):
    hotels_req_classes = ['hotelsAPI.api.hotels.BestHotels.BestHotelsRequest',
                          'hotelsAPI.api.hotels.CrazyHotels.CrazyHotelsRequest']
    hotels__res_classes = ['hotelsAPI.api.hotels.BestHotels.BestHotelsResponse',
                           'hotelsAPI.api.hotels.CrazyHotels.CrazyHotelsResponse']

    responseObjects = []
    errors = []
    index = 0
    # loop through requests to APIs
    for className in hotels_req_classes:
        klass = import_class_from_string(className)  # reverse call to classes
        if (api1 is None or api2 is None):
            obj = klass(fromDate, toDate, city, adultsCount)
        else:
            if index == 0:
                obj = klass(api1, fromDate, toDate, city, adultsCount)
            else:
                obj = klass(api2, fromDate, toDate, city, adultsCount)
        r = requests.get(obj.providerUrl, params=obj.__str__())  # hit API with params sent via request
        # make sure status code is OK  with no exceptions
        if (r.status_code == 200 and r.raise_for_status() is None):
            # Get response classes by reflection
            resKlass = import_class_from_string(hotels__res_classes[index])
            responseResults = r.json()  # Json format of response
            # create response objects and add them to list
            responseObjects = extractResultsFromResponse(responseResults, resKlass)
        else:
            errors.append("Something went wrong! : {}".format(r.raise_for_status()))
        index = index + 1

    responseObjects.sort(key=attrgetter('rate'), reverse=True)  # sorted response objects based on rate
    return responseObjects, errors


def extractResultsFromResponse(resJson, resKlass):
    responseObjects = []
    for result in resJson:
        responseObjects.append(
            resKlass(result['hotelName'], result['rate'], result['fare'],
                     result['amenities']))
    return responseObjects


# Reverse call to retrieve class
def import_class_from_string(path):
    from importlib import import_module
    module_path, _, class_name = path.rpartition('.')
    mod = import_module(module_path)
    klass = getattr(mod, class_name)
    return klass
