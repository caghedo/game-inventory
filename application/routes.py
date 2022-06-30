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
    
            '''if len(fullname) == 0 or len(steamname) == 0:
                message = "Please supply both full name and steam name"
            else:
                message = f'Thank you, {fullname}'''
            
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
    player_game=Player_Game.query.all()
    for y in player_game:
        if y.player_id==player.id:
            redirect(url_for('player_gamedelete',id=y.id))
    db.session.delete(player)
    db.session.commit()
    return redirect(url_for('playerview'))






@app.route('/gameview')
def gameview():
    game=Game.query.all()
    return render_template('gameview.html',game=game)

@app.route('/gamecreate', methods=['GET','POST'])
def gamecreate():
    message=""
    form=GameCreateForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            name=form.name.data
            size=form.size.data
    
            if len(name)== 0:
                message = "Please supply the game's name"
            
            game1=Game(  
            name = name,
            size = size)

            db.session.add(game1)
            db.session.commit()
    return render_template('gamecreate.html',form=form,message=message)

@app.route('/gameupdate', methods=['GET','POST'])
def gameupdate():
    form=GameUpdateForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            game=Game.query.get(form.id.data)
            game.size=form.size.data
            db.session.commit()
    return render_template('gameupdate.html',form=form)

@app.route('/gamedelete/<int:id>')
def gamedelete(id):
    game=Game.query.get(id)
    db.session.delete(game)
    player_game=Player_Game.query.all()
    for x in player_game:
        if x.game_id==game.id:
            db.session.delete(x)
    db.session.commit()
    return redirect(url_for('gameview'))





@app.route('/player_gameview')
def player_gameview():
    player_game=Player_Game.query.all()
    return render_template('player_gameview.html',player_game=player_game)

@app.route('/player_gamecreate', methods=['GET','POST'])
def player_gamecreate():
    message=""
    form=Player_GameCreateForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            playerid=form.player_id.data
            gameid=form.game_id.data
            installed=form.installed.data
    
           
            
            player_game1=Player_Game(  
            player_id=playerid,
            game_id=gameid, installed=installed)

            db.session.add(player_game1)
            db.session.commit()
    return render_template('player_gamecreate.html',form=form,message=message)

@app.route('/player_gameupdate', methods=['GET','POST'])
def player_gameupdate():
    form=Player_GameUpdateForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            player_game=Player_Game.query.get(form.id.data)
            player_game.installed=form.installed.data
            db.session.commit()
    return render_template('player_gameupdate.html',form=form)

@app.route('/player_gamedelete/<int:id>')
def player_gamedelete(id):
    player_game=Player_Game.query.get(id)
    db.session.delete(player_game)
    db.session.commit()
    return redirect(url_for('player_gameview'))



