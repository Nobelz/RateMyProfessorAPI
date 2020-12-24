import re
import requests


class School:
    """Represents a school."""

    def __init__(self, school_id: int):
        """
        Initializes a school to the school id.

        :param school_id: The school's id.
        """

        self.id = school_id
        self.name = self._get_name()

    def _get_name(self):
        url = "https://www.ratemyprofessors.com/campusRatings.jsp?sid=%s" % self.id
        page = requests.get(url)
        school_names = re.findall(r"schoolName: '(.*?)'", page.text)

        if school_names:
            school_name = str(school_names[0])
        else:
            raise ValueError('Invalid school id or bad request.')

        return school_name

    def __eq__(self, other):
        return (self.name, self.id) == (other.name, other.id)
