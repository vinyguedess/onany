citest:
	coverage run -m unittest discover
	coverage xml

clear:
	rm -rf build coverage dist onany.egg-info .coverage
	
deploy:
	python setup.py sdist bdist_wheel
	twine upload dist/*

test:
	coverage run -m unittest discover
	coverage html
	coverage report