from flask import Flask, render_template
app = Flask(__name__)

@app.route('/<x>/<y>')
def check (x,y):
    return render_template("checkerboard.html", num = int(x), num1 = int(y))

if __name__=="__main__":
    app.run(debug = True)