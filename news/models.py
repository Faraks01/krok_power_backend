from django.db import models


class News(models.Model):
    class Meta:
        ordering = ('created',)
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    created = models.DateTimeField(auto_now_add=True)

    title = models.CharField(max_length=200)

    text = models.CharField(max_length=800)

    # image = models.ImageField(
    #     upload_to=upd_rand_name,
    #     blank=True
    # )

    def __str__(self):
        return self.title
