from stocks.api import app, db
import uuid
from datetime import datetime

#Adding Flask Security for Passwords
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    id = db.Column(db.String, primary_key = True)
    first_name = db.Column(db.String(150), nullable = True, default = '')
    last_name = db.Column(db.String(150), nullable = True, default = '')
    email = db.Column(db.String(150), nullable = False)
    password = db.Column(db.String, nullable = True, default = '')
    g_auth_verify = db.Column(db.Boolean, default = False)
    token = db.Column(db.String, default = '', unique=True)
    date_created = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
    data_set = db.relationship('Dataset', backref = 'owner', lazy = True)

    def __init__(self,email,first_name = '', last_name = '', id = '', password = ''):
        self.id = self.set_id()
        self.first_name = first_name
        self.last_name = last_name
        self.password = self.set_password(password)
        self.email = email

    def set_id(self):
        return str(uuid.uuid4())

    def set_password(self, password):
        self.pw_hash = generate_password_hash(password)
        return self.pw_hash
    
    def __repr__(self):
        return f'User {self.email} has been added to the database'
    
class StockDataSet(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    ticker = db.Column(db.String(150))
    period_type = db.Column(db.Integer)
    period = db.Column(db.String(150))
    frequency_type = db.Column(db.String(150))
    frequency = db.Column(db.String(150))
    end_date = db.Column(db.DateTime)
    start_date = db.Column(db.DateTime)
    user_id = db.Column(db.String, db.ForeignKey('user.token'), nullable = False)

    def __init__(self,ticker,period_type,period,user_id):
        self.ticker = ticker
        self.period_type = period_type
        self.period = period
        self.user_id = user_id

    def __repr__(self):
        return f'The following Drone has been added: {self.ticker} which belongs to {self.user_id}'

    def to_dict(self):
        return {
            "id": self.id,
            "ticker": self.ticker,
            "period_type": self.period_type,
            "period": self.period
        }