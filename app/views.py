from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template
import datetime

def index(request):
    t = get_template('base.html')
    html = t.render(Context({'current_date': 12356}))
    return HttpResponse(html)    

def date(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)
