from application import db


class Player(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    full_name=db.Column(db.String(30),nullable=False)
    steam_id=db.Column(db.String(30), nullable=False)
    Player_game = db.relationship('Player_Game', backref='playerbr')

class Game(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(50), nullable=False)
    size=db.Column(db.Integer, nullable=False)
    Player_game = db.relationship('Player_Game', backref='gamebr')

    

class Player_Game(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    player_id=db.Column(db.Integer, db.ForeignKey("player.id"))
    game_id=db.Column(db.Integer, db.ForeignKey("game.id")) 
    installed=db.Column(db.Boolean, nullable=False)


    