from django import template

register = template.Library()

@register.filter(name = "get_range")
def get_range( value ):
	"""
    Filter - returns a list containing range made from given value
    Usage (in template):
	"""
	return range(1, int(value+1))

@register.filter(name = "className")
def className( value ): 
	"""
	Filter - returns the class name of value
	Usage (in template):
	"""
	return value.__class__.__name__