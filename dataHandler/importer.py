from    dataHandler.models  import Base, Scrobble
from    sqlalchemy          import create_engine
from    sqlalchemy.orm      import sessionmaker
from    sqlalchemy.sql      import func

def updateDB(db_file, fm_network, fm_username):
    """
    Connect to or create the database, get recent tracks not already in the database and add them to it
    """
    engine = create_engine(('sqlite:///' + db_file), echo=False)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    from_timestamp = __last_timestamp(session) + 1
    recent_scrobbles = __get_scrobbles(from_timestamp, fm_network, fm_username)
    session.bulk_save_objects(recent_scrobbles)

    session.commit()
    session.close()


def __get_scrobbles(from_timestamp, fm_network, fm_username):
    """
    Get all scrobbles from last.fm starting from the last one in the database.
    If getAll is true, retrieve all scrobbles, 
    reseting the database to match last.fm (may take a few minutes).
    returns an array of Scrobble objects
    """
    lfm_user = fm_network.get_user(fm_username)
    cacheable = True if (from_timestamp == None) else False
    scrobbles = lfm_user.get_recent_tracks(
        limit=None, cacheable=cacheable, time_from=from_timestamp, time_to=None
        )
    return __format_scrobble_array(scrobbles=scrobbles)
    

def __format_scrobble_array(scrobbles):
    """
    Convert the python list of scrobbles from pylast to a single dimensional array
    of Scrobble objects that can be mapped to the scrobble database.
    """
    scrobble_array = []
    for row in scrobbles:
        timestamp = row.timestamp.__str__()
        track = row.track.get_title().__str__()
        album = row.album.__str__()
        artist = row.track.get_artist().__str__()
        scrobble = Scrobble(timestamp=timestamp, track=track, album=album, artist=artist)
        scrobble_array.append(scrobble)
    return scrobble_array


def __last_timestamp(session):
    """return the greatest (most recent) timestamp in the scrobble library"""
    return session.query(func.max(Scrobble.timestamp.label('max_timestamp'))).one()[0]
