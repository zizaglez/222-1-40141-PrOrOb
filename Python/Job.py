class Job:
    def __init__(self, job_salary, job_position, job_description, job_location, job_company, job_working_hours):
        self.job_salary = job_salary
        self.job_position = job_position
        self.job_description = job_description
        self.job_location = job_location
        self.job_company = job_company
        self.job_working_hours = job_working_hours

    def job_is_hiring(self):
        return "+Job is hiring"

    def job_is_not_hiring(self):
        return "+Job is not hiring"

    def job_is_open(self):
        return "+Job is open"

    def new_job_position(self, job_salary, job_position, job_location, job_company):
        return "+There is a new job position at " +job_company+" with a starting salary of $"+str(job_salary)+". Company is located in "+job_location+". They're looking for a "+job_position

    def job_salary_increase(self, job_salary, job_position, job_working_hours):
        if job_working_hours > 40 and job_position == "Software Engineer":
            job_salary = job_salary * 1.25
            return "+The salary for the "+job_position+" position has increased to $"+str(job_salary)+" if the employee works more than 40 hours per week"
        else:
            return "+The salary for the "+job_position+" position has not increased."


    def employee_will_get_raise(self, job_position, job_working_hours):
        if job_working_hours > 40 and job_position == "Software Engineer":
            return "+Employee will get a raise"
        else:
            return "+Employee will not get a raise"


new_job = Job(20000, "Software Engineer", "We are looking for a software engineer to join our team", "Guadalajara", "TechCompany", 48)

print(new_job.job_is_hiring())
print(new_job.job_is_not_hiring())
print(new_job.job_is_open())
print(new_job.new_job_position(new_job.job_salary, new_job.job_position, new_job.job_location, new_job.job_company))
print(new_job.job_salary_increase(new_job.job_salary, new_job.job_position, new_job.job_working_hours))
print(new_job.employee_will_get_raise(new_job.job_position, new_job.job_working_hours)) 