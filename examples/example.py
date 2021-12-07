import ratemyprofessor

professor = ratemyprofessor.get_professor_by_school_and_name(
    ratemyprofessor.get_school_by_name("Case Western Reserve University"), "Connamacher")
if professor is not None:
    print("%sworks in the %s Department of %s." % (professor.name, professor.department, professor.school.name))
    print("Rating: %s / 5.0" % professor.rating)
    print("Difficulty: %s / 5.0" % professor.difficulty)
    print("Total Ratings: %s" % professor.num_ratings)
    if professor.would_take_again is not None:
        print(("Would Take Again: %s" % round(professor.would_take_again, 1)) + '%')
    else:
        print("Would Take Again: N/A")
else:
    print("Professor not found.")
    
print("\n\nTesting @Ozeitis's addition of deep_search_professor_by_school_and_name()")
#Testing a lookup for Yeshiva University John W. John alone gives three results
#John Hogan, David A. John, and the one we want, Christopher John Williams 

professor = ratemyprofessor.deep_get_professor_by_school_and_name(ratemyprofessor.get_school_by_name("Yeshiva University"), "John W")
if professor is not None:
    if professor.name == "Christopher John Williams":
        print("Sucesfully found the professor we want, %s" % professor.name)
        print("%sworks in the %s Department of %s." % (professor.name, professor.department, professor.school.name))
        print("Rating: %s / 5.0" % professor.rating)
        print("Difficulty: %s / 5.0" % professor.difficulty)
        print("Total Ratings: %s" % professor.num_ratings)
        if professor.would_take_again is not None:
            print(("Would Take Again: %s" % round(professor.would_take_again, 1)) + '%')
        else:
            print("Would Take Again: N/A")
    else:
        print("Found a professor, but it's not the one we want, %s" % professor.name)
else:
    print("Professor not found, @Ozeitis's test failed!")