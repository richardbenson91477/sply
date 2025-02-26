all: install

dist:
	python -m build

install:
	pip install --force-reinstall --no-build-isolation --no-deps .

clean:
	rm -rf build sply.egg-info dist
