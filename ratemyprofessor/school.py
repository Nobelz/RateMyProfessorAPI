import re
import requests


class School:
    """Represents a school."""

    def __init__(self, school_id: int):
        """
        Initializes a school to the school id.

        :param school_id: The school's id.
        """

        self.school_id = school_id
        self.school_name = self._get_name()

    def _get_name(self) -> str:
        url = f'https://www.ratemyprofessors.com/campusRatings.jsp?sid={self.school_id}'
        page = requests.get(url)
        school_names = re.findall(r"schoolName: '(.*?)'", page.text)

        if school_names:
            school_name = str(school_names[0])
        else:
            raise ValueError('Invalid school id!')

        return school_name
