.DEFAULT_GOAL := dist

PROJECT := toronto-hydro-green-button
VERSION := 0.1.0

.PHONY: clean
clean:
	$(RM) -r dist/

.PHONY: dist
dist: dist/$(PROJECT)-$(VERSION).tar.gz

dist/$(PROJECT)-$(VERSION).tar.gz:
	python setup.py sdist
