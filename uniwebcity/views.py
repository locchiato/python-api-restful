from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import loader

from professors.models import Professor
from departments.models import Department

#@login_required(login_url="/login/")
def index(request):
    
    context = {
        'segment': 'index',
        'professors': Professor.objects.all().order_by('-id'),
        'departments': Department.objects.all().order_by('-id')
        }

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))

def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))

        context['segment'] = load_template

        if 'departments' in load_template:
            context['departments'] = Department.objects.all().order_by('-id')
            html_template = loader.get_template('departments/index.html')
        
        if 'professors' in load_template:
            context['professors'] = Professor.objects.all().order_by('-id')
            html_template = loader.get_template('professors/index.html')
        
        
        return HttpResponse(html_template.render(context, request))

    except TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))
