import sqlite3
from flask import Flask, request

app = Flask(__name__)
conn = sqlite3.connect('test.db')
cursor = conn.cursor()

@app.route('/user')
def get_user():
    user_id = request.args.get('id')
    #Vulnerable to SQL injection
    query = "SELECT * FROM users WHERE id = " + user_id
    cursor.execute(query)
    return str(cursor.fetchall())

if __name__ == "__main__":
    app.run(debug=True)