import unittest
import ratemyprofessor


from ratemyprofessor import School
from ratemyprofessor import Professor


class Test(unittest.TestCase):
    def test_school(self):
        cwru = School(186)

        # Test if school can be found
        self.assertEqual(cwru, ratemyprofessor.get_school_by_name("Case Western Reserve University"))

        # Test School constructor
        self.assertEqual(cwru.name, "Case Western Reserve University")
        self.assertEqual(cwru.id, 186)

        # Test if school cannot be found
        self.assertIsNone(ratemyprofessor.get_school_by_name("Case Eastern Reserve University"))

        # Test invalid school id
        try:
            School(-1)
            self.fail()
        except ValueError:
            pass

        # Test if schools can be found
        self.assertIsNotNone(ratemyprofessor.get_schools_by_name("University"))

        # Test if schools cannot be found
        self.assertEqual([], ratemyprofessor.get_schools_by_name("Fake University That Does Not Exist"))

        # Test if all the schools can be found
        self.assertEqual(6, len(ratemyprofessor.get_schools_by_name("Ohio State")))

    def test_professor(self):
        connamacher = Professor(1658282)

        # Test if professor can be found
        self.assertEqual(connamacher, ratemyprofessor.get_professor_by_school_and_name(School(186), "Connamacher"))

        # Test Professor constructor
        self.assertEqual("Harold Connamacher", connamacher.name)
        self.assertEqual("Computer Science", connamacher.department)
        self.assertEqual(School(186), connamacher.school)

        # Test if professor cannot be found
        self.assertIsNone(ratemyprofessor.get_professor_by_school_and_name(School(186), "Captain Obvious"))

        # Test invalid professor id
        try:
            Professor(1)
            self.fail()
        except ValueError:
            pass

        # Test if professors can be found
        professors = ratemyprofessor.get_professors_by_school_and_name(School(186), "Smith")
        self.assertIsNotNone(professors)

        # Test if professors are being sorted by number of ratings
        professors.sort()

        lowest_ratings_professor = professors[0]
        for professor in professors:
            if professor < lowest_ratings_professor:
                self.fail()
            lowest_ratings_professor = professor

        # Test if professors cannot be found
        self.assertEqual([], ratemyprofessor.get_professors_by_school_and_name(School(186), "Peter Rabbit"))

    def test_ratings(self):
        connamacher = Professor(1658282)

        ratings = connamacher.get_ratings()
        ratings.sort()

        most_recent_rating = ratings[0]
        print(most_recent_rating.date)
        for rating in ratings:
            # Tests to make sure that the ratings are sorted from newest to oldest
            if rating < most_recent_rating:
                self.fail()
            most_recent_rating = rating


if __name__ == '__main__':
    unittest.main()
