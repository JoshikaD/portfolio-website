from flask import Flask, render_template, request, redirect
import os
import psycopg2
app = Flask(__name__)
DATABASE_URL = os.getenv("DATABASE_URL")
conn =psycopg2.connect(DATABASE_URL)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Handle form submission
@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    cur = conn.cursor()
    cur.execute(
        "INSERT INTO contacts (name, email, message) VALUES (%s, %s, %s)",
        (name, email, message)
    )
    conn.commit()
    cur.close()

    return redirect("https://joshikad.github.io/portfolio-website/?success=true")

# Run server
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=10000)