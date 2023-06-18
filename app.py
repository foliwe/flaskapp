from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
import pycountry
from typing import List, Dict

app = Flask(__name__)

# MySQL Connection Configuration
config = {
    'user': 'root',
    'password': 'root',
    'host': 'db',
    'port': '3306',
    'database': 'flaskapp'
}


def student() -> List[Dict]:
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    cursor.close()
    connection.close()


@app.route('/', methods=['GET', 'POST'])
def index():
    countries = [country.name for country in pycountry.countries]
    if request.method == 'POST':
        # Get form data
        full_name = request.form['full_name']
        date_of_birth = request.form['date_of_birth']
        email = request.form['email']
        sex = request.form['sex']
        date_of_stated = request.form['date_of_stated']
        country = request.form['country']
        contact_number = request.form['contact_number']
        it_knowledge = request.form['it_knowledge']
        comment = request.form['comment']

        # Connect to MySQL
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor()


        query = "INSERT INTO student (full_name, date_of_birth, email, sex, date_of_stated, country, contact_number, it_knowledge, comment) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = (full_name, date_of_birth, email, sex, date_of_stated, country, contact_number, it_knowledge, comment)
        cursor.execute(query, values)

        # Commit changes and close connection
        connection.commit()
        cursor.close()
        connection.close()

        # Redirect to thank you page
        return redirect(url_for('thank_you', name=full_name))

    return render_template('index.html', countries=countries)


@app.route('/thank-you/<name>')
def thank_you(name):
    return render_template('thank_you.html', name=name)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
