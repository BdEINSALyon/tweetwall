from django.db import models


class Provider(models.Model):
    name = models.CharField(max_length=50)

    TWITTER = 'TWI'
    INSTAGRAM = 'INS'
    TYPE_CHOICES = (
        (TWITTER, 'Twitter'),
        (INSTAGRAM, 'Instagram')
    )
    type = models.CharField(max_length=3, choices=TYPE_CHOICES)

    app_id = models.CharField(max_length=100)
    app_secret = models.CharField(max_length=200)


class Feed(models.Model):
    hashtag = models.CharField(max_length=50)
    providers = models.ManyToManyField(
        to=Provider,
        related_name='feeds'
    )


class Message(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    text = models.TextField()
    image = models.URLField(max_length=300)
    video = models.URLField(max_length=300)
    video_is_gif = models.BooleanField(default=False)

    author_name = models.CharField(max_length=50)
    author_username = models.CharField(max_length=50)
    author_picture = models.URLField(max_length=300)
    published_at = models.DateTimeField()
    provider = models.ForeignKey(
        to=Provider,
        on_delete=models.CASCADE,
        related_name='messages'
    )
    provider_post_id = models.CharField(max_length=20)

    validated_at = models.DateTimeField()

    PENDING = 'PE'
    PUBLISHED = 'PU'
    PROMOTED = 'PR'
    REJECTED = 'RE'

    STATUS_CHOICES = (
        (PENDING, 'En attente'),
        (PUBLISHED, 'Publié'),
        (PROMOTED, 'Promu'),
        (REJECTED, 'Rejeté')
    )
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default=PENDING)

    feed = models.ForeignKey(
        to=Feed,
        on_delete=models.CASCADE,
        related_name='messages'
    )
