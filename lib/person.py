#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self, name="Harriet",job="Purchasing"):
        self._name = "Harriet"
        self._job = "Purchasing"

        self.name = name
        self.job = job

    def get_name (self):
        return self._name
    def set_name (self,name):
        if not isinstance(name,str):
             print("Name must be string between 1 and 25 characters.")
             return
        person = name.title()

        if  1 <= len(person)<= 25:
            self._name = person
        else:
            print("Name must be string between 1 and 25 characters.")

    name = property(get_name,set_name)

    def get_job(self):
        return self._job
    def set_job(self,job):
        if job in APPROVED_JOBS:
            self._job = job 
        else:
            print("Job must be in list of approved jobs.")
    job = property(get_job, set_job)

harry = Person("","Admin")
print(harry.name)
print(harry.job)

nate = Person("elly","")
print(nate.name)
print(nate.job)