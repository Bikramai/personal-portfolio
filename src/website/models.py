from django.db import models


# Create your models here.
class About(models.Model):
    """
    A model for the about page.
    """
    name = models.CharField(
        max_length=100,
        help_text='Your name'
    )
    contact_no = models.CharField(
        max_length=100,
        help_text='Your contact number'
    )
    email = models.EmailField(
        help_text='Your email address'
    )

    description = models.TextField(
        help_text='A short description about you'
    )
    image = models.ImageField(
        upload_to='about',
        help_text='Your avatar'
    )
    available = models.BooleanField(
        default=True
    )
    experience = models.IntegerField(
        help_text='Your experience'
    )
    projects_completed = models.IntegerField(
        help_text='Number of projects completed'
    )
    happy_clients = models.IntegerField(
        help_text='Number of happy clients'
    )
    fb_link = models.URLField(
        blank=True
    )
    pintrest_link = models.URLField(
        blank=True
    )
    github_link = models.URLField(
        blank=True
    )
    youtube_link = models.URLField(
        blank=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'About'
        verbose_name_plural = 'About'


class Brands(models.Model):
    """
    A model for the brands page.
    """
    name = models.CharField(
        max_length=100
    )
    logo = models.ImageField(
        upload_to='brands',
        help_text='Brands You have collaborated with 50x50 [png]'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'


class Reviews(models.Model):
    """
    A model for the reviews page.
    """
    name = models.CharField(
        max_length=100
    )
    role = models.CharField(
        max_length=100,
        help_text='Reviewers role i.e. CEO, CTO',
    )
    description = models.CharField(
        max_length=500,
        help_text='Your review'
    )
    rating = models.IntegerField(
        help_text='Rating out of 5'
    )
    project_link= models.URLField(
        help_text='Link to the project'
    )


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'


class Awards(models.Model):
    """
    A model for the awards page.
    """

    name = models.CharField(
        max_length=100
    )

    year = models.IntegerField(
        help_text='Year of the award'
    )
    position = models.CharField(
        max_length=100,
        help_text='Position achieved'
    )
    project_link = models.URLField(
        help_text='Link to the project'
    )
    icon = models.ImageField(
        upload_to='awards',
        help_text='Icon of the award 50x50 [png] !important'
    )


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Award'
        verbose_name_plural = 'Awards'

""" HOME -------------------------------------------------------- """

class WorkExperience(models.Model):
    """
    A model for the work experience page.
    """
    organization = models.CharField(
        max_length=100
    )
    organization_image = models.ImageField(
        upload_to='experience',
        help_text='Logo of the organization 50x50 [png]'
    )
    designation = models.CharField(
        max_length=100
    )

    start_year = models.IntegerField(
        help_text='Year of start'
    )
    end_year = models.IntegerField(
        help_text='Year of end'
    )

    def __str__(self):
        return self.organization

    class Meta:
        verbose_name = 'Work Experience'
        verbose_name_plural = 'Work Experience'


class Expertise(models.Model):
    """
    A model for the expertise page.
    """
    skill_name = models.CharField(
        max_length=100
    )
    skill_icon = models.ImageField(
        upload_to='expertise',
        help_text='Icon of the skill 50x50 [png]'
    )

    def __str__(self):
        return self.skill_name

    class Meta:
        verbose_name = 'Expertise'
        verbose_name_plural = 'Expertise'


""" SERVICES -------------------------------------------------------- """
class Services(models.Model):
    """
    A model for the services page.
    """
    name = models.CharField(
        max_length=100
    )
    icon = models.ImageField(
        upload_to='services',
        help_text='Icon of the service [png]'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

class FAQ(models.Model):
    """
    A model for the FAQ page.
    """
    question = models.CharField(
        max_length=100
    )
    answer = models.CharField(
        max_length=100
    )

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = 'FAQ'
        verbose_name_plural = 'FAQ'

""" PROJECTS -------------------------------------------------------- """
from tinymce.models import HTMLField

class Projects(models.Model):
    """
    A model for the projects page.
    """
    name = models.CharField(
        max_length=100
    )
    over_view = models.CharField(
        max_length=700
    )
    description = HTMLField(
        help_text='Description of the project'
    )
    image = models.ImageField(
        upload_to='projects',
        help_text='Screenshot of the project HD'
    )
    project_link = models.URLField(
        help_text='Link to the project'
    )

    client_name = models.CharField(
        max_length=100
    )

    service_provided = models.CharField(
        max_length=100
    )
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'


""" CONTACT ---------------------------------------------------------"""


class ContactMe(models.Model):
    """
    A model for the contact page.
    """
    name = models.CharField(
        max_length=100
    )
    email = models.EmailField(
        max_length=100
    )
    Subject = models.CharField(
        max_length=100
    )

    comment = models.TextField(
        help_text="Descripotion of your Proposal"
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contact'