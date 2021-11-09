from flask import *

app = Flask(__name__)

@app.route('/')
def message():
	return render_template('blog.html')

@app.route('/customer')  
def customer():  
   return render_template('customer.html')  

@app.route('/proceso.html')  
def proceso():  
    return render_template('proceso.html')  

@app.route('/tradicional.html')  
def tradicional():  
    return render_template('tradicional.html') 

  
@app.route('/success',methods = ['POST', 'GET'])  
def print_data():  
   if request.method == 'POST':  
      result = request.form  
      return render_template("result_data.html",result = result)


if __name__ == '__main__':
	app.run(debug = True) 
