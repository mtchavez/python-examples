def loud(future_cls, future_cls_parents, future_cls_attr):
	attrs = ((name, value) for name, value in future_cls_attr.items() if not name.startswith('__'))
	# turn them into uppercase
	uppercase_attr = dict((name.upper(), value) for name, value in attrs)

	# let `type` do the class creation
	return type(future_cls, future_cls_parents, uppercase_attr)

__metaclass__ = loud

class Sprocket():

	name = 'default'
