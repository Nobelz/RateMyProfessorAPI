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
        self._get_rating_info(professor_id)

    def _get_rating_info(self, professor_id: int):
        url = f"https://www.ratemyprofessors.com/ShowRatings.jsp?tid={professor_id}"
        page = requests.get(url)
        html = etree.HTML(page.text)

        # Name
        try:
            names = (html.xpath('//*[@id="root"]/div/div/div[3]/div[1]/div[1]/div[2]/div[1]/span/text()'))[0]
            self.name: str = names[0] + ' ' + names[1]
        except (ValueError, IndexError):
            self.name = None

        # Rating
        try:
            rating = (html.xpath('//*[@id="root"]/div/div/div[3]/div[1]/div[1]/div[1]/div[1]/div/div[1]/text()'))[0]
            self.rating: float = float(rating)
        except (ValueError, IndexError):
            self.rating = None

        # Difficulty Rating
        try:
            diff = (html.xpath('//*[@id="root"]/div/div/div[3]/div[1]/div[1]/div[3]/div[2]/div[1]/text()'))[0]
            self.difficulty: float = float(diff)
        except (ValueError, IndexError):
            self.difficulty = None
