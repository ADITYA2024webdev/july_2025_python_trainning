from flask import Flask, jsonify
from flask_mysqldb import MySQL
app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'roottoor'
app.config['MYSQL_DB'] = 'aditya_cse'

mysql = MySQL(app)


@app.route('/')
def hello_world():
    return 'Hello, aditya'

# @app.route('/007')
# def myname():
#     return 'My name is aditya'

@app.route('/myname/<name>')
def myname(name):
    return jsonify({"message":"hello","name":name})


@app.route('/getData')
def getData():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM user")
    result = cur.fetchall()
    cur.close()
    return jsonify(result)


if __name__ == '__main__':
    app.run()


