from django.db import models


def upd_rand_name(instance, filename):
    import uuid, os
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('static/images', filename)


class News(models.Model):
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    created = models.DateTimeField(auto_now_add=True)

    title = models.CharField(max_length=200, verbose_name="Заголовок")

    text = models.TextField(verbose_name="Текст")

    image = models.ImageField(
        upload_to=upd_rand_name,
        blank=True,
        verbose_name="Картинка"
    )

    def __str__(self):
        return self.title
