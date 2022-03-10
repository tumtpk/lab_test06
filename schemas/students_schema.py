def student_serializer(student) -> dict:
    return {
        "id": str(student["_id"]),
        "name": student["name"],
        "description": student["description"],
        "completed": student["completed"],
        "date": student["date"],
    }

def students_serializer(students) -> list:
    return [student_serializer(student) for student in students]