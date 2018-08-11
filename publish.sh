git checkout master
rm -rf dist/
rm -rf build/
python setup.py sdist bdist_wheel
twine upload dist/*
