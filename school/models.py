from django.db import models

# Create your models here.
class studentsdetail(models.Model):
    rollnbr = models.BigAutoField(primary_key=True)
    s_name = models.CharField(max_length=50)
    s_fname = models.CharField(max_length=50)
    dob = models.DateField()
    date_join = models.DateField()
    c_position = models.BooleanField(default=True)
    sex = models.BooleanField(default=True)
    address = models.CharField(max_length=200)
    fm_number = models.CharField(max_length=15)

    def __str__(self):
        return self.s_name


class yearclass(models.Model):
    year=models.IntegerField(primary_key=True,default=2021)

    def __str__(self):
        return str(self.year)

class months(models.Model):
    monthname = models.CharField(max_length=50)
    def __str__(self):
        return str(self.monthname)

class schoolclasses(models.Model):
    standardname = models.CharField(max_length=100)
    def __str__(self):
        return self.standardname

class enroll_student(models.Model):
    years = models.ForeignKey(yearclass,on_delete=models.CASCADE)
    standard = models.ForeignKey(schoolclasses,on_delete=models.CASCADE)
    student = models.ForeignKey(studentsdetail,on_delete=models.CASCADE)

class fees(models.Model):
    enrollstudent = models.ForeignKey(enroll_student,on_delete=models.CASCADE)
    months = models.ForeignKey(months,on_delete=models.CASCADE)
    studentamount = models.IntegerField()

class subjects(models.Model):
    subjectname = models.CharField(max_length=100)
    def __str__(self):
        return self.subjectname


class marks(models.Model):
    subjectname = models.ForeignKey(subjects,on_delete=models.DO_NOTHING)
    enrollstudent = models.ForeignKey(enroll_student,on_delete=models.CASCADE)
    subjectmarks = models.PositiveSmallIntegerField(default=0,null=True)
    
    
class teacherdetail(models.Model):
    t_name = models.CharField(max_length=50)
    t_fname = models.CharField(max_length=50)
    dob = models.DateField()
    m_number = models.CharField(max_length=20)
    s_email = models.CharField(max_length=50)
    date_hiring = models.DateField()
    c_position = models.BooleanField(default=True)
    sex = models.BooleanField(default=True)
    address = models.CharField(max_length=200)
    fm_number = models.CharField(max_length=15)
    salary = models.IntegerField()
    speciality = models.CharField(max_length=200)
    def __str__(self):
        return str(self.t_name)

class teachpaymonths(models.Model):
    years = models.ForeignKey(yearclass,on_delete=models.DO_NOTHING)
    months = models.ForeignKey(months,on_delete=models.DO_NOTHING)
    teacher = models.ForeignKey(teacherdetail,on_delete=models.CASCADE)
    teacheramount = models.IntegerField()




   
