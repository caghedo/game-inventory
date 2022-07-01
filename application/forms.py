from flask_wtf import FlaskForm
from application import app
from wtforms import IntegerField, StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length
from os import getenv

app.config['SECRET_KEY'] = getenv('SECRET_KEY')

class PlayerCreateForm(FlaskForm):
    full_name = StringField('Full Name',validators=[DataRequired(), Length(min=2,max=30)])
    steam_id = StringField('Steam ID',validators=[DataRequired(), Length(min=2,max=30)])
    submit = SubmitField('Add Entry')

class PlayerUpdateForm(FlaskForm):
    id= IntegerField('Type ID here')
    steam_id= StringField('Type new Steam ID here',validators=[DataRequired(), Length(min=2,max=30)])
    submit = SubmitField('Change Entry')

class GameCreateForm(FlaskForm):
    name = StringField('Game Name',validators=[DataRequired(), Length(min=2,max=30)])
    size = StringField('Size in MB',validators=[DataRequired(), Length(min=1,max=10)])
    submit = SubmitField('Add Entry')

class GameUpdateForm(FlaskForm):
    id=IntegerField("Type ID here")
    size= IntegerField("Type new size in MB here",validators=[DataRequired(), Length(min=1,max=10)])
    submit= SubmitField("Change Entry")

class Player_GameCreateForm(FlaskForm):
    player_id=IntegerField("Type Player ID here",validators=[DataRequired(), Length(min=1,max=5)])
    game_id=IntegerField("Type Game ID here",validators=[DataRequired(), Length(min=1,max=5)])
    installed=BooleanField("Type installation status here")
    submit=SubmitField("Add Entry")

class Player_GameUpdateForm(FlaskForm):
    id=IntegerField("Type ID here")
    installed=BooleanField("Change installation status here")
    submit=SubmitField("Change Entry")

