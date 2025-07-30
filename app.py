
from flask import Flask, render_template, request, redirect
import mysql.connector

# ✅ Define app before any @app.route
app = Flask(__name__)

# ✅ MySQL connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="roottoor",  # Replace if needed
    database="demo"
)

# ✅ Routes
@app.route('/')
def index():
    return render_template('home.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        user_id = request.form['id']
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        cursor = db.cursor()
        query = "INSERT INTO user (id, name, email, password) VALUES (%s, %s, %s, %s)"
        values = (user_id, name, email, password)
        cursor.execute(query, values)
        db.commit()
        cursor.close()

        return redirect('/')

# ✅ Run the app
if __name__ == '__main__':
    app.run(debug=True)
