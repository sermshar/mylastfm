from pylast_config import NETWORK, USERNAME
from models import Scrobble
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

lfm_user = NETWORK.get_user(USERNAME)

engine = create_engine('sqlite:///mylastfm.sqlite3', echo=True)
Session = sessionmaker(bind=engine)
session = Session()

def updateDB(parameter_list):
    pass
