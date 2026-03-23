"""Problem 07: Create and read data with SQLAlchemy.

Task:
1. Open a SQLAlchemy Session on `school.db`.
2. Create one Assignment for an existing student.
3. Read all students.
4. Read students with age >= 22 sorted by age descending.
5. Read assignments with joined student names.

Starter:
- Reuse `Student` and `Assignment` from `db_models.py`.
- Use `select(...)` queries.
"""

from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

from db_models import Assignment, Student

DB_URL = "sqlite:///school.db"


def main() -> None:
    engine = create_engine(DB_URL, echo=False)

    with Session(engine) as session:
        # TODO 1: add an assignment for an existing student
        ana = session.execute(
            select(Student).where(Student.email == "ana@example.com")
        ).scalar_one()
        session.add(Assignment(title="Homework 1", score=90, student_id=ana.id))
        session.commit()

        # TODO 2: read all students
        students = session.execute(select(Student)).scalars().all()
        print("All students:")
        for s in students:
            print(f"  {s.name}, age={s.age}, track={s.track}")

        # TODO 3: read filtered + sorted students
        older = session.execute(
            select(Student).where(Student.age >= 22).order_by(Student.age.desc())
        ).scalars().all()
        print("\nStudents age >= 22 (desc):")
        for s in older:
            print(f"  {s.name}, age={s.age}")

        # TODO 4: read assignments with joined student names
        assignments = session.execute(select(Assignment)).scalars().all()
        print("\nAssignments:")
        for a in assignments:
            print(f"  [{a.student.name}] {a.title} — score={a.score}")


if __name__ == "__main__":
    main()
