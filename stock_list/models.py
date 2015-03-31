from django.db import models

# Create your models here.
class moneycontrol(models.Model):
    COMPANY = models.CharField(primary_key=True, max_length=80)
    LTP = models.FloatField(max_length=10)
    Change_I = models.CharField(max_length=7)
    VOLUME = models.IntegerField(max_length=10)
    BUY_PRICE = models.FloatField(max_length=7)
    SELL_PRICE = models.FloatField(max_length=7)
    BUY_QTY = models.FloatField(max_length=7)
    SELL_QTY = models.FloatField(max_length=7)
    date = models.DateField()
    time = models.DateTimeField()
    class Meta:
        db_table = "money_control"