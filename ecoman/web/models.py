from django.db import models

def get_ecoin(telegram_id):
    foydalanuvchi=Foydalanuvchi.objects.get(telegram_id=telegram_id)
    posts=foydalanuvchi.post.all().filter(tasdiq=True)
    foydalanuvchi.ecoin=posts.count()
    foydalanuvchi.save()
    
    return foydalanuvchi.ecoin


class Foydalanuvchi(models.Model):
    telegram_id=models.IntegerField(default=0)
    ism=models.CharField(max_length=255,blank=True,null=True)
    phone=models.IntegerField(default=0,blank=True,null=True)
    city=models.CharField(max_length=255,blank=True,null=True)
    ecoin=models.IntegerField(default=0)
    res_step=models.IntegerField(default=0)
    add=models.IntegerField(default=0)

    def __str__(self):
        get_ecoin(self.telegram_id)
        return str(self.telegram_id)
    
class Post(models.Model):
    foydalanuvchi=models.ForeignKey(Foydalanuvchi,related_name="post",on_delete=models.CASCADE)
    image=models.URLField(editable=False)
    tasdiq=models.BooleanField(default=False)
    added_date=models.DateTimeField(auto_now_add=True)

    def image_tag(self):
        from django.utils.html import mark_safe
        return mark_safe('<img src="%s" width="200" style="border:solid 1px" />' % (self.image))
    image_tag.short_description = 'Image'
    image_tag.allow_tags = True

    def save(self,*args, **kwargs):
        get_ecoin(self.foydalanuvchi.telegram_id)
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.foydalanuvchi.ism} {self.tasdiq}"
