import ratemyprofessor

professor = ratemyprofessor.get_professor_by_school_and_name(
    ratemyprofessor.get_school_by_name("Case Western Reserve University"), "Connamacher")
if professor is not None:
    print(f"{professor.name} works in the {professor.department} Department of {professor.school.name}.")
    print(f"Rating: {professor.rating} / 5.0")
    print(f"Difficulty: {professor.difficulty} / 5.0")
    print(f"Total Ratings: {professor.num_ratings}")
    if professor.would_take_again is not None:
        print(f"Would Take Again: {round(professor.would_take_again, 1)}%")
    else:
        print("Would Take Again: N/A")
