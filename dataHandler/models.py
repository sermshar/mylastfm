from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
# https://stackoverflow.com/questions/39869793/when-do-i-need-to-use-sqlalchemy-back-populates


Base = declarative_base()

class Scrobble(Base):
    __tablename__ = 'scrobbles'

    id          = Column(Integer, primary_key=True)
    timestamp   = Column(Integer)
    track       = Column(String)
    album       = Column(String)
    artist      = Column(String)

    def __repr__(self):
        return f'<Scrobble(id="{self.id}", timestamp="{self.timestamp}", track="{self.track}", album="{self.album}", artist="{self.artist}")>'


class Track(Base):
    __tablename__ = 'tracks'
    
    id         = Column(Integer, primary_key=True)
    name       = Column(String)
    Album      = Column(Integer)
    
    def __repr(self):
        return f'<Track(id="{self.id}", name="{self.name}")>'


class Album(Base):
    __tablename__ = 'albums'
    
    id         = Column(Integer, primary_key=True)
    name       = Column(String)
    artist_id  = 
    artist     = 
    
    def __repr(self):
        return f'<Album(id="{self.id}", name="{self.name}")>'

    
class Artist(Base):
    __tablename__ = 'artists'
    
    id         = Column(Integer, primary_key=True)
    name       = Column(String)
    albums     = relationship("Album", back_populates="albums")
    
    def __repr(self):
        return f'<Artist(id="{self.id}", name="{self.name}")>'
    
    
