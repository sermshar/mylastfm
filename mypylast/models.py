from sqlalchemy import Column, Integer, String
from base import Base

class Scrobble(Base):
    __tablename__ = 'scrobbles'

    id          = Column(Integer, primary_key=True)
    timestamp   = Column(Integer)
    track       = Column(String)
    album       = Column(String)
    artist      = Column(String)

    def __repr__(self):
        return "<Scrobble(timestamp='%s', track='%s', album='%s', 'artist='%s')>" % (
            self.timestamp, self.track, self.album, self.artist)
