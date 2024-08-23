-- First, make sure you are using the correct database
USE your_database_name;

-- Create the 'exemplo' table with columns 'id', 'nome', and 'idade'
CREATE TABLE exemplo (
    id INT AUTO_INCREMENT PRIMARY KEY,  -- 'id' column as the primary key and auto-incremented
    nome VARCHAR(100) NOT NULL,          -- 'nome' column with a maximum length of 100 characters
    idade INT NOT NULL                   -- 'idade' column as an integer
);

-- Insert some fictional data into the 'exemplo' table
INSERT INTO exemplo (nome, idade) VALUES ('Alice', 25);
INSERT INTO exemplo (nome, idade) VALUES ('Bob', 30);
INSERT INTO exemplo (nome, idade) VALUES ('Carlos', 22);
INSERT INTO exemplo (nome, idade) VALUES ('Diana', 28);
INSERT INTO exemplo (nome, idade) VALUES ('Eduardo', 35);
