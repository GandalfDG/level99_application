class ApplicationResponse():
    def __init__(self):
        self.full_name = ""
        self.email_address = ""
        self.can_commute = False
        self.us_authorized = False
        self.sponsorship = False
        self.linkedin_url = ""
        self.github_url = ""
        self.resume_url = ""
        self.what_attracted = ""
        self.salary_expected = ""
        self.favorite_software = ""
        self.hobbies = ""
        self.constructive_criticism = ""
        self.love_job = ""
        self.django_experience = 0.0
        self.react_experience = 0.0
        self.mysql_experience = 0.0
        self.gcp_experience = 0.0
        self.software_experience = 0.0
        self.use_submission = False

    def get_data(self):
        return {
            "full_name": self.full_name,
            "email_address": self.email_address,
            "can_commute_to_natick_ma": self.can_commute,
            "are_you_able_to_work_in_the_united_states": self.us_authorized,
            "do_you_require_sponsorship": self.sponsorship,
            "linkedin_profile": self.linkedin_url,
            "github_profile": self.github_url,
            "link_to_resume": self.resume_url,
            "what_attracted_you_to_level99": self.what_attracted,
            "what_is_your_expected_salary_range": self.salary_expected,
            "what_is_your_favorite_favorite_part_of_the_software_development_experience": self.favorite_software,
            "what_are_your_hobbies": self.hobbies,
            "what_was_the_best_constructive_criticism_you_ever_received": self.constructive_criticism,
            "what_would_make_you_love_this_job": self.love_job,
            "years_of_django_experience": self.django_experience,
            "years_of_react_experience": self.react_experience,
            "years_of_mysql_experience": self.mysql_experience,
            "years_of_gcp_experience": self.gcp_experience,
            "years_of_software_development_experience": self.software_experience,
            "use_this_submission": self.use_submission
        }