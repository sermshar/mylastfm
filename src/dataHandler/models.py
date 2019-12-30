from sqlalchemy import Column, Integer, String, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class RawScrobble(Base):
    __tablename__ = "raw_scrobbles"

    id = Column(Integer, primary_key=True)
    timestamp = Column(Integer)
    track = Column(String)
    album = Column(String)
    artist = Column(String)

    def __repr__(self):
        return "<RawScrobble(timestamp='%s', track='%s', album='%s', 'artist='%s')>" % (
            self.timestamp, self.track, self.album, self.artist)


class Track(Base):
    __tablename__ = "rename_tracks"

    id = Column(Integer, primary_key=True)
    timestamp = Column(Integer)
    track = Column(String)
    album = Column(String)
    artist = Column(String)
    isrc = Column(String)

    def __repr__(self):
        return "<Track(timestamp='%s', track='%s', album='%s', 'artist='%s')>" % (
            self.timestamp, self.track, self.album, self.artist)


class RewriteRule(Base):
    __tablename__ = "rewrite_rules"

    id = Column(Integer, primary_key=True)
    raw_id = Column(Integer)
    raw_timestamp = Column(Integer)
    raw_track = Column(String)
    raw_album = Column(String)
    raw_artist = Column(String)
    rename_track_id = Column(Integer)

    # https://stackoverflow.com/a/10061143
    __table_args__ = (UniqueConstraint(
        'raw_id',
        'raw_timestamp',
        'raw_track',
        'raw_album',
        'raw_artist',
        name='raw_scrobble_uc'),
    )


class TrackArtist(Base):
    __tablename__ = "tracks_artists"

    id = Column(Integer, primary_key=True)
    track_id = Column(Integer)
    artist_id = Column(Integer)
    order = Column(Integer)
