from flask import Flask, render_template, request, redirect, url_for, session

import ibm_db
conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=ea286ace-86c7-4d5b-8580-3fbfa46b1c66.bs2io90l08kqb1od8lcg.databases.appdomain.cloud;PORT=31505;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=dgh01493;PWD=UAXBE3o4f8HclRKP",'','')
print(conn)
print("success")


app = Flask(__name__,template_folder='template') 
@app.route('/')
def home():
    return render_template('register.html')


@app.route('/register',methods = ['POST', 'GET'])
def register():
  msg=''
  if request.method == 'POST':

    username = request.form['name']
    email = request.form['username']
    password = request.form['password']

    sql = "SELECT * FROM REGISTER WHERE EMAIL =?"
    stmt = ibm_db.prepare(conn, sql)
    ibm_db.bind_param(stmt,1,email)
    ibm_db.execute(stmt)
    account = ibm_db.fetch_assoc(stmt)

    if account:
        msg="You are already a member, please login using your details"
        return render_template('login.html', msg = msg) 
    else:
        insert_sql = "INSERT INTO REGISTER (USERNAME, EMAIL, PASSWORD)  VALUES (?,?,?)"
        prep_stmt = ibm_db.prepare(conn, insert_sql)
        ibm_db.bind_param(prep_stmt, 1, username)
        ibm_db.bind_param(prep_stmt, 2, email)
        ibm_db.bind_param(prep_stmt, 3, password)
        ibm_db.execute(prep_stmt)
        return render_template("index.html")


@app.route('/login',methods=['post','get'])

def index():

    insert_sql = "INSERT INTO LOGIN (EMAIL, PASSWORD)  VALUES (?,?)"
    prep_stmt = ibm_db.prepare(conn, insert_sql)
    email = request.form['username']
    password= request.form['password']
    
    
    ibm_db.bind_param(prep_stmt, 1, email)
    ibm_db.bind_param(prep_stmt, 2, password)
    
    ibm_db.execute(prep_stmt)
    return render_template("index.html")

@app.route('/admin',methods=['post','get'])

def admin():

    insert_sql = "INSERT INTO ADMIN (EMAIL, PASSWORD)  VALUES (?,?)"
    prep_stmt = ibm_db.prepare(conn, insert_sql)
    email = request.form['username']
    password= request.form['password']
    
    
    ibm_db.bind_param(prep_stmt, 1, email)
    ibm_db.bind_param(prep_stmt, 2, password)
    
    ibm_db.execute(prep_stmt)
    return render_template("index.html")


@app.route('/adminlog')
def adminlog():
    return render_template("admin.html")


@app.route('/move')
def move():
    return render_template("login.html")

@app.route('/Home')
def Home():
    return render_template("index.html")

@app.route('/About')
def About():
    return render_template("About.html")

@app.route('/Course')
def Course():
    return render_template("Course.html")

@app.route('/Blog')
def Blog():
    return render_template("Blog.html")

@app.route('/feedback',methods=['post','get'])
def feedback():
    insert_sql = "INSERT INTO FEEDBACK (NAME, EMAIL, MOBILE, PRODUCT, FEEDBACK)  VALUES (?,?,?,?,?)"
    prep_stmt = ibm_db.prepare(conn, insert_sql)
    name = request.form['name']
    email = request.form['email']
    mobile = request.form['mobile']
    product= request.form['product']
    feedback = request.form['feedback']
    
    ibm_db.bind_param(prep_stmt, 1, name)
    ibm_db.bind_param(prep_stmt, 2, email)
    ibm_db.bind_param(prep_stmt, 3, mobile)
    ibm_db.bind_param(prep_stmt, 4, product)
    ibm_db.bind_param(prep_stmt, 5, feedback)
    
    ibm_db.execute(prep_stmt)    
    return render_template("Blog.html")

@app.route('/contact',methods=['post','get'])
def contact():
    insert_sql = "INSERT INTO CONTACT (NAME, EMAIL, SUBJECT, MESSAGE)  VALUES (?,?,?,?)"
    prep_stmt = ibm_db.prepare(conn, insert_sql)
    name = request.form['name']
    email = request.form['email']
    subject = request.form['subject']
    message= request.form['message']
    
    ibm_db.bind_param(prep_stmt, 1, name)
    ibm_db.bind_param(prep_stmt, 2, email)
    ibm_db.bind_param(prep_stmt, 3, subject)
    ibm_db.bind_param(prep_stmt, 4, message)
    
    ibm_db.execute(prep_stmt)    
    return render_template("Contact.html")

@app.route('/Contact')
def Contact():
    return render_template("Contact.html")


@app.route('/shop')
def shop():
    return render_template("shop.html")



if __name__ == '__main__':
    app.run(debug=True)
