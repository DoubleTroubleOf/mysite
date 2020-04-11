from django.db import models

# Create your models here.


class Indicator(models.Model):
    #поля класа это поля таблицы в БД
    Month =  models.DecimalField("Месяц", max_digits = 2, decimal_places = 0)
    Year = models.CharField("Год", max_length=4)
    Income = models.DecimalField("Чистый доход",max_digits = 4, decimal_places = 0)
    
    def __str__(self):
        return str(self.Year)+':'+ str(self.Month) + '  ||   ' + str(self.Income)
  
    class Meta:
        #Этот клас для удобства роботы с админ панелью
        verbose_name = "Показатель эффективности"
        verbose_name_plural = "Показатели эффективности"
        
        
"""
После создание модели данных нода 
сделать миграцию БД
"""