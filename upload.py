from flask import *  
app = Flask(__name__)  
 
@app.route('/')  
def upload():  
    return render_template("file_upload_form.html")  
 
@app.route('/success', methods = ['POST'])  
def success():  
    if request.method == 'POST':  
        f = request.files['file']  
        f.save('static/images/' + f.filename)
        return render_template("success1.html", name = f.filename)



@app.route('/enlaces')
def enlaces():
    enlaces=[{"url":"http://www.google.es","texto":"Google"},
            {"url":"http://www.twitter.com","texto":"Twitter"},
            {"url":"http://www.facebook.com","texto":"Facebook"},
            {"url":"http://www.youtube.com","texto":"youtube"}]
    return render_template("enlace.html",enlaces=enlaces)


if __name__ == '__main__':  
    app.run(debug = True)  
