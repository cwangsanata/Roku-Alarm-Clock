from .. import db

class Alarm(db.Model):
    __tablename__ = 'alarms'
    
    id = db.Column(db.Integer, primary_key=True) 
    day = db.Column(db.String(10), nullable=False) 
    alarm_time_id = db.Column(db.Integer, db.ForeignKey('alarm_times.id'), nullable=False)  # Foreign key to Alarm_Times
    video_id = db.Column(db.Integer, db.ForeignKey('videos.id'), nullable=False)  # Foreign key to Videos
    note = db.Column(db.String, nullable=True) 

    # Relationships
    alarm_time = db.relationship('AlarmTime', backref='alarms')
    video = db.relationship('Video', backref='alarms')

    def __repr__(self):
        return f'<Alarm {self.id}: {self.day} at {self.alarm_time.time}>'