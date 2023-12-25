

1. set new version in setup.py
2. update version badge in readme.md
3. run bash commands
```bash
python -m pip install build
pip install twine
python3 -m build
twine upload dist/*
```
4. enter username and password