import threading


def worker():
	print threading.currentThread().getName()

def naming(name=None):
	if name:
		thread = threading.Thread(name=name, target=worker)
	else:
		thread = threading.Thread(target=worker)
	thread.start()
