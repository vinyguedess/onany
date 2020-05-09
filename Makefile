citest:
	coverage run -m unittest discover
	coverage xml
	
deploy:
	python setup.py sdist bdist_wheel
	twine upload dist/*

test:
	coverage run -m unittest discover
	coverage html
	coverage report