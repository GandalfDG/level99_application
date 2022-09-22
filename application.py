"""
Usage: application [--submit]

-s, --submit    officially submit the application (off by default)
"""

from docopt import docopt
from requests import request

from responses import ApplicationResponse


API_URL = "http://35.245.9.156/api/collections/apply/records"

FULL_NAME = "Jack Case"
EMAIL_ADDRESS = "jackacase@gmail.com"
CAN_COMMUTE = True
US_AUTHORIZED = True
SPONSORSHIP_REQ = False
LINKEDIN_URL = "https://www.linkedin.com/in/jackacase/"
GITHUB_URL = "https://github.com/GandalfDG"
RESUME_URL = "TODO"

ATTRACTION = """
I've been working on various web development projects in my free time, and at
the same time I've been in the job market looking for something new. The
Linkedin message I got inviting me to 'apply by API' caught my eye, and learning
what the company is all about definitely piqued my interest further. So far in
my career I've worked at places making serious hardware for defense
applications, building energy monitoring applications so corporations can tick
the 'environmentally conscious' box, and developing IP for even larger companies
to save power on their wireless radio installations. What all of these have had
in common was a serious lack of being able to explain my job to my family and
friends, and a lack of that satisfying feeling of seeing someone truly enjoying
what I've made. Seeing that Level99 is innovating in the amusement industry, as
well as working with heavy-hitters in the industry including Disney Imagineering
really called out to me. My fiance (wife in just over a week!) and I love
amusement parks and rollercoasters, and she works as a Disney travel agent, so
to also be involved in this industry would be a dream come true!
"""

EXPECTED_SALARY = ""

FAVORITE_SOFTWARE_PART = """

"""

HOBBIES = """

"""

CONSTRUCTIVE_CRITICISM = """

"""

LOVE_THIS_JOB = """

"""


def main():
    args = docopt(__doc__)
    use_submission = args["--submit"]
    response = ApplicationResponse(
        full_name=FULL_NAME,
        email_address=EMAIL_ADDRESS,
        can_commute=CAN_COMMUTE,
        us_authorized=US_AUTHORIZED,
        sponsorship=SPONSORSHIP_REQ,
        what_attracted=ATTRACTION,
        salary_expected=EXPECTED_SALARY,
        favorite_software=FAVORITE_SOFTWARE_PART,
        hobbies=HOBBIES,
        constructive_criticism=CONSTRUCTIVE_CRITICISM,
        love_job=LOVE_THIS_JOB,
        use_submission=use_submission
    )

    print(response.get_data())

    api_response = request("POST", API_URL, data=response.get_data())
    print(api_response)
    pass


if __name__ == "__main__":
    main()
