from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):

    USER_TYPE_CHOICES = (
        ('A', 'Admin'),
        ('M', 'Moderator'),
        ('S', 'Seller'),
        ('B', 'Buyer'),
    )

    user = models.OneToOneField(User, related_name='users',unique=True, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to = 'profile/', default='profile/default.jpg')
    date_joined =  models.DateTimeField(auto_now_add=True, null=True)
    phone_number = models.CharField(max_length=14, blank=True, null=True)
    user_type = models.CharField(max_length=1, choices=USER_TYPE_CHOICES, null=True, default='B')

    def __str__(self):
        return self.user.username
    

@receiver(post_save, sender=User)
def create_user_profile(sender, **kwargs):
# def create_user_profile(sender, instance, created, **kwargs):
    if kwargs['created']:
        UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_user_profile, sender=User)



class Category(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)
   
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name
    
    
    @classmethod
    def get_categories(cls):
        categories = Category.objects.all()
        return categories




class Artifact(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)
    date_posted =  models.DateTimeField(auto_now_add=True, null=True)
    image = models.ImageField(upload_to = 'photos/',  null = True)
    price = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    auction_price = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    is_sold = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)


    class Meta:
        ordering = ['-date_posted']

    def __str__(self):
    	return self.name

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def get_images(cls):
        images = cls.objects.all()
        return images

    @classmethod
    def get_images_by_category(cls, category_id):
        images = cls.objects.filter(category = category_id)
        return images

    @classmethod
    def single_artifact(cls, artifact_id):
        artifact = cls.objects.get(id=artifact_id)
        return artifact

    @classmethod
    def search_by_name(cls,search_term):
        query = cls.objects.filter(name__icontains=search_term)
        return query


class Comment(models.Model):
    posted_by = models.ForeignKey(User,on_delete=models.CASCADE, blank=True, null=True)
    artifact = models.ForeignKey(Artifact,on_delete=models.CASCADE, blank=True, null=True)
    date_posted =  models.DateTimeField(auto_now_add=True, null=True)
    comment = models.TextField(max_length=200, blank=True, null=True)
    is_flagged = models.BooleanField(default=False)

    def __str__(self):
        return self.artifact.name

    @classmethod
    def get_comments(cls, artifact_id):
        comments_list = cls.objects.filter(artifact=artifact_id)

        return comments_list

    @classmethod
    def flag_comment(cls, artifact_id):
        comment = cls.objects.get(pk=artifact_id)
        comment.is_flagged = True
        comment.save()


    @classmethod
    def delete_comment(cls, artifact_id):
        comment = cls.objects.get(pk=artifact_id)
                    
        return comment

class Bid(models.Model):
    bid_price = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    artifact = models.ForeignKey(Artifact,on_delete=models.CASCADE, blank=True, null=True)
    bidder = models.ForeignKey(User,on_delete=models.CASCADE, blank=True, null=True)



# testing the abstract concepts and saving
class ContactInfo(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    
    class Meta:
        abstract = True

class Customer(ContactInfo):
    purchase_history = models.CharField(max_length=10, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)

class Staff(ContactInfo):
    bio = models.TextField()
    position = models.CharField(max_length=20)