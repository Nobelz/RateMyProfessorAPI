import requests
import json
import base64
import os
import datetime
from bs4 import BeautifulSoup

from functools import total_ordering
from .school import School

current_path = os.path.dirname(__file__)
with open(os.path.join(current_path, "json/ratingsquery.json"), 'r') as f:
    ratings_query = json.load(f)

with open(os.path.join(current_path, "json/professorquery.json"), 'r') as f:
    professor_query = json.load(f)

with open(os.path.join(current_path, "json/header.json"), 'r') as f:
    headers = json.load(f)


@total_ordering
class Professor:
    """Represents a professor."""

    def __init__(self, professor_id: int):
        """
        Initializes a professor to the professor id.

        :param professor_id: The professor's id.
        """

        self.id = professor_id
        self._get_rating_info(professor_id)

    def _get_rating_info(self, professor_id: int):
        headers["Referer"] = "https://www.ratemyprofessors.com/ShowRatings.jsp?tid=%s" % professor_id
        professor_query["variables"]["id"] = base64.b64encode(("Teacher-%s" % professor_id)
                                                              .encode('ascii')).decode('ascii')
        data = requests.post(url="https://www.ratemyprofessors.com/graphql", json=professor_query, headers=headers)

        if data is None or json.loads(data.text)["data"]["node"] is None:
            raise ValueError("Professor not found with that id or bad request.")

        professor_data = json.loads(data.text)["data"]["node"]
        courses_data = professor_data["courseCodes"]

        self.courses = []
        for course_data in courses_data:
            self.courses.append(Course(professor=self, count=course_data["courseCount"],
                                       name=course_data["courseName"]))

        self.name = professor_data["firstName"] + ' ' + professor_data["lastName"]
        self.department = professor_data["department"]
        self.difficulty = professor_data["avgDifficulty"]
        self.rating = professor_data["avgRating"]
        if professor_data["wouldTakeAgainPercent"] == 0:
            self.would_take_again = None
        else:
            self.would_take_again = professor_data["wouldTakeAgainPercent"]
        self.num_ratings = professor_data["numRatings"]
        self.school = School(int(base64.b64decode(
            professor_data["school"]["id"].encode('ascii')).decode('ascii')[7:]))

    def get_ratings(self, course_name=None):
        """
        Returns a list of strings that represent the courses that have ratings for that particular course name.

        If the professor has not been rated, this returns an empty list.
        Likewise, if there are no ratings for the course name, this will also return an empty list.
        If no course name is given, this method finds all the course names.


        :return: A list of the professor's courses for that course name.
        """
        if self.num_ratings == 0:
            return []

        headers["Referer"] = "https://www.ratemyprofessors.com/ShowRatings.jsp?tid=%s" % self.id
        ratings_query["variables"]["id"] = base64.b64encode(("Teacher-%s" % self.id).encode('ascii')).decode('ascii')
        ratings_query["variables"]["count"] = self.num_ratings

        if course_name is not None:
            course_found = False
            for course in self.courses:
                if course.name == course_name:
                    course_found = True

            if course_found is False:
                return []
            else:
                ratings_query["variables"]["courseFilter"] = course_name

        data = requests.post(url="https://www.ratemyprofessors.com/graphql", json=ratings_query, headers=headers)

        if data is None or json.loads(data.text)["data"]["node"]["ratings"]["edges"] is None:
            return []

        ratings_data = json.loads(data.text)["data"]["node"]["ratings"]["edges"]
        ratings = []

        for rating_data in ratings_data:
            rating = rating_data["node"]

            if rating["attendanceMandatory"] == "non mandatory":
                attendance_mandatory = False
            elif rating["attendanceMandatory"] == "mandatory":
                attendance_mandatory = True
            else:
                attendance_mandatory = None

            if bool(rating["isForCredit"]) is False:
                credit = False
            elif bool(rating["isForCredit"]) is True:
                credit = True
            else:
                credit = None

            if bool(rating["isForOnlineClass"]) is False:
                online_class = False
            elif bool(rating["isForOnlineClass"]) is True:
                online_class = True
            else:
                online_class = None

            if rating["wouldTakeAgain"] == 1:
                take_again = True
            elif rating["wouldTakeAgain"] == 0:
                take_again = False
            else:
                take_again = None

            date = datetime.datetime.strptime(rating["date"][0:19], '%Y-%m-%d %H:%M:%S')

            ratings.append(Rating(rating=rating["helpfulRating"], difficulty=rating["difficultyRating"],
                                  comment=rating["comment"], class_name=rating["class"], date=date,
                                  take_again=take_again, grade=rating["grade"], thumbs_up=rating["thumbsUpTotal"],
                                  thumbs_down=rating["thumbsDownTotal"], online_class=online_class, credit=credit,
                                  attendance_mandatory=attendance_mandatory))

        return ratings

    def __repr__(self):
        return self.name

    def __lt__(self, other):
        return self.num_ratings < other.num_ratings

    def __eq__(self, other):
        return (self.name, self.department, self.school) == (other.name, other.department, other.school)


class Course:
    """Represents a course."""

    def __init__(self, professor: Professor, count: int, name: str):
        """
        Initializes a course.

        :param professor: The professor who teaches the course.
        :param count: The number of ratings for the course.
        :param name: The name of the course.
        """
        self.professor = professor
        self.name = name
        self.count = count


@total_ordering
class Rating:
    """Represents a rating."""

    def __init__(self,  rating: int, difficulty: int, comment: str, class_name: str, date: datetime,
                 take_again=None, grade=None, thumbs_up: int = 0, thumbs_down: int = 0, online_class=None, credit=None,
                 attendance_mandatory=None):
        """
        Initializes a rating.

        Note that some fields may be None, and that you may be required to check if those are None.

        :param rating: The rating number.
        :param difficulty: The difficulty rating.
        :param comment: The rating comment.
        :param class_name: The class the rating was for.
        :param date: The date the rating was made.
        :param take_again: If the person who made the rating would take the class again, if any
        :param grade: The grade of the person who made the rating, if any
        :param thumbs_up: The number of thumbs up for the rating
        :param thumbs_down: The number of thumbs down for the rating
        :param online_class: If the rating is for an online class, if any
        :param credit: If the rating was for credit, if any
        :param attendance_mandatory: If attendance was mandatory for the class, if any
        """
        self.rating = rating
        self.difficulty = difficulty
        self.comment = BeautifulSoup(comment, "lxml").text
        self.class_name = class_name
        self.date = date
        self.take_again = take_again
        self.grade = grade
        self.thumbs_up = thumbs_up
        self.thumbs_down = thumbs_down
        self.online_class = online_class
        self.credit = credit
        self.attendance_mandatory = attendance_mandatory

    def __lt__(self, other):
        return self.date > other.date
