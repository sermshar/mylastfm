import pylast
from config import API_KEY, API_SECRET, USERNAME
import code

NETWORK = pylast.LastFMNetwork(api_key=API_KEY, api_secret=API_SECRET, username=USERNAME)

# https://stackoverflow.com/a/2158266
code.interact(local=locals())
