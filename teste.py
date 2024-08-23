from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

# MySQL database configuration
db_config = {
    'user': 'extreme',         # Database user
    'password': 'extreme',     # Database password
    'host': 'localhost',             # Host where the database is running
    'database': 'extreme' # Name of the database
}

# Function to connect to the MySQL database
def connect_to_database():
    connection = mysql.connector.connect(**db_config)
    return connection

# What is an endpoint? It's a URL that responds to a specific request.
# This is the root endpoint that you can access at http://localhost:5000/
@app.route('/')
def index():
    return "Welcome to the API!"

# This endpoint returns data from the "exemplo" table in JSON format
@app.route('/data', methods=['GET'])
def get_data():
    # Connect to the database
    connection = connect_to_database()
    cursor = connection.cursor(dictionary=True)  # Using dictionary=True to get results as dictionaries
    
    # Execute the SQL query to get all records from the "exemplo" table
    cursor.execute("SELECT nome, idade FROM exemplo")
    
    # Fetch all results from the query
    results = cursor.fetchall()
    
    # Close the database connection
    cursor.close()
    connection.close()
    
    # Return the results in JSON format
    return jsonify(results)

# Run the Flask application
if __name__ == '__main__':
    # The application runs on host 'localhost' and port 5000 by default
    app.run(debug=True)
