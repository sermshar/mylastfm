# mylastfm

This is a git repository for keeping track of my last.fm data and code for retrieval and analysis.

Goals:
- [ ] separate tables for scrobbles, artists, tags, etc.
- [ ] interface for updating database automatically
- [ ] keep track of last update time for info-resources like tags, wikis etc.
- [ ] generic functions for graphing data
- [ ] Jupyter notebook that can import machinery for graphing data and querying and updating the database
- [ ] progressbar/indicator for long database imports (might not be possible with pylast)


---


## setup

### environment

Uses `Python 3.7.0`.

I used `virtualenv` and `pyenv`. To avoid pylint errors in vscode add a file `.env` to the root, containing `PYTHONPATH=./dataHandler`. ([more info](https://stackoverflow.com/questions/48973742/proper-relative-imports-unable-to-import-module))

Activate the ipython widgets extension by running 
`jupyter nbextension enable --py widgetsnbextension` and
`jupyter labextension install @jupyter-widgets/jupyterlab-manager`
in the root. ([more info](https://ipywidgets.readthedocs.io/en/latest/user_install.html#installing-the-jupyterlab-extension))


### the last.fm configuration file

Create a configuration file containing the following.

```python
import pylast

API_KEY = # YOUR API KEY
API_SECRET = # YOUR SECRET KEY
USERNAME = # YOUR USERNAME

NETWORK = pylast.LastFMNetwork(api_key=API_KEY, api_secret=API_SECRET, username=USERNAME)

DBFILE = # YOUR SQLITE DATABASE PATH (FROM ROOT)
```

import `USERNAME` and `NETWORK` for use in `updateDB()`.




