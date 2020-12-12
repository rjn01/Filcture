
from flask import Flask, render_template, redirect, request
from Neural_Style import new_style

app =  Flask(__name__)

@app.route('/') 

def hello():  
    return render_template('index_new.html') 
    
@app.route('/', methods = ['POST']) 

def submit_data():
    if request.method== 'POST':
        f = request.files["user_picture"]  
        path = "./static/new_file".format(f.filename)
        f.save(path)
        
        if path:
            output = new_style.main(path,'./Desktop/New/Filcture/Neural-Style/default_style.jpg')
            '''print(output)
            result_dic = {
            'img' : f.filename,
            'text' : output
        }
        

        else:
            result_dic = {
            'img' : f.filename,
            'text' : "NO number plate detected"
            }
        '''
    return(render_template("index_new.html", your_text = "Nice"))
    

if __name__== "__main__":
    app.run(debug=True)
