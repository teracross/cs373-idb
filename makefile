all:

clean:
	rm -f *.pyc
	rm -f models.html

models.html: models.py
	epydoc IDB