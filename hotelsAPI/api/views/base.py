from django.http import HttpResponse
from django.http.response import JsonResponse

# View unused
def index(request):
    return JsonResponse('{"Hello":"World"}', safe=False)
