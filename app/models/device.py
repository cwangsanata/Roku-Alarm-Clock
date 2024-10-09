from .. import db

class Device(db.Model):
    __tablename__ = 'devices'
    
    id = db.Column(db.Integer, primary_key=True) 
    ip = db.Column(db.String(15), nullable=False)
    port = db.Column(db.Integer, nullable=False)
    timeout = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Device('{self.ip}', '{self.port}', '{self.timeout}')"
    