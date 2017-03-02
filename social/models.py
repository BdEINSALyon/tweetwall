from django.db import models


class Provider(models.Model):
    class Meta:
        verbose_name = 'Fournisseur'

    name = models.CharField(max_length=50, verbose_name='nom')

    TWITTER = 'TWI'
    INSTAGRAM = 'INS'
    TYPE_CHOICES = (
        (TWITTER, 'Twitter'),
        (INSTAGRAM, 'Instagram')
    )
    type = models.CharField(max_length=3, choices=TYPE_CHOICES, verbose_name='type')

    app_id = models.CharField(max_length=100, verbose_name="identifiant de l'application")
    app_secret = models.CharField(max_length=200, verbose_name="secret de l'application")

    @property
    def provider_instance(self):
        from social.providers import base, twitter, instagram
        if self.type == Provider.TWITTER:
            return twitter.TwitterProvider(self)
        if self.type == Provider.INSTAGRAM:
            return instagram.InstagramProvider(self)
        else:
            return base.Provider(self)

    def __str__(self):
        return self.get_type_display()


class Feed(models.Model):
    class Meta:
        verbose_name = 'flux'
        verbose_name_plural = 'flux'

    hashtag = models.CharField(max_length=50, verbose_name='hashtag')
    providers = models.ManyToManyField(
        to=Provider,
        related_name='feeds',
        verbose_name='fournisseurs'
    )

    def __str__(self):
        return self.hashtag


class Message(models.Model):
    class Meta:
        verbose_name = 'message'

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    text = models.TextField(blank=True, verbose_name='texte')
    image = models.URLField(max_length=300, blank=True, verbose_name='image')
    video = models.URLField(max_length=300, blank=True, verbose_name='vidéo')
    video_is_gif = models.BooleanField(default=False, verbose_name='la vidéo est un GIF')

    author_name = models.CharField(max_length=50, blank=True, verbose_name="nom de l'auteur")
    author_username = models.CharField(max_length=50, verbose_name="nom d'utilisateur de l'auteur")
    author_picture = models.URLField(max_length=300, blank=True, verbose_name="image de l'auteur")
    published_at = models.DateTimeField(verbose_name='publié le')
    provider = models.ForeignKey(
        to=Provider,
        on_delete=models.CASCADE,
        related_name='messages',
        verbose_name='fournisseur'
    )
    provider_post_id = models.CharField(max_length=20, verbose_name='identifiant du post chez le fournisseur')

    validated_at = models.DateTimeField(blank=True, null=True, verbose_name='validé le')

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
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default=PENDING, verbose_name='statut')

    feed = models.ForeignKey(
        to=Feed,
        on_delete=models.CASCADE,
        related_name='messages',
        verbose_name='flux'
    )

    def __str__(self):
        return self.author_name + ' on ' + str(self.published_at)
