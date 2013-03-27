import threading


def simple():
	def describe(_id):
		print 'Thread %s' % _id
		return 'Thread %s' % _id

	for i in range(3):
		thread = threading.Thread(target=describe, args=(i,))
		thread.start()
