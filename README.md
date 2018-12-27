# mylastfm

This is a git repository for keeping track of my last.fm data and code for retrieval and analysis.

Goals:
- [ ] separate tables for scrobbles, artists, tags, etc.
- [ ] keep track of last update time for info-resources like tags, wikis etc.
- [ ] generic functions for graphing data

---

## setup

Add a file `pylast_config.py` to the root directory containing: 

```python
import pylast

API_KEY = # YOUR API KEY
API_SECRET = # YOUR SECRET KEY
USERNAME = # YOUR USERNAME

NETWORK = pylast.LastFMNetwork(api_key=API_KEY, api_secret=API_SECRET, username=USERNAME)
```

---

## Implementation Notes

Uses `Python 3.7.0`.

I used `virtualenv` and `pyenv`. To avoid pylint errors in vscode add a file `.env` to the root, containing `PYTHONPATH=./dataHandler`. ([why?](https://stackoverflow.com/questions/48973742/proper-relative-imports-unable-to-import-module))
