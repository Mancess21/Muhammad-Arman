from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app=Flask(__name__)
app.config['SECRET_KEY'] = "andrian"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Data_Demog.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager= LoginManager(app)

from sim.admin.routes import Sadmin
app.register_blueprint(Sadmin)


from sim.penduduk.routes import Suser
app.register_blueprint(Suser)
