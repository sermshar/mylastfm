# mylastfm

This is a git repository for keeping track of my last.fm data and code for retrieval and analysis.

Goals:
- [ ] separate tables for scrobbles, artists, tags, etc.
- [ ] keep track of last update time for info-resources like tags, wikis etc.
- [ ] generic functions for graphing data

---

## setup

Python version 3.7.0

Add a file `mypylast/pylast_config.py` containing: 

```python
import pylast

API_KEY = # YOUR API KEY
API_SECRET = # YOUR SECRET KEY
USERNAME = # YOUR USERNAME

NETWORK = pylast.LastFMNetwork(api_key=API_KEY, api_secret=API_SECRET, username=USERNAME)
```
