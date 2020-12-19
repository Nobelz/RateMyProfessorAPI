import requests

from lxml import etree
from .school import School


class Professor:
    """Represents a professor."""

    def __init__(self, school: School, professor_id: int):
        """
        Initializes a school to the school id.

        :param school: The professor's school.
        :param professor_id: The professor's id.
        """

        self.school: School = school
        self.id = professor_id
        self._get_rating_info(professor_id)

    def _get_rating_info(self, professor_id: int):
        url = f"https://www.ratemyprofessors.com/ShowRatings.jsp?tid={professor_id}"
        page = requests.get(url)
        html = etree.HTML(page.text)

        # Name
        try:
            first_name = (html.xpath('//*[@id="root"]/div/div/div[3]/div[1]/div[1]/div[2]/div[1]/span[1]/text()'))[0]
            last_name = (html.xpath('//*[@id="root"]/div/div/div[3]/div[1]/div[1]/div[2]/div[1]/span[2]/text()'))[0]
            self.name: str = first_name + ' ' + last_name
        except (ValueError, IndexError):
            self.name = None

        # Rating
        try:
            rating = (html.xpath('//*[@id="root"]/div/div/div[3]/div[1]/div[1]/div[1]/div[1]/div/div[1]/text()'))[0]
            self.rating: float = float(rating)
        except (ValueError, IndexError):
            self.rating = None

        # % Would Take Again and Difficulty Rating
        try:
            diff = (html.xpath('//*[@id="root"]/div/div/div[3]/div[1]/div[1]/div[3]/div/div[1]/text()'))
            if len(diff) == 2:
                self.difficulty: float = float(diff[1])
                self.would_take_again: int = int(diff[0])
            elif len(diff) == 1:
                self.difficulty: float = float(diff[0])
                self.would_take_again = None
            else:
                self.difficulty = None
                self.would_take_again = None
        except (ValueError, IndexError):
            self.difficulty = None
            self.would_take_again = None

        # Number of Ratings
        try:
            num_ratings = (html.xpath('//*[@id="root"]/div/div/div[3]/div[1]/div[1]/div[1]/div[2]/div/a/text()'))[0]
            self.num_ratings: int = int(num_ratings)
        except (ValueError, IndexError):
            self.num_ratings = 0

        # Department
        try:
            department = (html.xpath('//*[@id="root"]/div/div/div[3]/div[1]/div[1]/div[2]/div[2]/span/b/text()'))[0]
            self.department: str = str(department)
        except (ValueError, IndexError):
            self.department = None

