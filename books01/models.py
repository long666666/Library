"""
数据表：
    1、出版社
    2、作者：与详细一对一
    3、作者详细表
    4、书：与出版社多对一
    5、作者、书、出版社对应表
"""

from django.db import models


# --------------------------出版社---------------------------------
class Publisher(models.Model):
    name = models.CharField(max_length=32)
    addr = models.CharField(max_length=128)
    phone = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = "publisher"


# ---------------------------作者---------------------------------=
class Author(models.Model):
    name = models.CharField(max_length=16)
    # 作者和详情一对一
    introduce = models.CharField(max_length=128)
    book = models.ManyToManyField(to="book")
    def __str__(self):
        return self.name

    class Meta:
        db_table = "author"


# -----------------------------------书--------------------------------
class book(models.Model):
    title = models.CharField(max_length=16)
    price = models.DecimalField(max_digits=5, decimal_places=2)  # 5位数字，保留两位小数

    # auto_now = True 每一次修改都自动更新时间
    # auto_now_add = True  第一次创建时自动填写时间
    # publisher_day = models.DateField(auto_now_add=True,auto_now=True) #二选一
    publisher_day = models.DateField(auto_now_add=True)
    # 书和出版社是多对一
    publisher = models.ForeignKey(to="Publisher", on_delete=models.CASCADE)  # 多对一(models.ForeignKey)
    introduction = models.CharField(max_length=128)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "book"
