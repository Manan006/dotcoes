from flask import Flask,render_template,redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',)

@app.route('/r/<target>')
def redirect_target(target:str):
    targets={
        "spotify":"https://open.spotify.com/user/bmld3ba3xyyhss6nnl1fsw9q5",
        "steam":"https://steamcommunity.com/id/mananboi006/",
        "hireme":"/contact",
        "github:":"https://github.com/Manan006/"
    }
    url=targets.get(target.lower())
    if url!=None:
        return redirect(url)
    else:
        return "a"
if __name__=="__main__":
    app.run(debug=False,port=8080)

