# Developer Notes

## Build
```bash
python setup.py sdist bdist_wheel
```

## Deploy to PyPI
```bash
twine upload dist/*
```

Will be available at https://pypi.org/project/proxy-servant/
