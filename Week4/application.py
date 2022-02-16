from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("hello.html")
    
    
@app.route("/getDetails",methods=["GET","POST"])
def get_Details():
    if request.method=="GET":
        return render_template("get_Details.html")
    elif request.method=="POST":
        userName = request.form["name"]
        return render_template("show_Details.html",display_name=userName)

    
if __name__ == '__main__':
    app.debug=True
    app.run()