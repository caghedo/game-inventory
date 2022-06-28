from application import app, db
from application.models import Player,Game,Player_Game
from flask import Flask, redirect, url_for, render_template, request
from application.forms import PlayerCreateForm,PlayerUpdateForm,GameCreateForm,GameUpdateForm,Player_GameCreateForm,Player_GameUpdateForm


@app.route('/home')
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/playerview')
def playerview():
    player=Player.query.all()
    return render_template('playerview.html',player=player)

@app.route('/playercreate', methods=['GET','POST'])
def playercreate():
    message=""
    form=PlayerCreateForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            fullname=form.full_name.data
            steamname=form.steam_id.data
    
            if len(fullname) == 0 or len(steamname) == 0:
                message = "Please supply both full name and steam name"
            else:
                message = f'Thank you, {fullname}'
            
            player1=Player(  
            full_name = fullname,
            steam_id = steamname)

            db.session.add(player1)
            db.session.commit()
    return render_template('playercreate.html',form=form,message=message)

@app.route('/playerupdate', methods=['GET','POST'])
def playerupdate():
    form=PlayerUpdateForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            player=Player.query.get(form.id.data)
            player.steam_id=form.steam_id.data
            db.session.commit()
    return render_template('playerupdate.html',form=form)

@app.route('/playerdelete/<int:id>')
def playerdelete(id):
    player=Player.query.get(id)
    db.session.delete(player)
    db.session.commit()
    return redirect(url_for('playerview'))





