from flask import Flask
from test1_blueprint import test1_blueprint

app = Flask(__name__)
app.register_blueprint(test1_blueprint)

user_names = ['SupaMan716','MarioLover999','CrazyDave7','MikeTheMonster444','JohnnyBeWild','Qwerty123','SickDude41','EdgyEdge5','MilkingCow45','CursedMan893','HotDogWoman443','JesusChrist777']

@app.route('/page1')
def first_page():
    return '##Welcome to the ＰＡＧＥ##'

@app.route('/page2')
def second_page(name="User that I don't know"):
    return '##Hello ' + name + '##'

@app.route('/page3')
def third_page(wallet=0):
    return '##You currently have $' + str(wallet) + ' in your wallet##'