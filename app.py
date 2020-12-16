from flask import Flask, render_template, redirect, request
import datetime
import time
from Neural_Style import new_style

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template("index.html")


@app.route("/", methods=["POST"])
def submit_data():
    if request.method == "POST":
        
        f = request.files["user_picture"]
        path = "./static/user_images/{}".format(f.filename)
        
        f.save(path)
        # style = "./static/style_images/style4.jpg"

        style_name = request.form["user_style"]
        
        style = "./static/style_images/" + style_name + ".jpg"

        
        if path:

            output_path = new_style.main(path, style)
            
            # time.sleep(10)
            output = {"filename": f.filename, "path": '.' + output_path}

        else:
            output = {"filename": f.filename, "path": "#"}

        
    return render_template("index.html", output=output)


if __name__ == "__main__":
    app.run(debug=True)
