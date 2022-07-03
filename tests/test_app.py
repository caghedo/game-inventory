from application import app, db
from application.models import Player,Game,Player_Game
from flask import Flask, redirect, url_for, render_template, request
from application.forms import PlayerCreateForm,PlayerUpdateForm,GameCreateForm,GameUpdateForm,Player_GameCreateForm,Player_GameUpdateForm
from flask_testing import TestCase


class TestBase(TestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///",
                SECRET_KEY='TEST_SECRET_KEY',
                DEBUG=True,
                WTF_CSRF_ENABLED=False
                )
        return app
    
    def setUp(self):
        db.create_all()
        sample1 = Player(full_name="Mike Beaver",steam_id="FallsPD")
        game1=Game(name="TF2",size=15000)
        sample2= Player_Game(player_id=1, game_id=1, installed=True)
        db.session.add(sample1)
        db.session.add(game1)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()


class PlayerTestRead(TestBase):
    def test_view(self):
        response = self.client.get(url_for('playerview'))
        self.assertIn(b'Mike Beaver', response.data)

class PlayerTestCreate(TestBase):
    def test_create(self):
        response =self.client.post(url_for('playercreate'),data=dict(full_name="Chris Aghedo",steam_id='69'))
        self.assertIn(b'Chris Aghedo', response.data)
        '''form=PlayerCreateForm()
        form.full_name.data="Chris Aghedo"
        form.steam_id.data="Ayy"
        fullname=form.full_name.data
        steamname=form.steam_id.data
        player1=Player(full_name=fullname,steam_id=steamname)
        db.session.add(player1)
        db.session.commit()
        player=Player.query.get(2)
        self.assertEqual("Chris Aghedo",player.full_name)'''

class PlayerTestDelete(TestBase):
    def test_delete(self):
        response = self.client.get(
            url_for('playerdelete', id=1), follow_redirects=True
            #data= dict(full_name="Chris Aghedo",steam_id="Ayy")
        )
        self.assertEqual(response.status_code, 200)
#start    

class PlayerTestUpdate(TestBase):
    def test_update(self):
        response = self.client.post(url_for('playerupdate'),data=dict(id=1,steam_id="lol"))
        self.assertIn(b'lol',response.data)



class GameTestView(TestBase):
    def test_view(self):
        response = self.client.get(url_for('gameview'))
        self.assertIn(b'TF2', response.data)

class GameTestCreate(TestBase):
    def test_create(self):
        response =self.client.post(url_for('gamecreate'),data=dict(name="Modern Warfare",size=555))
        self.assertIn(b'Modern Warfare', response.data)


class GameTestDelete(TestBase):
    def test_delete(self):
        response = self.client.get(
        url_for('gamedelete', id=1), follow_redirects=True)
        self.assertEqual(response.status_code, 200)

class GameTestUpdate(TestBase):
    def test_update(self):
        response = self.client.post(url_for('gameupdate'),data=dict(id=1,size=6000))
        self.assertIn(b'6000',response.data)

class Player_GameTestView(TestBase):
    def test_player_game_view(self):
        response=self.client.get(url_for('player_gameview'))
        sample2= Player_Game(player_id=1, game_id=2, installed=True)
        db.session.add(sample2)
        db.session.commit()
        self.assertEqual(response.status_code, 200)

class Player_GameTestCreate(TestBase):
    def test_player_game_create(self):
        response=self.client.post(url_for('player_gamecreate'),data=dict(player_id=1,game_id=1,installed=False))
        self.assertIn(b'False',response.data)

class Player_GameTestUpdate(TestBase):
    def test_player_game_update(self):
        response=self.client.put(url_for('player_gameupdate'),data=dict(id=1, installed=False))
        self.assertIn(b'1', response.data)

#90% of tests done anyway, CRUD works