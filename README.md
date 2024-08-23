# API-example-flask

This project is a simple example of a RESTful API built with Python's Flask framework. The API connects to a MySQL database, retrieves data from a table, and returns it in JSON format.

## What is an API?

An API (Application Programming Interface) is a set of definitions and protocols that allow different software systems or components to communicate with each other. In the context of a web API, it typically refers to a service that allows different clients (like web browsers or mobile apps) to interact with a server to retrieve or manipulate data.

### Advantages of Using an API

1. **Separation of Concerns**: APIs allow different parts of a system to be developed and maintained independently. For example, the frontend of an application can be developed separately from the backend.
2. **Code Reusability**: APIs enable functionality to be reused across different applications. A well-designed API can be used by various clients, such as websites, mobile apps, or even other APIs.
3. **Scalability**: APIs allow different services within an application to be scaled independently, helping to maintain and expand the application as it grows.

## Project Setup

### Prerequisites

- Python 3.7 or higher
- MySQL server running locally
- MySQL Connector for Python (`mysql-connector-python` package)
- Flask (`flask` package)

### Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/zmovirzynski/API-example-flask.git
   cd flask-mysql-api-example
   ```

2. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Set up the MySQL database**:

   - Create a MySQL database and a table named `exemplo`.
   - Insert some sample data into the table.

   Here is an example SQL script to set up the database:

   ```sql
   USE your_database_name;

   CREATE TABLE exemplo (
       id INT AUTO_INCREMENT PRIMARY KEY,
       nome VARCHAR(100) NOT NULL,
       idade INT NOT NULL
   );

   INSERT INTO exemplo (nome, idade) VALUES ('Alice', 25);
   INSERT INTO exemplo (nome, idade) VALUES ('Bob', 30);
   INSERT INTO exemplo (nome, idade) VALUES ('Carlos', 22);
   INSERT INTO exemplo (nome, idade) VALUES ('Diana', 28);
   INSERT INTO exemplo (nome, idade) VALUES ('Eduardo', 35);
   ```

4. **Configure the database connection in the Python code**:

   - In the `app.py` file, update the `db_config` dictionary with your MySQL credentials:

     ```python
     db_config = {
         'user': 'your_username',
         'password': 'your_password',
         'host': 'localhost',
         'database': 'your_database_name'
     }
     ```

5. **Run the Flask application**:

   ```bash
   python app.py
   ```

   The application will run locally on `http://localhost:5000`.

## API Endpoints

- **`GET /`**: A simple welcome message to ensure the API is running.

- **`GET /data`**: Retrieves all records from the `exemplo` table and returns them in JSON format.

## Example Response

```json
[
    {
        "nome": "Alice",
        "idade": 25
    },
    {
        "nome": "Bob",
        "idade": 30
    },
    {
        "nome": "Carlos",
        "idade": 22
    }
]
```

## License

This project is licensed under the MIT License.
