# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import date

import requests
from django.test import TestCase
import unittest

from hotelsAPI.api.hotels.BaseHotel import BaseHotelRequest, BaseHotelResponse
from hotelsAPI.api.hotels.BestHotels import BestHotelsRequest, BestHotelsResponse
from hotelsAPI.api.hotels.CrazyHotels import CrazyHotelsRequest, CrazyHotelsResponse
from unittest import mock
import responses

from hotelsAPI.api.views.requestsHandler import requestHandler, getSortedResponse


class TestHotels(unittest.TestCase):

    def setUp(self):
        pass

    def test_BaseHotelReq(self):
        self.assertEqual(
            '{"fromDate": "None" , "toDate":"' + str(date.today()) + '","city":"Amman","numberofAdults":"5"}',
            BaseHotelRequest("", None, date.today(), 'Amman', "5").__str__())

    def test_BaseHotelRes(self):
        self.assertEqual('{{"provider": "{}" , "hotelName":"{}", "rate": {} , "fare":"{}","amenities":"{}"}}'.format(
            "BaseHotels", "Landmark", "4", "142.12", "5"),
            BaseHotelResponse("BaseHotels", "Landmark", "4", "142.12", "5").__str__())

    def test_BestHotelsReq(self):
        self.assertEqual(
            '{"fromDate": "None" , "toDate":"' + str(date.today()) + '","city":"Amman","numberofAdults":"5"}',
            BestHotelsRequest(None, date.today(), 'Amman', "5").__str__())

    def test_BestHotelsRes(self):
        self.assertEqual('{{"provider": "{}" , "hotelName":"{}", "rate": {} , "fare":"{}","amenities":"{}"}}'.format(
            "BestHotels", "Landmark", "4", "142.12", "5"),
            BestHotelsResponse("Landmark", "4", "142.12", "5").__str__())

    def test_CrazyHotelsReq(self):
        self.assertEqual(
            '{"from": "None" , "To":"' + str(date.today()) + '","city":"Amman","adultsCount":"5"}',
            CrazyHotelsRequest(None, date.today(), 'Amman', "5").__str__())

    def test_CrazyHotelsRes(self):
        self.assertEqual('{{"provider": "{}" , "hotelName":"{}", "rate": {} , "fare":"{}","amenities":"{}"}}'.format(
            "CrazyHotels", "Landmark", "4", "142.12", "5"),
            CrazyHotelsResponse("Landmark", "****", "142.12", "5").__str__())


# Our test case class
class HotelsAPIsTestCases(unittest.TestCase):
    @responses.activate
    def test_BestHotels404(self):
        bestHotelObj = BestHotelsRequest(date.today(), date.today(), 'Amman', 5)
        responses.add(responses.GET, bestHotelObj.buildUrl(),
                      json={'error': 'not found'}, status=404)
        resp = requests.get(bestHotelObj.buildUrl())
        assert resp.json() == {"error": "not found"}

        assert len(responses.calls) == 1
        assert responses.calls[0].request.url == bestHotelObj.buildUrl()
        assert responses.calls[0].response.text == '{"error": "not found"}'

    @responses.activate
    def test_CrazyHotels404(self):
        crazyHotelObj = CrazyHotelsRequest(date.today(), date.today(), 'Amman', 5)
        responses.add(responses.GET, crazyHotelObj.buildUrl(),
                      json={'error': 'not found'}, status=404)
        resp = requests.get(crazyHotelObj.buildUrl())
        assert resp.json() == {"error": "not found"}

        assert len(responses.calls) == 1
        assert responses.calls[0].request.url == crazyHotelObj.buildUrl()
        assert responses.calls[0].response.text == '{"error": "not found"}'

    @responses.activate
    def test_bestHotels200(self):
        bestHotelReqObj = BestHotelsRequest(date.today(), date.today(), 'Amman', 5)
        url = bestHotelReqObj.buildUrl()
        bestHotelResponseObj = BestHotelsResponse("Marriot", "5", "145.22", 2)
        json_response = bestHotelResponseObj.printResponse()

        responses.add(responses.GET, url,
                      json=json_response, status=200)
        resp = requests.get(url)
        assert resp.json() == json_response

        assert len(responses.calls) == 1
        assert (responses.calls[0].response.text) == '"' + json_response.replace('"', '\\"') + '"'

    @responses.activate
    def test_CrazyHotels200(self):
        crazyHotelReqObj = CrazyHotelsRequest(date.today(), date.today(), 'Amman', 5)
        url = crazyHotelReqObj.buildUrl()
        crazyHotelObj = CrazyHotelsResponse("Marriot", "5", "145.22", 2)
        json_response = crazyHotelObj.printResponse()

        responses.add(responses.GET, url,
                      json=json_response, status=200)
        resp = requests.get(url)
        assert resp.json() == json_response

        assert len(responses.calls) == 1
        assert (responses.calls[0].response.text) == '"' + json_response.replace('"', '\\"') + '"'

    @responses.activate
    def test_requestHandler200(self):
        responseResults = [BestHotelsResponse("A", "5", "142.22", "4").printResponse(),
                           BestHotelsResponse("B", 3, "152.22", "2").printResponse(),
                           BestHotelsResponse("C", "2", "112.22", "3").printResponse(),
                           CrazyHotelsResponse("D", "***", "99.22", "2").printResponse()]

        sortedResults, errors = getSortedResponse(date.today(), date.today(), 'Amman', 5)
        if (errors is not None):
            for error in errors:
                print(error)
        for result in sortedResults:
            print(result.printResponse())
        response = requestHandler(request)
        json_response = crazyHotelObj.printResponse()

        responses.add(responses.GET, url,
                      json=json_response, status=200)
        resp = requests.get(url)
        assert resp.json() == json_response

        assert len(responses.calls) == 1
        assert (responses.calls[0].response.text) == '"' + json_response.replace('"', '\\"') + '"'


def mocked_requests_get(*args, **kwargs):
    responseResults = [BestHotelsResponse("A", "5", "142.22", "4").printResponse(),
                       BestHotelsResponse("B", 3, "152.22", "2").printResponse(),
                       BestHotelsResponse("C", "2", "112.22", "3").printResponse(),
                       CrazyHotelsResponse("D", "***", "99.22", "2").printResponse()]

    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code

        def json(self):
            return self.json_data

    if args[0] is not None:
        return MockResponse(responseResults, 200)
    return MockResponse(None, 404)


if __name__ == '__main__':
    unittest.main()

#
# def test():
#     city = "irbid"
#     fromDate = date.today()
#     toDate = date.today()
#     adultsCount = 5
#     hotels_classes = ['hotelsAPI.api.hotels.BestHotels.BestHotelsRequest',
#                       'hotelsAPI.api.hotels.CrazyHotels.CrazyHotelsRequest']
#     hotels__res_classes = ['hotelsAPI.api.hotels.BestHotels.BestHotelsResponse',
#                            'hotelsAPI.api.hotels.CrazyHotels.CrazyHotelsResponse']
#     urls = []
#     responseObjects = []
#     index = 0
#     responseResults = [BestHotelsResponse("ffdf", 5, 142.22, 4),
#                        BestHotelsResponse("hhhhhh", 3, 152.22, 2),
#                        BestHotelsResponse("vcxvc", 2, 112.22, 3)]
#     # cxz = CrazyHotelsResponse("ffdf", "***", 99.22, 2)
#     for className in hotels_classes:
#         klass = import_class_from_string(className)
#         obj = klass(fromDate, toDate, city, adultsCount)
#         urls.append(obj.__str__())
#         # if (index == 1):
#         #     responseResults = [cxz]
#         for result in responseResults:
#             if (index == 1):
#                 break
#             resKlass = import_class_from_string(hotels__res_classes[index])
#             # hotelName, hotelRate, price, amenities)
#             obj_res_json = json.loads(result.__str__())
#             responseObjects.append(resKlass(obj_res_json['hotelName'], obj_res_json['rate'], obj_res_json['fare'],
#                                             obj_res_json['amenities']))
#         index = index + 1
#
#     responseObjects.sort(key=attrgetter('fare'), reverse=True)
#     # responseObjects.sort(key=lambda x: x.rate, reverse=True)  # sorted response objects based on rate
#     print(responseObjects)
#
#
# test()
