from django.db import models

class RadarBaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    modified_at = models.DateTimeField(auto_now=True, verbose_name="Last Modified At")


class Category(models.Model):
    name = models.CharField(max_length=255)
    keywords = models.CharField(max_length=255)
    weight = models.IntegerField()

    def __unicode__(self):
        return self.name


class Source(models.Model):
    name = models.CharField(max_length=255)
    url = models.URLField()

    def __unicode__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name


class LeadStatus(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name


class Lead(RadarBaseModel):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category)
    source = models.ForeignKey(Source)
    source_url = models.URLField()
    status = models.ForeignKey(LeadStatus)
    tags = models.ManyToManyField(Tag)
    blurb = models.TextField()
    rating = models.IntegerField()
    opportunity = models.BooleanField()
    def __unicode__(self):
        return self.name

class Industry(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name

class Company(RadarBaseModel):
    name = models.CharField(max_length=255)
    industry = models.ForeignKey(Industry)
    website = models.URLField(blank=True, null=True, default=None)
    linkedin = models.URLField(blank=True, null=True, default=None)
    email = models.EmailField(blank=True, null=True, default=None)
    phone = models.CharField(max_length=255, blank=True, null=True, default=None)

    def __unicode__(self):
        return self.name

class CompanyContact(RadarBaseModel):
    name = models.CharField(max_length=255)
    works_at = models.ForeignKey(Company, related_name="works_at")
    linkedin = models.URLField(blank=True, null=True, default=None)
    email = models.EmailField(blank=True, null=True, default=None)
    phone = models.CharField(max_length=255, blank=True, null=True, default=None)

    def __unicode__(self):
        return "%s > %s" % (self.works_at, self.name)
