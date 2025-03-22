from datetime import timezone
from django.utils.translation import gettext_lazy as _
from django.db import models
from core.abstract.models import AbstractManager,AbstractModel

# Create your models here.
class PostManager(AbstractManager):
    pass
class Post(AbstractModel):
    # 📝 Basic Content
    title = models.CharField(max_length=255, verbose_name=_("Title"))
    content = models.TextField(verbose_name=_("Content"), blank=True, null=True)
    
    # 🖼️ Media Files
    image = models.ImageField(upload_to="posts/images/", blank=True, null=True)
    video = models.FileField(upload_to="posts/videos/", blank=True, null=True)
    file = models.FileField(upload_to="posts/files/", blank=True, null=True)

    # 👤 User Relationship
    author = models.ForeignKey(to='core_user.User', on_delete=models.CASCADE, related_name="posts")

    # 🏷️ Tags & Categories
    tags = models.ManyToManyField("Tag", blank=True)
    category = models.ForeignKey("Category", on_delete=models.SET_NULL, null=True, blank=True)

    # 📆 Timestamps
    published_at = models.DateTimeField(blank=True, null=True)

    # 🔢 Status & Meta
    is_edited = models.BooleanField(default=False)
    is_published = models.BooleanField(default=False)
    views_count = models.PositiveIntegerField(default=0)
    likes_count = models.PositiveIntegerField(default=0)

    objects = PostManager()

    def update_likes_count(self):
        # Update the likes_count based on the number of users who liked the post
        self.likes_count = self.liked_by.count()
        self.save()
    def increment_views_count(self):
        self.views_count += 1
        self.save()
    
    class Meta:
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.is_published and not self.published_at:
            self.published_at = timezone.now()  # Set published_at when post is published
        super().save(*args, **kwargs)
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.name
