from flask import Flask, render_template, request, redirect, url_for
import mysql.connector, uuid
import pycountry

app = Flask(__name__)

# MySQL Connection Configuration
# MySQL Connection Configuration
mysql_config = {
    'user': 'root',
    'password': 'Foli1882',
    'host': 'flaskapp-db',  # Use the Docker Compose service name here
    'database': 'flaskapp'
}


# Connect to MySQL
conn = mysql.connector.connect(**mysql_config)
cursor = conn.cursor()

# Check if table exists
cursor.execute("SHOW TABLES LIKE 'student'")
table_exists = cursor.fetchone()

if not table_exists:
    # Create the student table
    # Create the student table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS student (
        id VARCHAR(36) PRIMARY KEY,
        full_name VARCHAR(100) NOT NULL,
        date_of_birth DATE NOT NULL,
        email VARCHAR(100) NOT NULL,
        sex VARCHAR(10) NOT NULL,
        date_of_stated DATE NOT NULL,
        country VARCHAR(100) NOT NULL,
        contact_number VARCHAR(20) NOT NULL,
        it_knowledge VARCHAR(20) NOT NULL,
        comment TEXT
    )
""")
    print("Table 'student' created successfully.")
else:
    print("Table 'student' already exists.")

# Close connection
cursor.close()
conn.close()

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
        conn = mysql.connector.connect(**mysql_config)
        cursor = conn.cursor()

        record_id = str(uuid.uuid4())

        query = "INSERT INTO student (id, full_name, date_of_birth, email, sex, date_of_stated, country, contact_number, it_knowledge, comment) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = (record_id, full_name, date_of_birth, email, sex, date_of_stated, country, contact_number, it_knowledge, comment)
        cursor.execute(query, values)

        # Commit changes and close connection
        conn.commit()
        cursor.close()
        conn.close()

        # Redirect to thank you page
        return redirect(url_for('thank_you', name=full_name))

    return render_template('index.html', countries=countries)

@app.route('/thank-you/<name>')
def thank_you(name):
    return render_template('thank_you.html', name=name)

if __name__ == '__main__':
    app.run()
