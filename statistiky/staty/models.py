from django.core.validators import MinValueValidator
from django.db import models
from django.urls import reverse


class Druh(models.Model):
    oznaceni_druhu = models.CharField(max_length=50, unique=True, verbose_name="Označení druhu hráče",
                            help_text='Zadejte text o maximální délce 50 znaků; text musí být jedinečný')
    OBLAST = (
        ('Levé křídlo', 'Levé křídlo'),
        ('Pravé křídlo', 'Pravé křídlo'),
        ('Brankář', 'Brankář' ),
        ('Centr', 'Centr'),
        ('Obrana', 'Obrana'),
    )
    oblast = models.CharField(max_length=40, choices=OBLAST, blank=True, default='Centr', verbose_name="Oblast", help_text='Vyberte označení oblasti')

    class Meta:
        ordering = ["oznaceni_druhu"]
        verbose_name = 'Druh hráče'
        verbose_name_plural = 'Druh hráče'

    def __str__(self):
        return f"{self.oznaceni_druhu}, {self.oblast}"


class Statistiky(models.Model):
    jmeno = models.CharField(max_length=30, verbose_name="Jméno Hráče", help_text='Zadejte jméno maximální délce 30 znaků')
    prijmeni = models.CharField(max_length=30, verbose_name="Příjmení Hráče", help_text='Zadejte příjmení maximální délce 30 znaků')
    popis = models.TextField(blank=True, null=True, verbose_name="Rychlý životopis")
    vyplata = models.IntegerField(validators=[MinValueValidator(1)], null=True, help_text="Zadejte nezáporné číslo", verbose_name="Výplata")
    KVALITA= (
        (10, '10'),
        (9, '9'),
        (8, '8'),
        (7, '7'),
        (6, '6'),
        (5, '5'),
        (4, '4'),
        (3, '3'),
        (2, '2'),
        (1, '1'),
    )
    kvalita = models.IntegerField( choices=KVALITA, blank=True, default=5, verbose_name="Kvalita hráče", help_text='Vyberte označení kvality')
    foto = models.ImageField(upload_to='staty/%Y/%m/%d/', blank=True, null=True, verbose_name="Profilovka")
    druh = models.ForeignKey(Druh, on_delete=models.RESTRICT)

    class Meta:
        ordering = ["prijmeni"]
        verbose_name = 'staty'
        verbose_name_plural = 'staty'

    def __str__(self):
        return f"{self.jmeno}"

    def get_absolute_url(self):
        """Metoda vrací URL stránky, na které se vypisují podrobné informace o zboží"""
        return reverse('detail', args=[str(self.id)])
