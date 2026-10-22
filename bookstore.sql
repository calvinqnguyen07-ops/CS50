CREATE TABLE authors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);

CREATE TABLE books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author_id INTEGER NOT NULL,
    year INTEGER,
    price REAL,
    FOREIGN KEY (author_id) REFERENCES authors(id)
);

INSERT INTO authors (name) VALUES
    ('Ursula K. Le Guin'),
    ('Octavia Butler'),
    ('Isaac Asimov');

INSERT INTO books (title, author_id, year, price) VALUES
    ('A Wizard of Earthsea', 1, 1968, 9.99),
    ('The Dispossessed', 1, 1974, 11.50),
    ('Kindred', 2, 1979, 10.25),
    ('Foundation', 3, 1951, 8.75);

-- Books with author names, newest first
SELECT books.title, authors.name, books.year
FROM books
JOIN authors ON books.author_id = authors.id
ORDER BY books.year DESC;

-- Number of books and average price per author
SELECT authors.name, COUNT(*) AS book_count, ROUND(AVG(books.price), 2) AS avg_price
FROM books
JOIN authors ON books.author_id = authors.id
GROUP BY authors.id;
