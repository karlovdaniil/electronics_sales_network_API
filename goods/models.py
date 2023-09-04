from django.db import models


class Contact(models.Model):

    email = models.EmailField(verbose_name='email', null=True, blank=True, unique=True)
    country = models.CharField(verbose_name='Страна', max_length=50, null=True, blank=True)
    city = models.CharField(verbose_name='Город', max_length=50, null=True, blank=True)
    street = models.CharField(verbose_name='Улица', max_length=50, null=True, blank=True)
    house_number = models.CharField(verbose_name='Номер дома', max_length=5, null=True, blank=True)

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'

    def __str__(self):
        return self.email


class Good(models.Model):

    title = models.CharField(verbose_name='Название товара', max_length=255)
    model = models.CharField(verbose_name='Модель', max_length=50, null=True, blank=True)
    release_date = models.DateField(verbose_name='Дата выхода продукта на рынок', null=True, blank=True)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.title


class Supplier(models.Model):

    class SupplierType(models.IntegerChoices):
        Factory = 0, 'Завод'
        retail_network = 1, 'Розничная сеть'
        individual_entrepreneur = 2, 'Индивидуальный предприниматель'

    name = models.CharField(verbose_name='Поставщик', max_length=100)
    type = models.PositiveSmallIntegerField(
        verbose_name='Тип поставщика', choices=SupplierType.choices, default=SupplierType.Factory
    )

    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'

    def __str__(self):
        return self.name


class RetailNetwork(models.Model):

    title = models.CharField(verbose_name='Название', max_length=255, unique=True)
    contact = models.ForeignKey(Contact, verbose_name='Контакт', on_delete=models.PROTECT, null=True, blank=True)
    good = models.ForeignKey(Good, verbose_name='Товар', on_delete=models.PROTECT, null=True, blank=True)
    supplier = models.ForeignKey(Supplier, verbose_name='Поставщик', on_delete=models.PROTECT, null=True, blank=True)
    accounts_receivable = models.DecimalField(
        verbose_name='Дебиторская задолженность', max_digits=20, decimal_places=2, default=0
    )
    created = models.DateTimeField(verbose_name='Время создания', auto_now_add=True)

    class Meta:
        verbose_name = 'Розничная сеть'
        verbose_name_plural = 'Розничные сети'
