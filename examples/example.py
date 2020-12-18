import ratemyprofessor


professor = ratemyprofessor.get_professor_by_school_and_name(
    ratemyprofessor.get_school_by_name("Case Western Reserve University"), "Connamacher")
print(f"Professor name: {professor.name}")
print(f"Professor rating: {professor.rating} / 5.0")
print(f"Professor difficulty: {professor.difficulty} / 5.0")