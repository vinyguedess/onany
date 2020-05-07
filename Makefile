deploy:
	python setup.py sdist
	twine upload dist/*

test:
	coverage run -m unittest discover
	coverage html
	coverage report
