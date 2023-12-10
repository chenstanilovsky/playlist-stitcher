.PHONY: docker-build docker-run build upload

docker-build:
	docker-compose build

docker-run:
	docker-compose run playlist-stitcher

build:
	python3 setup.py develop

upload:
	python3 setup.py sdist bdist_wheel
	twine upload -r pypi --skip-existing dist/*