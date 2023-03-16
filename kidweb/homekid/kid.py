from flask import Flask, render_template,flash
from form import ContactForm
from datetime import datetime as dt
from flask_mysqldb import MySQL


app = Flask(__name__)
app.secret_key = b'fjvhvusdbujvbsvdjxixfcghdmcbcfvjnjdbvjcfd'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'school_db'

mysql = MySQL(app)
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/courses")
def courses():
    return render_template('courses.html')

@app.route("/contact", methods=['GET','POST'])
def contact():
    form = ContactForm()
    
    if form.validate_on_submit():
        fname = form.fname.data
        lname = form.lname.data
        email = form.email.data
        subject = form.subject.data
        message = form.message.data
        
        now = dt.now()
        post_date = now.strftime("%d %b, %Y")
        flash(f'Application Sent !!', 'Success')
        print(post_date)
        
        cursor = mysql.connection.cursor()
        cursor.execute ('''INSERT INTO contact (fname, lname, email, subject, message, post_date)
        VALUES (%s, %s, %s, %s, %s, %s)''', (fname, lname, email, subject, message, post_date))
        mysql.connection.commit()
        cursor.close()
        
    return render_template("contact.html", form=form)


@app.route("/blog")
def blog():
    return render_template('blog.html')

@app.route("/singleblog")
def singleblog():
    return render_template('singleblog.html')

@app.route("/singlecourse")
def singlecourse():
    return render_template('singlecourse.html')


@app.route("/teacherprofile")
def teacherprofile():
    return render_template('teacherprofile.html')

@app.route("/teacher")
def teacher():
    return render_template('teacher.html')


if __name__ == "__main__":
    app.run(debug=True)