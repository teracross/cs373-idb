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

# Businesses
def business1(request):
    context = RequestContext(request)
    # context_dict = {'message': "Hello World, business page 1"}
    return render_to_response('OperationRepo/business1.html', context_dict, context)

def business2(request):
    context = RequestContext(request)
    # context_dict = {'message': "Hello World, business page 2"}
    return render_to_response('OperationRepo/business2.html', context_dict, context)

def business3(request):
    context = RequestContext(request)
    # context_dict = {'message': "Hello World, business page 3"}
    return render_to_response('OperationRepo/business3.html', context_dict, context)

# Reviews
def review1(request):
    context = RequestContext(request)
    # context_dict = {'message': "Hello World, review page 1"}
    return render_to_response('OperationRepo/review1.html', context_dict, context)

def review2(request):
    context = RequestContext(request)
    # context_dict = {'message': "Hello World, review page 2"}
    return render_to_response('OperationRepo/review2.html', context_dict, context)

def review3(request):
    context = RequestContext(request)
    # context_dict = {'message': "Hello World, review page 3"}
    return render_to_response('OperationRepo/review3.html', context_dict, context)


# Users
def user1(request):
    context = RequestContext(request)
    # context_dict = {'message': "Hello World, user page 1"}
    return render_to_response('OperationRepo/user1.html', context_dict, context)
    
def user2(request):
    context = RequestContext(request)
    # context_dict = {'message': "Hello World, user page 2"}
    return render_to_response('OperationRepo/user2.html', context_dict, context)

def user3(request):
    context = RequestContext(request)
    # context_dict = {'message': "Hello World, user page 3"}
    return render_to_response('OperationRepo/user3.html', context_dict, context)

def splash(index):
	  context = RequestContext(request)
	  # context_dict = {'message' : "Hello World, splash page"}
	  return render_to_response('OperationRepo/index.html', context_dict, context)





