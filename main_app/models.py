from django.db import models


class educationalOffering(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.TextField()
    
    def __str__(self):
        return self.name


class degreeProgram(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    educationalOffering = models.ForeignKey('educationalOffering',on_delete=models.CASCADE)
    specializationAvailable = models.BooleanField()

    def __str__(self):
        return self.name

class specialization(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=300)
    degreeProgram = models.ForeignKey('degreeProgram',on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class eligibilityHeader(models.Model):
    id = models.AutoField(primary_key=True)
    heading = models.CharField(max_length=400)
    description = models.TextField(blank=True)
    note = models.TextField(blank=True)
    degreeProgram = models.ForeignKey('degreeProgram',on_delete=models.CASCADE)
    def __str__(self):
       return self.heading

class eligibilityDetails(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.TextField()
    eligibiltyHeader = models.ForeignKey('eligibilityHeader',on_delete=models.CASCADE)

    def __str__(self):
        return self.content

class policy(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=400)
    description = models.TextField()
    def __str__(self):
       return self.name
 
class policyDetail(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.TextField()
    tags = models.CharField(max_length=20)
    def __str__(self):
       return self.content

class refundSteps(models.Model):
    id = models.AutoField(primary_key=True)
    heading = models.CharField(max_length=20)
    description = models.TextField()
    def __str__(self):
       return self.heading

class refundCharges(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.TextField(blank=True)
    def __str__(self):
       return self.content

class acceptancePolicy(models.Model):
    id = models.AutoField(primary_key=True)
    heading = models.CharField(max_length=300,blank=True)
    content = models.TextField()
    educationalOffering = models.ForeignKey('educationalOffering',on_delete=models.CASCADE)

    def __str__(self):
        return self.heading

class nominationConsideration(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.TextField()
    educationalOffering = models.ForeignKey('educationalOffering',on_delete=models.CASCADE)

    def __str__(self):
        return self.content

class newsAndUpdates(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField()
    heading = models.TextField()
    date = models.DateTimeField() 

    def __str__(self):
        return self.heading  


class homeSlider(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField()

    def __str(self):
        return self.image

class gallery(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField()
    date = models.DateField()
    caption = models.CharField(max_length=500)
    
    def __str__(self):
        return self.caption


class visionAndMission(models.Model):
    choices = [
        ('VISION','VISION'),
        ('MISSION','MISSION')
    ]
    id = models.AutoField(primary_key=True)
    image = models.FileField()
    heading = models.CharField(max_length=50)
    content = models.TextField()
    category = models.CharField(max_length=20,choices=choices)

    def __str__(self):
        return self.heading
    

class chancellorMessage(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.FileField()
    name = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.name


class contactQuery(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    contactNumber = models.BigIntegerField()
    country = models.CharField(max_length=100)
    message = models.TextField()
    createDate = models.DateTimeField()

    def __str__(self):
        return self.name
class accreditationParagraph(models.Model):
    id = models.AutoField(primary_key=True)
    heading = models.CharField(max_length=30)
    content = models.TextField()

class accreditationList(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.TextField()


class describingAccreditationParagraph(models.Model):
    id = models.AutoField(primary_key=True)
    heading = models.TextField()
    listAvailable = models.BooleanField()

    def __str__(self):
        return self.heading

class describingAccreditation(models.Model):
    id = models.AutoField(primary_key=True)
    heading = models.ForeignKey('describingAccreditationParagraph',on_delete=models.CASCADE)
    listItem = models.TextField()

    def __str__(self):
        return self.listItem 

class accreditationImportance(models.Model):
    id = models.AutoField(primary_key=True)
    heading = models.CharField(max_length=200)
    content = models.TextField()

class afterGraduationServices(models.Model):
    id = models.AutoField(primary_key=True)
    heading = models.TextField()

class accreditatedCenters(models.Model):
    id = models.AutoField(primary_key=True)
    flag = models.FileField()
    country = models.CharField(max_length=100,blank=True)
    heading = models.CharField(max_length=100,blank=True)
    contactPerson = models.CharField(max_length=300,blank=True)
    phoneNumber = models.CharField(max_length=20,blank=True)  
    address = models.TextField(blank=True)
    email = models.EmailField(blank=True)
    website = models.CharField(max_length=50,blank=True)


    def __str__(self):
        return self.country


class testimonials(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    image = models.FileField()
    designation = models.CharField(max_length=50,blank=True)
    content = models.TextField()


class faculty(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.FileField()
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100,blank=True)
    qualification = models.CharField(max_length=200)
    description = models.TextField()


class thesisPolicy(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=150)
    description = models.TextField()
    attachment = models.FileField()

class academyWorks(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=20)
    icon = models.FileField(blank=True)
    attachment = models.FileField(blank=True)


class gradeTable(models.Model):
    id = models.AutoField(primary_key=True)
    grade = models.CharField(max_length=10)
    description = models.CharField(max_length=200)
    inclusion = models.CharField(max_length=10)

class thesisEvaluation(models.Model):
    id = models.AutoField(primary_key=True)
    criteria = models.CharField(max_length=200)
    hundread = models.TextField()
    ninety = models.TextField()
    eighty = models.TextField()
    seventy = models.TextField()
    fail = models.TextField()


class studentFiles(models.Model):
    id = models.AutoField(primary_key=True)
    heading = models.CharField(max_length=100)
    content = models.TextField()
    def __str__(self):
        return self.content

class mainCampus(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    region = models.CharField(max_length=100,blank=True)
    address = models.CharField(max_length=500,blank=True)
    phone = models.CharField(max_length=20,blank=True)

class academicsCenters(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField()
    name = models.CharField(max_length=100)


class universityOffering(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.TextField()

class educationalModalities(models.Model):
    id = models.AutoField(primary_key=True)
    heading = models.CharField(max_length=50)
    content = models.TextField()

class educationModel(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title
   
class educationalModalContent(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.ForeignKey('educationModel',on_delete=models.CASCADE)
    heading = models.CharField(max_length=50,blank=True)
    content = models.TextField()


class nonDiscriminationPolicy(models.Model):
    id = models.AutoField(primary_key=True)
    heading = models.CharField(max_length=50)
    image = models.FileField()
    content = models.TextField()


class requirementHeader(models.Model):
    id = models.AutoField(primary_key=True)
    heading = models.CharField(max_length=300)
    subHeading = models.CharField(max_length=700, blank=True)
    image = models.FileField()

    def __str__(self):
        return self.heading

class requirementContent(models.Model):
    id = models.AutoField(primary_key=True)
    header = models.ForeignKey('requirementHeader',on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return self.content
