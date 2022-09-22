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
RESUME_URL = "https://1drv.ms/b/s!Av1-0TFQHMsJjIpvHlqxUl2LmX1CPw?e=7cVboz"

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
""".lstrip()

EXPECTED_SALARY = "I'm looking for a salary in the $115k to $140k range."

FAVORITE_SOFTWARE_PART = """
My favorite part of the software development process is when a new feature
requires going back to the drawing board as it doesn't quite mesh with the
existing architecture, and then finding and implementing an elegant way to
integrate the feature, improving the overall software architecture in the
process. Other than that the purely satisfying phase when you're approaching
an MVP for a new project.
""".lstrip()

HOBBIES = """
Outside of work I enjoy 3D sculpting, 3D printing, and painting miniatures,
visiting amusement parks and riding rollercoasters (I've ridden 67 unique
coasters so far), camping and biking, and tinkering with electronics and web
development projects. In college I sang in an a cappella group and have a solo
on the album we recorded (Sing It! by the Brick City Singers on Spotify).
""".lstrip()

CONSTRUCTIVE_CRITICISM = """
I got this constructive criticism from my manager at maxlinear when I was
working on debugging issues in the lab along with the hardware designers, which
was to 'be an engineer, not a technician' when working on debug. At the time I
was simply reading and writing registers through our debug CLI, but wasn't
really thinking about what I was actually doing. This encouraged me to be more
involved in the debug process, to dig into our register documentation, and
making my own suggestions and being an active participant in the lab debug
process. As I gained confidence with our product, and worked through more
bringups in the lab, I was able to much more effectively track down bugs in our
system whether they turned out to be software issues, or hardware issues.
""".lstrip()

LOVE_THIS_JOB = """
I would love this job as I would get to put the web development skills I've
developed on my own time to good use as part of a team working on software for a
fun and exciting industry. I've had enough of working on teams using outdated
technology without automated testing and release pipelines. I want to work in
the fast-paced environment of web technologies and contribute to something that
I can explain to and share with anyone.
""".lstrip()


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

        linkedin_url=LINKEDIN_URL,
        github_url=GITHUB_URL,
        resume_url=RESUME_URL,

        django_experience=0.75,
        software_experience=5,
        use_submission=use_submission
    )

    print(response.get_data())

    api_response = request("POST", API_URL, json=response.get_data())
    print(api_response.text)
    pass


if __name__ == "__main__":
    main()
