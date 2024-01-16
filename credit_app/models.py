from django.db import models


class Base(models.Model):
    
    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создано")


class Producer(Base):
    
    class Meta:
        verbose_name = "Производитель"
        verbose_name_plural = "Производители"
    
    def __str__(self):
        return self.name
    
    name = models.CharField(max_length=255, verbose_name="Производитель")


class Product(Base):
    
    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
    
    def __str__(self):
        return self.name
    
    name = models.CharField(max_length=255, verbose_name="Товар")
    producer = models.ForeignKey(
        Producer, on_delete=models.CASCADE, related_name="products"
    )
    

class Contract(Base):
        
    class Meta:
        verbose_name = "Контракт"
        verbose_name_plural = "Контракты"
    
    def __str__(self):
        return self.number
    
    # CONTRACT-LZ1223KH-17/01/2024
    number = models.CharField(
        max_length=255, unique=True, verbose_name="Номер контракта"
    )


class LoanApplication(Base):
    
    class Meta:
        verbose_name = "Кредитная заявка"
        verbose_name_plural = "Кредитные заявки"
    
    def __str__(self):
        return self.number
    
    # LOAN-LZ1223KH-17/01/2024
    number = models.CharField(
        max_length=255, unique=True, verbose_name="Номер кредитной заявки"
    )
    
    contract = models.OneToOneField(
        Contract, on_delete=models.CASCADE, related_name="loan_application"
    )
    products = models.ManyToManyField(
        Product, related_name="loan_applications"
    )
