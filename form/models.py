from django.db import models


class Color(models.Model):
    class Meta:
        verbose_name = 'Цвет'
        verbose_name_plural = 'Цвета'

    alias = models.CharField(max_length=30, verbose_name="Название цвета")

    color = models.CharField(
        max_length=20,
        verbose_name="Код цвета \n\nhttps://ru.wikipedia.org/wiki/%D0%A6%D0%B2%D0%B5%D1%82%D0%B0_HTML",
    )

    def __str__(self):
        return self.alias


class BodyShape(models.Model):
    class Meta:
        ordering = ('name',)
        verbose_name = 'Форма корпуса'
        verbose_name_plural = 'Формы корпусов'

    name = models.CharField(max_length=100, db_index=True, verbose_name="Форма корпуса")

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
        verbose_name="Цвета корпуса"
    )

    rosette_colors = models.ManyToManyField(
        Color,
        related_name='rosette_colors',
        verbose_name="Цвета розеток"
    )

    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name


class WireType(models.Model):
    class Meta:
        ordering = ('name',)
        verbose_name = 'Тип кабеля'
        verbose_name_plural = 'Типы кабелей'

    name = models.CharField(max_length=100, db_index=True, verbose_name="Тип кабеля")

    def __str__(self):
        return self.name


class WireLength(models.Model):
    class Meta:
        ordering = ('name',)
        verbose_name = 'Длинна кабеля'
        verbose_name_plural = 'Длинна кабелей'

    name = models.FloatField(max_length=100, verbose_name="Длинна кабеля")

    def __str__(self):
        return f'{self.name}'


class FeedbackForm(models.Model):
    class Meta:
        ordering = ('created',)
        verbose_name = 'Предзаполненная форма обратной связи'
        verbose_name_plural = 'Предзаполненные формы обратной связи'

    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    phone_number = models.CharField(max_length=20, blank=False, verbose_name="Номер телефона")

    first_name = models.CharField(max_length=40, blank=False, verbose_name="Имя")

    body_shape = models.ForeignKey(
        BodyShape,
        related_name="body_shapes",
        on_delete=models.CASCADE,
        default=1,
        verbose_name="Форма корпуса"
    )

    body_color = models.CharField(max_length=10, default="#FFFFFF", verbose_name="Цвет корпуса")

    backlight = models.BooleanField(default=True)

    tire_gilding = models.BooleanField(default=False, verbose_name="Золочение шин")

    usb_ports = models.BooleanField(default=True, verbose_name="USB порты")

    amount_of_rosette = models.PositiveIntegerField(default=9, verbose_name="Количество розеток")

    rosette_color = models.CharField(max_length=10, default="#FFFFFF", verbose_name="Цвет розеток")

    manufacturer = models.ForeignKey(
        Manufacturer,
        related_name="manufacturers",
        on_delete=models.CASCADE,
        blank=True,
        verbose_name="Производитель"
    )

    wire_type = models.ForeignKey(
        WireType,
        related_name="wire_types",
        on_delete=models.CASCADE,
        blank=True,
        verbose_name="Тип кабеля"
    )

    wire_length = models.PositiveIntegerField(
        blank=True,
        verbose_name="Длинна кабеля"
    )

    def __str__(self):
        return str(self.created)


class BillingForm(models.Model):
    class Meta:
        ordering = ('created',)
        verbose_name = 'Форма обратной связи'
        verbose_name_plural = 'Формы обратной связи'

    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    phone_number = models.CharField(max_length=20, verbose_name="Номер телефона")

    first_name = models.CharField(max_length=40, blank=True, verbose_name="Имя")

    def __str__(self):
        return str(self.created)
