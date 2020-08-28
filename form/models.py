from django.db import models


class Color(models.Model):
    class Meta:
        verbose_name = 'Цвет'
        verbose_name_plural = 'Цвета'

    alias = models.CharField(max_length=30)

    color = models.CharField(max_length=20)

    def __str__(self):
        return self.alias


class BodyShape(models.Model):
    class Meta:
        ordering = ('name',)
        verbose_name = 'Форма корпуса'
        verbose_name_plural = 'Формы корпусов'

    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name


class Manufacturer(models.Model):
    class Meta:
        ordering = ('name',)
        verbose_name = 'Производитель'
        verbose_name_plural = 'Производители'

    body_colors = models.ManyToManyField(
        Color,
        related_name='body_colors',
    )

    rosette_colors = models.ManyToManyField(
        Color,
        related_name='rosette_colors',
    )

    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name


class WireType(models.Model):
    class Meta:
        ordering = ('name',)
        verbose_name = 'Тип кабеля'
        verbose_name_plural = 'Типы кабелей'

    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name


class FeedbackForm(models.Model):
    class Meta:
        ordering = ('created',)
        verbose_name = 'Предзаполненная форма обратной связи'
        verbose_name_plural = 'Предзаполненные формы обратной связи'

    created = models.DateTimeField(auto_now_add=True)

    phone_number = models.CharField(max_length=20)

    first_name = models.CharField(max_length=40)

    body_shape = models.ForeignKey(
        BodyShape,
        related_name="body_shapes",
        on_delete=models.CASCADE,
        default=1
    )

    body_color = models.CharField(max_length=10, default="#FFFFFF")

    backlight = models.BooleanField(default=True)

    tire_gilding = models.BooleanField(default=False)

    usb_ports = models.BooleanField(default=True)

    amount_of_rosette = models.PositiveIntegerField(default=9)

    rosette_color = models.CharField(max_length=10, default="#FFFFFF")

    rosette_manufacturer = models.ForeignKey(
        Manufacturer,
        related_name="manufacturers",
        on_delete=models.CASCADE,
        blank=True
    )

    wire_type = models.ForeignKey(
        WireType,
        related_name="wire_types",
        on_delete=models.CASCADE,
        blank=True
    )

    wire_length = models.PositiveIntegerField(blank=True)


class BillingForm(models.Model):
    class Meta:
        ordering = ('created',)
        verbose_name = 'Форма обратной связи'
        verbose_name_plural = 'Формы обратной связи'

    created = models.DateTimeField(auto_now_add=True)

    phone_number = models.CharField(max_length=20)

    first_name = models.CharField(max_length=40, blank=True)
