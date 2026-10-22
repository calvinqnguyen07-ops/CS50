CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);

CREATE TABLE courses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL
);

CREATE TABLE enrollments (
    student_id INTEGER,
    course_id INTEGER,
    grade REAL,
    PRIMARY KEY (student_id, course_id),
    FOREIGN KEY (student_id) REFERENCES students(id),
    FOREIGN KEY (course_id) REFERENCES courses(id)
);

INSERT INTO students (name) VALUES ('Ana'), ('Ben'), ('Carla');
INSERT INTO courses (title) VALUES ('Databases'), ('Web Design'), ('Python');

INSERT INTO enrollments VALUES
    (1, 1, 92.5), (1, 3, 88.0),
    (2, 1, 75.0), (2, 2, 81.5),
    (3, 3, 95.0);

-- Every student with their courses and grades
SELECT students.name, courses.title, enrollments.grade
FROM enrollments
JOIN students ON enrollments.student_id = students.id
JOIN courses ON enrollments.course_id = courses.id
ORDER BY students.name;

-- Students above the overall average grade
SELECT name FROM students
WHERE id IN (
    SELECT student_id FROM enrollments
    WHERE grade > (SELECT AVG(grade) FROM enrollments)
);
