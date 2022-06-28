from flask_wtf import FlaskForm
from application import app
from wtforms import IntegerField, StringField, SubmitField, BooleanField

app.config['SECRET_KEY'] = 'YOUR_SECRET_KEY'

class PlayerCreateForm(FlaskForm):
    full_name = StringField('Full Name')
    steam_id = StringField('Steam ID')
    submit = SubmitField('Add Entry')

class PlayerUpdateForm(FlaskForm):
    id= IntegerField('Type ID here')
    steam_id=StringField('Type new Steam ID here')
    submit = SubmitField('Change Entry')

class GameCreateForm(FlaskForm):
    name = StringField('Game Name')
    size = StringField('Size in MB')
    submit = SubmitField('Add Entry')

class GameUpdateForm(FlaskForm):
    id=IntegerField("Type ID here")
    size= IntegerField("Type new size in MB here")
    sumbit=SubmitField("Change Entry")

class Player_GameCreateForm(FlaskForm):
    player_id=IntegerField("Type Player ID here")
    game_id=IntegerField("Type Game ID here")
    installed=BooleanField("Type installation status here")
    submit=SubmitField("Add Entry")

class Player_GameUpdateForm(FlaskForm):
    id=IntegerField("Type ID here")
    installed=BooleanField("Change installation status here")
    submit=SubmitField("Change Entry")

