from peewee import *

# Define DB

db = SqliteDatabase("students.db")


# Model

class Student(Model):
    username = CharField(max_length=255, unique=True)
    points = IntegerField(default=0)

    class Meta:
        database = db


students = [
    {'username': 'GaryTok', 'points': 200000, },
    {'username': 'booby', 'points': 14500},
    {'username': 'jimmmy', 'points': 4321, },
    {'username': 'yaaaa', 'points': 32232},
    {'username': 'joeyy', 'points': 4500, },
    {'username': 'jamespeach', 'points': 3211},
]


def add_students():
    for student in students:
        try:
            Student.create(username=student['username'], points=student['points'])
        except IntegrityError:
            student_record = Student.get(username=student['username'])
            student_record.points = student['points']
            student_record.save()

def top_student():
    student = Student.select().order_by(Student.points.desc()).get()
    return student

# Create table

if __name__ == "__main__":
    db.connect()
    db.create_tables([Student], safe=True)
    add_students()
    print("Our top student right now it: {0.username}".format(top_student()))
