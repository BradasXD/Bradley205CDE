from flask import Flask, make_response, abort, redirect, render_template

app = Flask(__name__);

@app.route('/')
def index():
    return render_template("Homepage.html")
    
@app.route('/8BallPool')
def eightball():
    return render_template("8BallPool.html")
    
@app.route('/About')
def About():
    return render_template("About.html")
    
@app.route('/AcidFactory')
def AcidFactory():
    return render_template("AcidFactory.html")
    
@app.route('/Action')
def Action():
    return render_template("Action.html")
    
@app.route('/Adventure')
def Adventure():
    return render_template("Adventure.html")
    
@app.route('/Agar.io')
def Agar_io():
    return render_template("Agar.io.html")
    
@app.route('/Boxo')
def Boxo():
    return render_template("Boxo.html")
    
@app.route('/CalabashBros')
def CalabashBros():
    return render_template("CalabashBros.html")
    
@app.route('/CandynClyde')
def CandynClyde():
    return render_template("CandynClyde.html")    
    
@app.route('/Commando')
def Commando():
    return render_template("Commando.html")
    
@app.route('/CommandoDefence')
def CommandoDefence():
    return render_template("CommandoDefence.html")
    
@app.route('/Contact')
def Contact():
    return render_template("Contact.html")
    
@app.route('/CubeBuster')
def CubeBuster():
    return render_template("CubeBuster.html")
    
@app.route('/EgyptianTale')
def EgyptianTale():
    return render_template("EgyptianTale.html")

@app.route('/Fragger')
def Fragger():
    return render_template("Fragger.html")

@app.route('/Mimelet')
def Mimelet():
    return render_template("Mimelet.html")

@app.route('/MinecartMadness')
def MinecartMadness():
    return render_template("MinecartMadness.html")

@app.route('/Puzzle')
def Puzzle():
    return render_template("Puzzle.html")

@app.route('/Shooter')
def Shooter():
    return render_template("Shooter.html")

@app.route('/SkywardNinja')
def SkywardNinja():
    return render_template("SkywardNinja.html")

@app.route('/StealthSniper')
def StealthSniper():
    return render_template("StealthSniper.html")

@app.route('/SushiGoRound')
def SushiGoRound():
    return render_template("SushiGoRound.html")

@app.route('/SwingCopter')
def SwingCopter():
    return render_template("SwingCopter.html")

@app.route('/TotalWreckage')
def TotalWreckage():
    return render_template("TotalWreckage.html")
    
@app.route('/Zombality')
def Zombality():
    return render_template("Zombality.html")
    
if __name__ == '__main__':
    app.run(port=8080, host='0.0.0.0', debug=True)