from django.db import models
from django.contrib.auth.models import User




BRANCH=[('CIVIL','CIVIL'),('MECH','MECH'),('ELECT','ELECT'),('TEXT','TEXT'),('IT','IT'),('CSE','CSE')]
class TeacherExtra(models.Model):
    id = models.AutoField(primary_key=True)
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    salary = models.PositiveIntegerField(null=False)
    joindate=models.DateField(auto_now_add=True)
    mobile = models.CharField(max_length=40)
    status=models.BooleanField(default=False)
    branch1=models.CharField(max_length=20,choices=BRANCH,default='Select Branch')
    teacher_profile = models.ImageField(upload_to='profile_pic/TeacherProfile_pic/',null=True,blank=True)

   
  
        
    def __str__(self):
        return self.user.first_name
    @property
    def get_id(self):
        return self.user.id
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name


class Country(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name

class State(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    state_name = models.CharField(max_length=30)

    def __str__(self):
        return '%s -%s' % (self.country, self.state_name)

class City(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    city_name = models.CharField(max_length=30)

    def __str__(self):
        return '%s -%s' % (self.state, self.city_name)

class Village(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    village_name = models.CharField(max_length=30)

    def __str__(self):
        return '%s -%s' % (self.city, self.village_name)


classes=[('fy','FY'),('sy','SY'),('ty','TY'),
('btech','BTECH')]
BRANCH=[('Select Branch','Select Branch'),('CIVIL','CIVIL'),('MECH','MECH'),('ELECT','ELECT'),('TEXT','TEXT'),('IT','IT'),('CSE','CSE')]
GENDER=[('male','MALE'),('MALE','FEMALE'),('other','OTHER')]
NATIONALITY=[('INDIAN','Indian')]
CATEGORY = [('Open','OPEN'),('obc','OBC'),('sc','SC'),('st','ST')]
class StudentExtra(models.Model):
    id = models.AutoField(primary_key=True)
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic= models.ImageField(upload_to='profile_pic/StudentProfile_pic/',null=True,blank=True)
    roll = models.CharField(max_length=10)
    mobile = models.CharField(max_length=40,null=True)
    fee=models.PositiveIntegerField(null=True)
    email = models.EmailField()
    gender = models.CharField(max_length=10,choices=GENDER,default='Select')
    branch= models.CharField(max_length=200,choices=BRANCH,default='Select')
    cl= models.CharField(max_length=10,choices=classes,default='one')
    status=models.BooleanField(default=False)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    state= models.ForeignKey(State, on_delete=models.SET_NULL, null=True)
    city= models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
    village= models.ForeignKey(Village, on_delete=models.SET_NULL, null=True)

    

    Nationality = models.CharField(max_length=10,choices=NATIONALITY,default='Select')
    category = models.CharField(max_length=10,choices=CATEGORY,default='Select')

    
    


    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return self.user.first_name



class Attendance(models.Model):
    roll=models.CharField(max_length=10,null=True)
    date=models.DateField()
    cl=models.CharField(max_length=10)
    present_status = models.CharField(max_length=10)



class Notice(models.Model):
    date=models.DateField(auto_now=True)
    by=models.CharField(max_length=20,null=True,default='college')
    message=models.CharField(max_length=500)



class Upload_Document(models.Model):
    student = models.ForeignKey(StudentExtra,on_delete=models.CASCADE,null=True)
    tc = models.FileField(null=True)
    mark10 = models.FileField(null=True)
    mark12 = models.FileField(null=True)
    g_certificate = models.FileField(null=True)
   