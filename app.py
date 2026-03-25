from flask import Flask, render_template, request, redirect
import psycopg2

app = Flask(__name__)

# Connect to PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    database="portfolio",
    user="postgres",
    password="Jo16sh11ika@",  # change this
    port="5432"
)

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

    return redirect('/')

# Run server
if __name__ == '__main__':
    app.run(debug=True)