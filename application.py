"""
Usage: application [--submit]

-s, --submit    officially submit the application (off by default)
"""

from docopt import docopt
import requests

from responses import ApplicationResponse


API_URL = "http://35.245.9.156/api/collections/apply/records"

FULL_NAME = "Jack Case"
EMAIL_ADDRESS = "jackacase@gmail.com"
CAN_COMMUTE = True
US_AUTHORIZED = True
SPONSORSHIP_REQ = False
LINKEDIN_URL = "https://www.linkedin.com/in/jackacase/"
GITHUB_URL = "https://github.com/GandalfDG"
RESUME_URL = ""

ATTRACTION = """

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
    pass


if __name__ == "__main__":
    main()
