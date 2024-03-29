from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Group(models.Model):
    """Group of post."""
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.title


class Post(models.Model):
    """Post which user create."""
    text = models.TextField(
        verbose_name='Текст поста',
        help_text="Текст нового поста"
    )
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts'
    )
    group = models.ForeignKey(
        Group,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='posts',
        verbose_name='Группа',
        help_text="Группа, к которой будет относиться пост"
    )

    class Meta:
        ordering = ("-pub_date",)

    def __str__(self):
        if len(self.text) >= 16:
            return self.text[:13] + '...'
        return self.text
