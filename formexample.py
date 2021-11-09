from flask import Flask, render_template, request, flash  
from flask_wtf import Form  
from wtforms import TextField, IntegerField, TextAreaField, SubmitField, RadioField, SelectField  
from wtforms import validators, ValidationError  


app = Flask(__name__)  
app.secret_key = 'development key'

class ContactForm(Form):  
   name = TextField("Nombre del candidato ",[validators.Required("Por favor escribe tu nombre.")])  

   Gender = RadioField('Género', choices = [('M','Masculino'),('F','Femenino')])  

   Address = TextAreaField("Dirección")  
     
   email = TextField("Correo",[validators.Required("Please enter your email address."),  
   validators.Email("Por favor escribe tu correo.")])  
     
   Age = IntegerField("Edad")  
   
   language = SelectField('Lenguajes de programación', choices = [('java', 'Java'),('py', 'Python'),('VB', 'Visual Basic')])  
  
   submit = SubmitField("Enviar")  
 
  
@app.route('/contact', methods = ['GET', 'POST'])  
def contact():  
   form = ContactForm()  
   if form.validate() == False:  
      flash('All fields are required.')  
   return render_template('contact.html', form = form)  
  
  
  
@app.route('/success',methods = ['GET','POST'])  
def success():  
   return render_template("success.html")  
  
if __name__ == '__main__':  
   app.run(debug = True)  
