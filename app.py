from flask import Flask, jsonify,request,render_template
from flask_mysqldb import MySQL
app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'roottoor'
app.config['MYSQL_DB'] = 'aditya_cse'

mysql = MySQL(app)

# # ---------------------------------------------------------------
# @app.route('/')
# def hello_world():
#     return 'Hello, aditya'

# @app.route('/007')
# def myname():
#     return 'My name is aditya'

# @app.route('/myname/<name>')
# def myname(name):
#     return jsonify({"message":"hello","name":name})

# # --------------------------------------------------------------
# @app.route('/getData')
# def getData():
#     id = request.args.get("id")
    
#     if id:
#         sql = f"SELECT * FROM user WHERE id = {id}"
#     else:
#         sql = "SELECT * FROM user"
    
#     cur = mysql.connection.cursor()
#     cur.execute(sql)
#     result = cur.fetchall()
#     cur.close()

#     return jsonify(result)

# # ---------------------------------------------------------------    

# @app.route('/myhtml', methods=['get', 'post'])
# def myHtml():
#     if request.method == 'POST':
#         name=request.form.get("name")
#         city=request.form.get("city")
#         address= request.form.get("address")
#         return f'{name}, {city} {address}'
#     else:
#         return render_template('home.html')

# # ---------------------------------------------------------------

# @app.route('/register_save',methods=["post"])
# def register_save():
#     email =request.form.get("email")
#     password =request.form.get("password")
#     return f" Email: {email}, Password: {password}"


# # -----------------------------------------------------------------

# @app.route('/mydetails',methods=["get","post"])
# def mydetails():
#     name=request.args.get("name")
#     city=request.args.get("city")
#     address= request.args.get("address")
    
#     return f"{name} is from {city} and lives in {address}"

# # ------------------------------------------------------------------

@app.route('/register_save', methods=['get', 'post'])
def register_save():
    if request.method == 'POST':
        id = request.form.get("id")
        name= request.form.get("name")
        password = request.form['password']
        email= request.form['email']
        phoneno= request.form['phoneno']
        cur = mysql.connection.cursor()
        sql = "INSERT INTO user (id, name, password, phoneno, email) VALUES (%s, %s, %s, %s, %s)"
        val = (id ,name,password,phoneno,email)
        cur.execute(sql, val)
        mysql.connection.commit()
        cur.close()
        return "register success"
    else:
        return render_template('home.html')

# ---------------------------------------------------------------
@app.route('/getdatahtml')
def getdatahtml():
    id = request.args.get("id")
    
    if id:
        sql = f"SELECT * FROM user WHERE id = {id}"
    else:
        sql = "SELECT * FROM user"
    
    cur = mysql.connection.cursor()
    cur.execute(sql)
    result = cur.fetchall()
    cur.close()

    return render_template("userlist.html",userlist=result)
# -----------------------------------------------------------------
@app.route('/userdetails')
def userdetails():
    id = request.args.get("id")
    sql=f"select*from user where id={id}"
    cur = mysql.connection.cursor()
    cur.execute(sql)
    results = cur.fetchall()
    cur.close()
    # id="9"
    # name="bot9"
    # email="test8@gmail.com"
    # password="878787"
    return render_template("user_details.html",id=results[0][0] ,name=results[0][1],email=results[0][2],password=results[0][3] )

if __name__ == '__main__':
    app.run()


