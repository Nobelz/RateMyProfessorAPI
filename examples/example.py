import ratemyprofessor


professor = ratemyprofessor.get_professor_by_school_and_name(
    ratemyprofessor.get_school_by_name("Case Western Reserve University"), "Connamacher")
if professor is not None:
    print(f"Name: {professor.name}")
    print(f"Department: {professor.department}")
    print(f"Rating: {professor.rating} / 5.0")
    print(f"Difficulty: {professor.difficulty} / 5.0")
    if professor.would_take_again is not None:
        print(f"Would Take Again: {professor.would_take_again} %")
    else:
        print(f"Would Take Again: N/A")
