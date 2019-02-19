# AvailableHotels
Simple API to collect data from other APIS as hotel search solution

This is intended to have UI using Django Framework- still not implemented-.

This can be run using terminal by running "main.py" file.

API's Request:
- fromDate: DATE
- toDate: DATE
- city: IATA code (AUH)
- numberOfAdults: integer number
API's Response:
- provider: name of the provider (“BestHotels” or “CrazyHotels”)
- hotelName: Name of the hotel
- fare: fare per night
- amenities: array of strings

and the returned response will be sorted by hotel rate
