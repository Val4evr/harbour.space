"""Problem 05: Basic aggregates and GROUP BY.

Task:
1. Count all students
2. Compute average age
3. Compute min and max age
4. Count students per track (GROUP BY track)

Print each result.
"""

import sqlite3

DB_PATH = "school.db"


def main() -> None:
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    # TODO: SELECT COUNT(*) FROM students
    count_all = cur.execute("SELECT COUNT(*) FROM students").fetchone()

    # TODO: SELECT AVG(age) FROM students
    avg_age = cur.execute("SELECT AVG(age) FROM students").fetchone()
    # TODO: SELECT MIN(age), MAX(age) FROM students
    min_age = cur.execute("SELECT MIN(age) FROM students").fetchone()
    max_age = cur.execute("SELECT MAX(age) FROM students").fetchone()
    # TODO: SELECT track, COUNT(*) FROM students GROUP BY track
    track_count = cur.execute(
        "SELECT track, COUNT(*) FROM students GROUP BY track").fetchall()

    conn.close()

    print("count_all: ", count_all)
    print("avg_age: ", avg_age)
    print("min_age: ", min_age)
    print("max_age: ", max_age)
    print("track_count: ", track_count)


if __name__ == "__main__":
    main()
