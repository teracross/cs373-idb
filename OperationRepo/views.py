from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response

def index(request):
    # Request the context of the request.
    # The context contains information such as the client's machine details, for example.
    context = RequestContext(request)

    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    context_dict = {'message': "Hello World"}

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    return render_to_response('OperationRepo/index.html', context_dict, context)

def business(request):
    context = RequestContext(request)
    context_dict = {'message': "Hello World, business page"}
    return render_to_response('OperationRepo/business.html', context_dict, context)

def review(request):
    context = RequestContext(request)
    context_dict = {'message': "Hello World, review page"}
    return render_to_response('OperationRepo/review.html', context_dict, context)

def user(request):
    context = RequestContext(request)
    context_dict = {'message': "Hello World, user page"}
    return render_to_response('OperationRepo/user.html', context_dict, context)
    
def splash(index):
	context = RequestContext(request)
	#context_dict = {'message' : "Hello World, splash page"}
	return render_to_response('OperationRepo/index.html', context_dict, context)
