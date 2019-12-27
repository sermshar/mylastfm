from src.dataHandler.models import Base, RawScrobble
from sqlalchemy import create_engine, exc
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func
from contextlib import contextmanager


def update_db(db_file, fm_network, fm_username):
    """
    Connect to or create the database, get recent tracks not already in the database and add them to it
    """
    with small_session(db_file) as session:
        last_raw_timestamp = __last_raw_timestamp(session)
        from_timestamp = __last_raw_timestamp(session) + 1 if (last_raw_timestamp is not None) else None
        recent_scrobbles = __get_raw_scrobbles(from_timestamp, fm_network, fm_username)
        session.bulk_save_objects(recent_scrobbles)


@contextmanager
def small_session(db_file):
    # https://docs.python.org/2.5/whatsnew/pep-343.html#module-contextlib
    engine = create_engine(("sqlite:///" + db_file), echo=False)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        yield session
        session.commit()
    except exc.SQLAlchemyError as error:
        session.rollback()
        print("Encountered an SQLAlchemy Error, the session has been rolled back.")
    finally:
        session.close()


def __get_raw_scrobbles(from_timestamp, fm_network, fm_username):
    """
    Get all scrobbles from last.fm starting from the last one in the database,
    or all scrobbles if the database is empty (this may take a few minutes).
    returns an array of Scrobble objects
    """
    lfm_user = fm_network.get_user(fm_username)
    cacheable = True if (from_timestamp is None) else False
    raw_scrobbles = lfm_user.get_recent_tracks(
        limit=None, cacheable=cacheable, time_from=from_timestamp, time_to=None
    )
    return __format_raw_scrobble_array(raw_scrobbles=raw_scrobbles)


def __format_raw_scrobble_array(raw_scrobbles):
    """
    Convert the python list of scrobbles from pylast to a single dimensional array
    of RawScrobble objects that can be mapped to the scrobble database.
    Note that the timestamp is a unix timestamp (seconds since 1970-01-01 UTC)
    """
    scrobble_array = []
    for row in raw_scrobbles:
        timestamp = row.timestamp.__str__()
        track = row.track.get_title().__str__()
        album = row.album.__str__()
        artist = row.track.get_artist().__str__()
        raw_scrobble = RawScrobble(
            timestamp=timestamp, track=track, album=album, artist=artist
        )
        scrobble_array.append(raw_scrobble)
    return scrobble_array


def __last_raw_timestamp(session):
    """return the greatest (most recent) timestamp in the RawScrobble table"""
    return session.query(func.max(RawScrobble.timestamp.label("max_timestamp"))).one()[0]
