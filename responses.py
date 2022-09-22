class ApplicationResponse():
    def __init__(self, **kwargs):
        self.full_name = kwargs["full_name"]
        self.email_address = kwargs["email_address"]
        self.can_commute = kwargs["can_commute"]
        self.us_authorized = kwargs["us_authorized"]
        self.sponsorship = kwargs["sponsorship"]
        self.what_attracted = kwargs["what_attracted"]
        self.salary_expected = kwargs["salary_expected"]
        self.favorite_software = kwargs["favorite_software"]
        self.hobbies = kwargs["hobbies"]
        self.constructive_criticism = kwargs["constructive_criticism"]
        self.love_job = kwargs["love_job"]
        self.use_submission = kwargs["use_submission"]

        # optional responses
        self.linkedin_url = kwargs["linkedin_url"] if kwargs.get("linkedin_url") else ""
        self.github_url = kwargs["github_url"] if kwargs.get("github_url") else ""
        self.resume_url = kwargs["resume_url"] if kwargs.get("resume_url") else ""
        self.django_experience = kwargs["django_experience"] if kwargs.get("django_experience") else 0.0
        self.react_experience = kwargs["react_experience"] if kwargs.get("react_experience") else 0.0
        self.mysql_experience = kwargs["mysql_experience"] if kwargs.get("mysql_experience") else 0.0
        self.gcp_experience = kwargs["gcp_experience"] if kwargs.get("gcp_experience") else 0.0
        self.software_experience = kwargs["software_experience"] if kwargs.get("software_experience") else 0.0


    def get_data(self):
        data = {
            "full_name": self.full_name,
            "email_address": self.email_address,
            "can_commute_to_natick_ma": self.can_commute,
            "are_you_able_to_work_in_the_united_states": self.us_authorized,
            "do_you_require_sponsorship": self.sponsorship,
            "what_attracted_you_to_level99": self.what_attracted,
            "what_is_your_expected_salary_range": self.salary_expected,
            "what_is_your_favorite_favorite_part_of_the_software_development_experience": self.favorite_software,
            "what_are_your_hobbies": self.hobbies,
            "what_was_the_best_constructive_criticism_you_ever_received": self.constructive_criticism,
            "what_would_make_you_love_this_job": self.love_job,
            "use_this_submission": self.use_submission,
        }

        # optional responses
        if self.linkedin_url: data["linkedin_profile"] = self.linkedin_url
        if self.github_url: data["github_profile"] = self.github_url
        if self.resume_url: data["link_to_resume"] = self.resume_url
        if self.django_experience: data["years_of_django_experience"] = self.django_experience
        if self.react_experience: data["years_of_react_experience"] = self.react_experience
        if self.mysql_experience: data["years_of_mysql_experience"] = self.mysql_experience
        if self.gcp_experience: data["years_of_gcp_experience"] = self.gcp_experience
        if self.software_experience: data["years_of_software_development_experience"] = self.software_experience
        
        return data