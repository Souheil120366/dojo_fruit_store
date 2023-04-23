from flask import Flask, render_template, request, redirect, session
app = Flask(__name__) 
app.secret_key = 'keep it secret, keep it safe' 

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form['apple'])
    session['firstname']=request.form['first_name']
    session['lastname']=request.form['last_name']
    session['studentid']=request.form['student_id']
    session['strawberry']=request.form['strawberry']
    session['raspberry']=request.form['raspberry']
    session['apple']=request.form['apple']
    return redirect("/show")
    

@app.route("/show")
def show_user():
    print("Showing the User Info From the Form")
    print(request.form)
    # return render_template("show.html")
    return render_template("checkout.html",
                           firstname=session['firstname'],
                           lastname=session['lastname'],
                           studentid=session['studentid'],
                           strawberry=session['strawberry'],
                           raspberry=session['raspberry'],
                           apple=session['apple'], 
                           count=str(int(session['strawberry'])+int(session['raspberry'])+int(session['apple'])))

    
@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    