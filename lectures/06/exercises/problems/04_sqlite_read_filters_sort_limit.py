"""Problem 04: Practice WHERE, ORDER BY, LIMIT.

Task:
1. Get students with age >= 22
2. Sort students by age DESC
3. Return only top 3 oldest students
4. Get backend students younger than 23

Use parameterized queries for filter values.
"""

import sqlite3

DB_PATH = "school.db"


def main() -> None:
    filter_age = 22
    filter_track = "backend"
    filter_age_less_than = 23
    top_n = 3

    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    # TODO 1: age >= 22
    age_at_least = cur.execute(
        "SELECT * FROM students WHERE age >= ?", (filter_age,)
    ).fetchall()

    # TODO 2 + 3: order by age desc, limit 3
    oldest_top_n = cur.execute(
        "SELECT * FROM students ORDER BY age DESC LIMIT ?", (top_n,)
    ).fetchall()

    # TODO 4: track='backend' and age < 23
    backend_under = cur.execute(
        "SELECT * FROM students WHERE track = ? AND age < ?",
        (filter_track, filter_age_less_than),
    ).fetchall()

    conn.close()

    print(f"Students with age >= {filter_age}:\n{age_at_least}\n")
    print(f"Top {top_n} oldest:\n{oldest_top_n}\n")
    print(
        f"track={filter_track!r}, age < {filter_age_less_than}:\n{backend_under}"
    )


if __name__ == "__main__":
    main()
