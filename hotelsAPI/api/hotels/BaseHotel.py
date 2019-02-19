import datetime
from abc import abstractmethod

import simplejson as json
from datetime import date
from easydict import EasyDict as edict


# Base Classes for Requests and Responses

class BaseHotelRequest():
    providerUrl="http://localhost:8080/"
    def __init__(self, providerUrl, fromDate, toDate, city, numberOfAdults):
        self.providerUrl = providerUrl
        self.fromDate = fromDate
        self.toDate = toDate
        self.city = city
        numberOfAdults=int(numberOfAdults)
        if (numberOfAdults < 1):
            numberOfAdults = 1
        self.numberOfAdults = numberOfAdults

    def __str__(self):
        return '{{"fromDate": "{}" , "toDate":"{}","city":"{}","numberofAdults":"{}"}}'.format(self.fromDate,
                                                                                               self.toDate,
                                                                                               self.city,
                                                                                               self.numberOfAdults)

    @abstractmethod
    def buildUrl(self):
        url = self.providerUrl + "?fromDate={}&toDate={}&city={}&numberofAdults={}".format(self.fromDate, self.toDate,
                                                                                           self.city,
                                                                                           self.numberOfAdults)
        return url


class BaseHotelResponse():

    def __init__(self, provider, hotelName, rate, fare, amenities):
        self.provider = provider
        self.hotelName = hotelName
        rate = int(rate)
        fare = float(fare)
        amenities = int(amenities)
        if (rate < 1):
            rate = 1
        if (rate > 5):
            rate = 5
        self.rate = rate
        if (fare < 1):
            fare = 1
        if (fare > 5):
            far = 5
        self.fare = fare
        self.amenities = amenities

    def __str__(self):
        return '{{"provider": "{}" , "hotelName":"{}", "rate": {} , "fare":"{}","amenities":"{}"}}'.format(
            self.provider,
            self.hotelName,
            self.rate,
            self.fare,
            self.amenities)
    def printResponse(self):
        return '{{"provider": "{}" , "hotelName":"{}" , "fare":"{}","amenities":"{}"}}'.format(
            self.provider,
            self.hotelName,
            self.fare,
            self.amenities)
