from flask import Flask , render_template, flash, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'amber'
app.config['MYSQL_DB'] = 'portfolio'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
# init MYSQL
mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('home.html')


@app.route('/my_work')
def mywork():
    return render_template('mywork.html')

@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':


    

        try:
            fname = request.form['fname']
            lname = request.form['lname']
         
            email = request.form['email']
            comment = request.form['comment']
            cur = mysql.connection.cursor()

            cur.execute("INSERT INTO details(fname,lname, email, comment) VALUES(%s,%s,%s,%s)",(fname,lname,email,comment))        
            mysql.connection.commit()

            # Close connection
            cur.close()
            flash('Your details are submitted, I will contact you soon, Thanks ', 'success')

            return redirect(url_for('index'))
        except Exception as e:
           return(str(e))
        
        return redirect(url_for('index'))
    return render_template('index.html')


if __name__ == '__main__':
    app.secret_key='secret123'
    app.run(debug=True)


    


  
   