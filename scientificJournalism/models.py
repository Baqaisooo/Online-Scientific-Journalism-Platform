from django.db import models
from django.urls import reverse
from passlib.hash import pbkdf2_sha256
from django.core.validators import FileExtensionValidator


GENDER_EN = (
    ('MALE','male'),
    ('FEMALE','female')
)

GENDER_AR = (
    ('MALE','ذكر'),
    ('FEMALE','أنثى')
)

ACCOUNT_STATUS_EN = (
    ('ONLINE','online'),
    ('FREEZE','freeze')
)

ACCOUNT_STATUS_AR = (
    ('ONLINE','نشط'),
    ('FREEZE','مجمد')
)

PACKAGE_STATUS_EN = (
    ('ACTIVE','active'),
    ('INACTIVE','inactive'),
    # ('FREEZE','freeze'),
)

PACKAGE_STATUS_AR = (
    ('ACTIVE','نشط'),
    ('INACTIVE','غير نشط'),
    # ('FREEZE','مجمد'),
)

SUBSCRIPTION_STATUS_EN = (
    ('ACTIVE','active'),
    ('INACTIVE','inactive'),
)

SUBSCRIPTION_STATUS_AR = (
    ('ACTIVE','نشط'),
    ('INACTIVE','غير نشط'),
)

ARTICLE_STATUS_EN = (
    ('REJECTED', 'rejected'),
    ('SUBMITTED','submitted'),
    ('ASSIGNED','assigned'),
    ('REVIEWED','reviewed'),
    ('FINAL_REVIEWED','final_reviewed'),
    ('WITH_REVIEWER','with reviewer'),
    # ('APOLOGIZED','apologized'),
    ('ONLINE','online'),
    ('EDITORIAL','editorial'),
    ('ARCHIVED','archived'),
)

ARTICLE_STATUS_AR = (
    ('REJECTED', 'مرفوض'),
    ('SUBMITTED','عند رئيس التحرير'),
    ('ASSIGNED','تحت التحرير'),
    ('REVIEWED','تمت مراجعته'),
    ('FINAL_REVIEWED','تمت المراجعة النهائية'),
    ('WITH_REVIEWER','عند المراجعين'),
    # ('APOLOGIZED','معتذر'),
    ('ONLINE','منشور'),
    ('EDITORIAL','افتتاحية'),
    ('ARCHIVED','مؤرشف'),
)

ARTICLE_TYPE = (
    ('VIDEO','video'),
    ('AUDIO','audio'),
    ('IMAGE','image'),
    ('TEXT','text'),
)

ARTICLE_FIELD_EN = (
    ('HEALTH','health'),
    ('IT','Information Technology'),
    ('ECOLOGY','Ecology'),
    ('ORGANISMS','Organisms'),
    ('NATURE','Nature and the universe'),
    ('CHEMICAL','Chemicals'),
    ('MATH','Math'),
    ('ENGINEERING','Engineering')
)

ARTICLE_FIELD_AR = (
    ('HEALTH','الصحة'),
    ('IT','تقنية المعلومات'),
    ('ECOLOGY','البيئة'),
    ('ORGANISMS','الحياة'),
    ('NATURE','الكون و الطبيعة'),
    ('CHEMICAL','الكيميائيات'),
    ('MATH','الرياضيات'),
    ('ENGINEERING','هندسيات')
)

DECISION = (
    ('ACCEPT','accept'),
    ('REJECT','reject')
)

REVIEW_DECISION = (
    ('ACCEPT','accept'),
    ('APOLOGIZE','apologize'),
)



class User(models.Model):

    user_ID = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length = 15)
    last_name = models.CharField(max_length = 15)
    birthdate = models.DateField(auto_now = False,auto_now_add = False)
    gender_en = models.CharField(max_length = 6, choices = GENDER_EN)
    gender_ar = models.CharField(max_length = 6, choices = GENDER_AR)
    email = models.EmailField(max_length = 40, unique=True)
    phone_number = models.BigIntegerField()
    country = models.CharField(max_length = 30)
    city = models.CharField(max_length = 20)
    activation = models.CharField(max_length=10, blank = True, null = True)
    
    class Meta:
        verbose_name_plural = 'User'
    
    def __str__(self):
        return '%i : %s %s' % (self.user_ID, self.first_name, self.last_name)

    # def get_absolute_url(self):
    #     return reverse(" `namespace`:urlname", kwargs={"pk": self.pk})
    

#-----------------------------------------------------------------------------------------#

class EBM (models.Model):

    EBM_ID = models.ForeignKey(
        'User',
        on_delete = models.CASCADE
    )
    password = models.CharField(max_length = 256)
    specialty_en = models.CharField(max_length = 20, choices = ARTICLE_FIELD_EN)
    specialty_ar = models.CharField(max_length = 20, choices = ARTICLE_FIELD_AR)
    account_status_en = models.CharField(max_length = 7, choices = ACCOUNT_STATUS_EN)
    account_status_ar = models.CharField(max_length = 7, choices = ACCOUNT_STATUS_AR)

    class Meta:
        verbose_name_plural = 'Editorial Board Member'
                 
    def __str__(self):
        return str(self.EBM_ID)

    def verify_password(self, raw_password):
        return pbkdf2_sha256.verify(raw_password, self.password)
        
    # def get_absolute_url(self):
    #     return reverse(" `namespace`:urlname", kwargs={"pk": self.pk})

#-----------------------------------------------------------------------------------------#

class Reviewer(models.Model):

    reviewer_ID = models.ForeignKey(
        'User',
        on_delete = models.CASCADE
    )
    password = models.CharField(max_length = 256)
    specialty_en = models.CharField(max_length = 20, choices = ARTICLE_FIELD_EN)
    specialty_ar = models.CharField(max_length = 20, choices = ARTICLE_FIELD_AR)
    workplace = models.CharField(max_length = 50)
    account_status_en = models.CharField(max_length = 7, choices = ACCOUNT_STATUS_EN)
    account_status_ar = models.CharField(max_length = 7, choices = ACCOUNT_STATUS_AR)
    
    class Meta:
        verbose_name_plural = 'Reviewer'
                
    def __str__(self):
        return str(self.reviewer_ID)
        
    def verify_password(self, raw_password):
        return pbkdf2_sha256.verify(raw_password, self.password)
        
    # def get_absolute_url(self):
    #     return reverse(" `namespace`:urlname", kwargs={"pk": self.pk})

#-----------------------------------------------------------------------------------------#

class Associate_Editor(models.Model):

    AE_ID = models.ForeignKey(
        "EBM",
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name_plural = 'Associate Editor'

    def __str__(self):
        return str(self.AE_ID)
    
        
    # def get_absolute_url(self):
    #     return reverse(" `namespace`:urlname", kwargs={"pk": self.pk})

#-----------------------------------------------------------------------------------------#

class Editor_in_Chief(models.Model):

    EIC_ID = models.ForeignKey(
        "EBM",
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name_plural = 'Editor in Chief'

    def __str__(self):
        return str(self.EIC_ID)

    # def get_absolute_url(self):
    #     return reverse(" `namespace`:urlname", kwargs={"pk": self.pk})

#-----------------------------------------------------------------------------------------#

# class Guest(models.Model):

#     Guest_ID = models.ForeignKey(
#         "User",
#         on_delete=models.CASCADE
#     )
#     special_number = models.BigIntegerField()

#     class Meta:
#         verbose_name_plural = 'Guest'
        
#     def __str__(self):
#         return str(self.Guest_ID)

    # def get_absolute_url(self):
    #     return reverse(" `namespace`:urlname", kwargs={"pk": self.pk})

#-----------------------------------------------------------------------------------------#

class Subscriber(models.Model):

    subscriber_ID = models.ForeignKey(
        'User',
        on_delete = models.CASCADE
    )
    password = models.CharField(max_length = 256)
    picture = models.ImageField(upload_to='writer_&_subscribers_pic/%Y/%m/%d')

    class Meta:
        verbose_name_plural = 'Subscriber'

    def __str__(self):
        return str(self.subscriber_ID)
        
    def verify_password(self, raw_password):
        return pbkdf2_sha256.verify(raw_password, self.password)
        
    # def get_absolute_url(self):
    #     return reverse(" `namespace`:urlname", kwargs={"pk": self.pk})

#-----------------------------------------------------------------------------------------#

class Admin(models.Model):

    admin_ID = models.ForeignKey(
        'User',
        on_delete = models.CASCADE
    )
    password = models.CharField(max_length=256)

    class Meta:
        verbose_name_plural = 'Admin'

    def __str__(self):
        return str(self.admin_ID)
    
    def verify_password(self, raw_password):
        return pbkdf2_sha256.verify(raw_password, self.password)
        
        
    # def get_absolute_url(self):
    #     return reverse(" `namespace`:urlname", kwargs={"pk": self.pk})

#-----------------------------------------------------------------------------------------#

class Setting(models.Model):

    article_price = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name='article price(S.R.)')
    online_duration = models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='online duration(days)')
    editorial_duration = models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='editorial duration(days)')


    class Meta:
        verbose_name_plural = 'Setting'

    # def get_absolute_url(self):
    #     return reverse(" `namespace`:urlname", kwargs={"pk": self.pk})

#-----------------------------------------------------------------------------------------#

class Writer(models.Model):

    writer_ID = models.ForeignKey("User", on_delete=models.CASCADE)
    password = models.CharField(max_length = 256)
    specialty_en = models.CharField(max_length = 20, choices = ARTICLE_FIELD_EN)
    specialty_ar = models.CharField(max_length = 20, choices = ARTICLE_FIELD_AR)
    workplace = models.CharField(max_length = 50)
    account_status_en = models.CharField(max_length = 7, choices = ACCOUNT_STATUS_EN, default='FREEZE')
    account_status_ar = models.CharField(max_length = 7, choices = ACCOUNT_STATUS_AR, default='FREEZE')
    picture = models.ImageField(upload_to='writer_&_subscribers_pic/%Y/%m/%d')

    class Meta:
        verbose_name_plural = ("Wirter")
                
    def __str__(self):
        return str(self.writer_ID)
        
    def verify_password(self, raw_password):
        return pbkdf2_sha256.verify(raw_password, self.password)
        
    # def get_absolute_url(self):
    #     return reverse(" `namespace`:urlname", kwargs={"pk": self.pk})

#-----------------------------------------------------------------------------------------#
 
# class Credit_Card(models.Model):

#     credit_card_ID = models.BigAutoField(primary_key=True)
#     user_ID = models.ForeignKey("User", on_delete=models.CASCADE)
#     credit_card_number = models.BigIntegerField()
#     name_on_card = models.CharField( max_length=30)
#     expiration_date = models.CharField(max_length=5)
    
#     class Meta:
#         verbose_name_plural = "Credit Card"
                
#     def __str__(self):
#         return str(self.user_ID)
        
    # def get_absolute_url(self):
    #     return reverse(" `namespace`:urlname", kwargs={"pk": self.pk})

#-----------------------------------------------------------------------------------------#

class Package(models.Model):

    package_ID = models.BigAutoField(primary_key=True)
    admin_ID = models.ForeignKey("Admin", on_delete=models.CASCADE)
    package_name_en = models.CharField(max_length=50)
    package_name_ar = models.CharField(max_length=50)
    pakage_description_en = models.TextField()
    pakage_description_ar = models.TextField()
    duration = models.PositiveIntegerField() # calculated as number of months
    price = models.DecimalField(max_digits=6, decimal_places=2)
    package_status_en = models.CharField(max_length=10, choices = PACKAGE_STATUS_EN, default = 'INACTIVE')
    package_status_ar = models.CharField(max_length=10, choices = PACKAGE_STATUS_AR, default = 'INACTIVE')

    class Meta:
        verbose_name_plural = ("Package")
            
    def __str__(self):
        return str(self.package_ID) + ' : '+ self.package_name_ar
    
    # def get_absolute_url(self):
    #     return reverse(" `namespace`:urlname", kwargs={"pk": self.pk})

#-----------------------------------------------------------------------------------------#

class Subscription(models.Model):

    subscription_ID = models.BigAutoField(primary_key=True)
    package_ID = models.ForeignKey("Package", on_delete=models.CASCADE)
    subscriber_ID = models.ForeignKey("Subscriber", on_delete=models.CASCADE)
    subscription_status_en = models.CharField(max_length=10, choices=SUBSCRIPTION_STATUS_EN)
    subscription_status_ar = models.CharField(max_length=10, choices=SUBSCRIPTION_STATUS_AR)
    start_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Subscription"

    # def get_absolute_url(self):
    #     return reverse(" `namespace`:urlname", kwargs={"pk": self.pk})

#-----------------------------------------------------------------------------------------#

class Article (models.Model):
    
    article_ID = models.BigAutoField(primary_key=True)
    writer_ID = models.ForeignKey("Writer", on_delete=models.CASCADE)
    type = models.CharField(max_length=7, choices=ARTICLE_TYPE)
    field_en = models.CharField(max_length=30, choices=ARTICLE_FIELD_EN)
    field_ar = models.CharField(max_length=30, choices=ARTICLE_FIELD_AR)
    cover_image = models.ImageField(upload_to="Cover Articles Images/%Y/%m/%d")
    title_ar = models.CharField(max_length=50, blank = True, null = True)
    title_en = models.CharField(max_length=50, blank = True, null = True)
    brief_of_article_en = models.TextField(blank = True, null = True)
    brief_of_article_ar = models.TextField(blank = True, null = True)
    context_en = models.TextField(blank=True, null = True)
    context_ar = models.TextField(blank=True, null = True)
    submit_date = models.DateTimeField(auto_now_add=True)
    article_status_en = models.CharField(max_length=15, choices=ARTICLE_STATUS_EN, default='SUBMITTED')
    article_status_ar = models.CharField(max_length=15, choices=ARTICLE_STATUS_AR, default='SUBMITTED')
    price = models.BooleanField(default = False) 
    is_editorial = models.BooleanField(default = False)
    publishing_date = models.DateTimeField(blank=True, null = True, auto_now=False, auto_now_add=False)
    number_of_views = models.IntegerField(default=0)


    class ArticleMeta:
        verbose_name_plural = ("Article")

    def __str__(self):
        return '%i : %s' % (self.article_ID, self.title_ar)
    
    # def get_absolute_url(self):
    #     return reverse(" `namespace`:urlname", kwargs={"pk": self.pk})

#-----------------------------------------------------------------------------------------#
import datetime
import random
def multimedia_directory_path(instance, filename):
    extention = ''
    for letter in reversed(filename):
        if (letter == '.'):
            break
        extention = letter + extention
    
    images_extentions = ['jpeg','jpg','png','gif']
    audios_extentions = ['mp3']
    videos_extentions = ['mp4']
    
    now = datetime.datetime.now()

    filename = str(random.randrange(1000000000000000,9999999999999999))+'.'+extention

    if extention.lower() in images_extentions:
        return 'images/{}/{}/{}/{}'.format(now.year, now.month, now.day, filename)

    if extention.lower() in audios_extentions:
        return 'audios/{}/{}/{}/{}'.format(now.year, now.month, now.day, filename)

    if extention.lower() in videos_extentions:
        return 'videos/{}/{}/{}/{}'.format(now.year, now.month, now.day, filename)

class Multimedia(models.Model):

    ID = models.BigAutoField(primary_key=True)
    aritcle_ID = models.ForeignKey("Article", on_delete=models.CASCADE)
    format = models.CharField(max_length=7, choices=ARTICLE_TYPE)
    content = models.FileField(upload_to= multimedia_directory_path, blank=True, null=True)
    # url_content = models.URLField( max_length=200, blank=True, null=True)


    class Meta:
        verbose_name_plural = "Multimedia"

    def __str__(self):
        return str(self.aritcle_ID)


    # def get_absolute_url(self):
    #     return reverse(" `namespace`:urlname", kwargs={"pk": self.pk})

#-----------------------------------------------------------------------------------------#

class Comment(models.Model):

    comment_ID = models.BigAutoField(primary_key=True)
    subscriber_ID = models.ForeignKey("Subscriber", on_delete=models.CASCADE)
    article_ID = models.ForeignKey("Article", on_delete=models.CASCADE)
    comment_date = models.DateTimeField(auto_now_add=True)
    comment_content = models.TextField()

    class Meta:
        verbose_name_plural = "Comment"

    def __str__(self):
        return str(self.comment_content)

    # def get_absolute_url(self):
    #     return reverse(" `namespace`:urlname", kwargs={"pk": self.pk})

#-----------------------------------------------------------------------------------------#

class Rate(models.Model):

    rate_ID = models.BigAutoField(primary_key=True, verbose_name='rating ID')
    subscriber_ID = models.ForeignKey("Subscriber", on_delete=models.CASCADE)
    article_ID = models.ForeignKey("article", on_delete=models.CASCADE)
    subscriber_rating = models.IntegerField()

    class Meta:
        verbose_name_plural = "Rating"

    # def get_absolute_url(self):
    #     return reverse(" `namespace`:urlname", kwargs={"pk": self.pk})

#-----------------------------------------------------------------------------------------#

class Purchase(models.Model):

    purchase_ID = models.AutoField(primary_key=True)
    article_ID = models.ForeignKey("Article", on_delete=models.CASCADE)
    # guest_ID = models.EmailField(max_length=50)
    purchase_date = models.DateTimeField(auto_now_add=True)
    # price = models.DecimalField(max_digits=6, decimal_places=2)
    download_code = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Purchase"

    # def get_absolute_url(self):
    #     return reverse(" `namespace`:urlname", kwargs={"pk": self.pk})

#-----------------------------------------------------------------------------------------#

class Feedback(models.Model):

    feedback_ID = models.BigAutoField(primary_key=True)
    EIC_ID = models.ForeignKey("Editor_in_Chief", verbose_name="Editor in Chief ID", on_delete=models.CASCADE)
    writer_ID = models.ForeignKey("Writer", on_delete=models.CASCADE)
    article_ID = models.ForeignKey("article", on_delete=models.CASCADE)
    EIC_comment = models.TextField(verbose_name="Editor in Chief Comment", blank=True, null=True)
    final_decision = models.CharField(max_length=7, choices=DECISION)

    class Meta:
        verbose_name_plural = "Editor in Chief Feedback"

    # def get_absolute_url(self):
    #     return reverse(" `namespace`:urlname", kwargs={"pk": self.pk})

#-----------------------------------------------------------------------------------------#

class Article_Revision(models.Model):

    article_revision_ID = models.BigAutoField(primary_key=True)
    AE_ID = models.ForeignKey("Associate_Editor", verbose_name="Associate Editor", on_delete=models.CASCADE)
    article_ID = models.ForeignKey("Article", on_delete=models.CASCADE)
    EIC_ID = models.ForeignKey("Editor_in_Chief", verbose_name="Editor in Chief ID", on_delete=models.CASCADE)
    reviewer_ID = models.ForeignKey("Reviewer", on_delete=models.CASCADE, blank=True, null=True)
    assign_date = models.DateTimeField(auto_now_add=True)
    AE_comment = models.TextField(verbose_name="Associate Editor Comment", blank=True, null=True)
    invite_date = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
    R_comment = models.TextField(verbose_name='Reviewer Comment', blank=True, null=True)
    AE_recommendation = models.CharField(max_length=7, verbose_name='Associate Editor Recommendation', choices=DECISION, blank=True, null=True)
    # AE_decision = models.CharField(max_length=10, verbose_name='Associate Editor Decision To Review', choices=REVIEW_DECISION, blank=True, null=True)
    # R_decision = models.CharField(max_length=10, verbose_name='Reviewer Decision To Review', choices=REVIEW_DECISION, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Article_Revision"

    # def get_absolute_url(self):
    #     return reverse(" `namespace`:urlname", kwargs={"pk": self.pk})
