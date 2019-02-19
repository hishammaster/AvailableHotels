from hotelsAPI.api.hotels.BaseHotel import BaseHotelRequest, BaseHotelResponse


# BestHotels class to form a request compatible with the request we want

class BestHotelsRequest(BaseHotelRequest):
    providerUrl = "http://www.bestHotels.com/"

    def __init__(self, fromDate, toDate, city, numberOfAdults):
        super(BestHotelsRequest, self).__init__(self.providerUrl, fromDate, toDate, city, numberOfAdults)

    def __init__(self, providerUrl, fromDate, toDate, city, numberOfAdults):
        super(BestHotelsRequest, self).__init__(providerUrl, fromDate, toDate, city, numberOfAdults)

    def buildUrl(self):
        url = self.providerUrl + "?from={}&To={}&city={}&adultsCount={}".format(self.fromDate, self.toDate, self.city,
                                                                                self.numberOfAdults)
        return url


# BestHotels class to form a response compatible with the response we want
class BestHotelsResponse(BaseHotelResponse):
    provider = "BestHotels"

    def __init__(self, hotelName, hotelRate, hotelFare, roomAmenities):
        super(BestHotelsResponse, self).__init__(self.provider, hotelName, hotelRate, hotelFare, roomAmenities)
