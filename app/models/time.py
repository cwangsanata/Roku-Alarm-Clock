from .. import db

class AlarmTime(db.Model):
    __tablename__ = 'alarm_times'
    
    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.Time, nullable=False)

    def __repr__(self):
        return f'<AlarmTime {self.id}: {self.time}>'