from django.db import models
# from django.contrib.auth.models import AbstractUser

# class User(AbstractUser):
#     name = models.CharField(max_length=100, blank=True, null=True)
#     phone = models.PositiveIntegerField(max_length=13, blank=True, null=True)
#

class Artifact(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)
    date_posted =  models.DateTimeField(auto_now_add=True, null=True)
    image = models.ImageField(upload_to = 'photos/', null = True)
    price = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    is_sold = models.BooleanField(default=False)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)


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
        images = Artifact.objects.all()
        return images


class Comment(models.Model):
    # user = models.ForeignKey(User,on_delete=models.CASCADE)
    artifact = models.ForeignKey(Artifact,on_delete=models.CASCADE)
    date_posted =  models.DateTimeField(auto_now_add=True, null=True)
    comment = models.TextField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.artifact.name

    @classmethod
    def get_comments(cls,artifact_id):
        comments_list = Comment.objects.filter(artifact=artifact_id)

        return comments_list

    @classmethod
    def flag_comment(cls,artifact_id):
        comment = Comment.objects.get(pk=artifact_id)

        return comment

    # @classmethod
    # def edit_comment(cls,artifact_id):
    #     comment = Comment.objects.get(pk=artifact_id)
    #     comment.update(comment)
                    
    #     return comment

    @classmethod
    def delete_comment(cls,artifact_id):
        comment = Comment.objects.get(pk=artifact_id)
                    
        return comment