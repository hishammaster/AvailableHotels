from hotelsAPI.api.hotels.BaseHotel import BaseHotelRequest, BaseHotelResponse


# CrazyHotels class to form a request compatible with the request we want
class CrazyHotelsRequest(BaseHotelRequest):
    providerUrl = "http://www.crazyHotels.com/"

    def __init__(self, fromDate, toDate, city, numberOfAdults):
        super(CrazyHotelsRequest, self).__init__(self.providerUrl, fromDate, toDate, city, numberOfAdults)

    def __init__(self, providerUrl, fromDate, toDate, city, numberOfAdults):
        super(CrazyHotelsRequest, self).__init__(providerUrl, fromDate, toDate, city, numberOfAdults)

    def __str__(self):
        return '{{"from": "{}" , "To":"{}","city":"{}","adultsCount":"{}"}}'.format(self.fromDate,
                                                                                    self.toDate,
                                                                                    self.city,
                                                                                    self.numberOfAdults)

    def buildUrl(self):
        url = self.providerUrl + "?from={}&To={}&city={}&adultsCount={}".format(self.fromDate, self.toDate, self.city,
                                                                                self.numberOfAdults)
        return url


# CrazyHotels class to form a response compatible with the response we want

class CrazyHotelsResponse(BaseHotelResponse):
    provider = "CrazyHotels"

    def __init__(self, hotelName, hotelRate, fare, amenities):
        super(CrazyHotelsResponse, self).__init__(self.provider, hotelName, len(hotelRate), fare, amenities)
