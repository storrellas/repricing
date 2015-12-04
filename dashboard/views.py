from django.shortcuts import render
from django.http import HttpResponse

import logging
import json
logger = logging.getLogger('views')


def dashboard(request):

    

    # POST Method: Used to configure check issuing
    if request.method == 'POST':
    
        # Capture ASIN
        asin = request.POST.get('asin')        
        print( 'ASIN: ' + asin )

        
        # This is a dummy response. Should be beter done
        data = { 'maximum': 10, 'minimum': 3 }
        return HttpResponse(json.dumps(data), content_type='application/json')



    return render(request, "dashboard.html")