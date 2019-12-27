import pylast
from config import API_KEY, API_SECRET, USERNAME, DBFILE
from src.dataHandler.importer import update_db


NETWORK = pylast.LastFMNetwork(api_key=API_KEY, api_secret=API_SECRET, username=USERNAME)
update_db(DBFILE, NETWORK, USERNAME)
