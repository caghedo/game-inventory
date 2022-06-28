from application import db
from application.models import Player,Game,Player_Game

db.drop_all()
db.create_all()