from flask import Flask, render_template, redirect, request
import datetime
from Neural_Style import new_style

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template("index.html")


@app.route("/", methods=["POST"])
def submit_data():
    if request.method == "POST":
        a = datetime.datetime.now()
        f = request.files["user_picture"]
        path = "./static/new_file".format(f.filename)
        f.save(path)
        #style = "./static/style_images/style4.jpg"
        
        style_name = request.form['user_style']
        print(style_name)
        style = "./static/style_images/" + style_name + ".jpg"

        if path:
            output = new_style.main(path, style)
            b = datetime.datetime.now()
            print(b-a)
            print(output)
            """
            result_dic = {
            'img' : f.filename,
            'text' : output
        }
        

        else:
            result_dic = {
            'img' : f.filename,
            'text' : "NO number plate detected"
            }
        """
    return render_template("index.html", your_text="Nice")


if __name__ == "__main__":
    app.run(debug=True)
