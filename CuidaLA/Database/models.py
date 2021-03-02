from django.db import models
from datetime import datetime

# Create your models here.

class Locations(models.Model):
    name=models.CharField(max_length=30)

class Skills(models.Model):
    name=models.CharField(max_length=30)

class Services(models.Model):
    name=models.CharField(max_length=30)

class User(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    legal_id=models.CharField(max_length=10)
    email=models.EmailField()
    password=models.CharField(max_length=50)
    caregiver=models.BooleanField()
    patient=models.BooleanField()
    adress=models.CharField(max_length=50)
    phone=models.CharField(max_length=15)
    created_at=models.DateTimeField(default=datetime.now, blank=True)
    updated_at=models.DateTimeField(default=datetime.now, blank=True)
    location_id=models.ForeignKey(Locations, on_delete=models.CASCADE)
    photo=models.ImageField()

class Caregiver_service(models.Model):
    service_id=models.ForeignKey(Services, on_delete=models.CASCADE)
    user_id=models.ForeignKey(User, on_delete=models.CASCADE)

class Caregiver_skills(models.Model):
    skill_id=models.ForeignKey(Skills, on_delete=models.CASCADE)
    user_id=models.ForeignKey(User, on_delete=models.CASCADE)

class Works(models.Model):
    employer=models.CharField(max_length=30)
    work_title=models.CharField(max_length=30)
    start_date=models.DateTimeField(auto_now=True)
    end_date=models.DateTimeField(auto_created=True)
    job_description=models.CharField(max_length=150)
    location_id=models.ForeignKey(Locations, on_delete=models.CASCADE)
    user_id=models.ForeignKey(User, on_delete=models.CASCADE)

class School(models.Model):
    name=models.CharField(max_length=50)
    study=models.CharField(max_length=30)
    start_date=models.DateTimeField(auto_created=True)
    end_date=models.DateTimeField(auto_created=True)
    user_id=models.ForeignKey(User, on_delete=models.CASCADE)
    location_id=models.ForeignKey(Locations, on_delete=models.CASCADE)

class Jobs(models.Model):
    the_type=models.CharField(max_length=30)
    created_at=models.DateTimeField(auto_created=True)
    tart_date=models.DateTimeField(auto_created=True)
    end_date=models.DateTimeField(auto_created=True)
    patient_phone=models.CharField(max_length=10)
    patient_age=models.IntegerField()
    user_id=models.ForeignKey(User, on_delete=models.CASCADE)
    salary_start=models.IntegerField()
    salary_end=models.IntegerField()
    status=models.CharField(max_length=10)
    updated_at=models.DateTimeField(auto_now_add=True)
    location_id=models.CharField(max_length=30)

class Applicants(models.Model):
    job_id=models.ForeignKey(Jobs, on_delete=models.CASCADE)
    caregiver_offer=models.IntegerField()
    patient_offer=models.IntegerField()
    status=models.CharField(max_length=10)
    created_at=models.DateTimeField(auto_created=True)
    updated_at=models.DateTimeField(auto_now_add=True)

class Availability(models.Model):
    job_id=models.ForeignKey(Jobs, on_delete=models.CASCADE)
    morning=models.BooleanField()
    afternoon=models.BooleanField()
    night=models.BooleanField()
    days=models.CharField(max_length=60)

class Job_service(models.Model):
    job_id=models.ForeignKey(Jobs, on_delete=models.CASCADE)
    service_id=models.ForeignKey(Services, on_delete=models.CASCADE)