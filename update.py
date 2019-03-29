from config import NETWORK, USERNAME, DBFILE
from dataHandler.importer import updateDB

updateDB(DBFILE, NETWORK, USERNAME)