# mylastfm

This is a git repository for keeping track of my last.fm data and code for retrieval and analysis.
It was originally for use with Jupyter notebooks, but I'm in the process of rewriting parts of it to be a CLI that will 
allow me to quickly update my local database, add renaming rules, and run common queries. There will be much less
focus on generating diagrams from the data.

## setup

### the last.fm configuration file

Copy the `config-example.py` file to `config.py` in the project root and replace the placeholder text. 

### the first run

Run `python update-script.py` from the project root to download all your scrobbles into the database, this may take a while the first time if your library is large.
