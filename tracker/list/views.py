# Create your views here.
from django.db.models import Sum
from django.db.models import Count
from django.shortcuts import render_to_response, get_object_or_404
from tracker.list.models import Article, Impact, Training, TrainingType
from tracker.list.forms import ContactForm
from django.template import RequestContext
from django.core.mail import send_mail
from django.http import HttpResponseRedirect

attendancetotal = Training.objects.aggregate(attendance_total=Sum('attendance'))

storytotal = Article.objects.aggregate(story_total=Count('slug'))

trainingtotal = Training.objects.aggregate(training_total=Count('eventnumber'))

citytotal = Training.objects.aggregate(city_total=Count('city'))

def index(request):

	articles = Article.objects.all().order_by('-date')[:3]

	training = Training.objects.all().order_by('-date')[:5]

	return render_to_response('index.html', {'articles': articles, 'training': training, 'attendancetotal': attendancetotal['attendance_total'], 'storytotal': storytotal['story_total'], 'trainingtotal': trainingtotal['training_total'], 'citytotal': citytotal['city_total']})

def impact_list(request):
	#View for all impact types

	impacttypes = Impact.objects.all().order_by('-name')

	return render_to_response('impact.html', {'impacttypes': impacttypes})

def impact_detail(request, slug):
	#View for all articles with a certain impact types

	impacttype=get_object_or_404(Impact, slug=slug)

	impactcategories = Impact.objects.all().order_by('name')

	impactlist = impacttype.article_set.all().order_by('-date')

	return render_to_response('impact_detail.html', {'impacttype': impacttype, 'impactlist': impactlist, 'impactcategories': impactcategories})


def article_index(request):

	articles = Article.objects.all().order_by('-date')

	return render_to_response('article.html', {'articles': articles})

def article_detail(request, slug):

	article_detail=get_object_or_404(Article, slug=slug)

	article=Article.objects.get(slug=slug)

	return render_to_response('article_detail.html', {'article_detail': article_detail, 'article': article})

def training_index(request):

    training = Training.objects.all().order_by('-date')[:5]

    training_long = Training.objects.all()


    return render_to_response('training.html', {'training': training, 'training_long': training_long})

def training_detail(request, slug):

    training_detail=get_object_or_404(Training, slug=slug)

    training = Training.objects.get(slug=slug)

    articlelist = training_detail.article_set.all().order_by('-date')

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            message = 'Event' + '\n' + training.city + ' ' + training.type.name + ' - %s/%s/%s' %(training.date.month, training.date.day, training.date.year) + '\n' + '\n' + 'Headline:' + '\n' + cd['headline'] + '\n' + '\n' + 'Hyperlink:' + '\n' + cd['hyperlink'] + '\n' + '\n' + 'Byline:' + '\n' + cd['byline'] + '\n' + '\n' + 'Story summary:' + '\n' + cd['story_summary']
            send_mail('Proposed story for IRE story tracker', message, cd['email'], ['tony@ire.org'])
            return HttpResponseRedirect('/thanks/')
    else:
        form = ContactForm()

    return render_to_response('training_detail.html', {'training_detail': training_detail, 'training': training, 'articlelist': articlelist, 'form': form}, context_instance = RequestContext(request))

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            message = 'Event' + '\n' + cd['event_type'].name + ' ' + '%s/%s/%s' %(cd['event_date'].month, cd['event_date'].day, cd['event_date'].year) + '\n' + '\n' + 'Headline:' + '\n' + cd['headline'] + '\n' + '\n' + 'Hyperlink:' + '\n' + cd['hyperlink'] + '\n' + '\n' + 'Byline:' + '\n' + cd['byline'] + '\n' + '\n' + 'Story summary:' + '\n' + cd['story_summary']
            send_mail('Proposed story for IRE story tracker', message, cd['email'], ['tony@ire.org'])
            return HttpResponseRedirect('/thanks/')
    else:
        form = ContactForm()
    return render_to_response('contact_form.html', {'form': form}, context_instance = RequestContext(request))

def thanks(request):

    return render_to_response('thanks.html')

def map_api(request):

    # By default, get all of the dispatch objects in the database 
    points = Training.objects.all()

    # The GET query string passed at the end of any URL in your project can
    # be accessed like this (for example, in www.website.com/?type=1), "type=1"
    # is the GET string.
    if request.GET: # If your request has a GET string ...

        # Variables passed in via GET are made accessible via dictionary object.
        # In the example above, the Django representation of the type=1 GET string
        # would be {'type': 1}
        if request.GET.has_key('type'): # Check for a dictionary key called type

            # If it's there, get the value corresponding with that key and use it to
            # get the corresponding Type object from the database.
            type_slug = request.GET.get('type')
            filter_type = Type.objects.get(slug=type_slug)

            # Finally, filter the points based on that type
            points = points.filter(type=filter_type)

    # Render to response is the same here, with one addition. Because we're rendering a JSON
    # file and not an HTML page, we want browsers and other clients to see it as the correct
    # type of file. That's where the optional mimetype argument comes in.
    # Reference here: http://en.wikipedia.org/wiki/Internet_media_type
    return render_to_response('training.json', {'points': points}, mimetype="application/json")