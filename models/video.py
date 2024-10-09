from .. import db

class Video(db.Model):
    __tablename__ = 'videos'
    
    id = db.Column(db.Integer, primary_key=True)  # Video ID
    video_url = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f'<Video {self.id}: {self.video_url}>'
