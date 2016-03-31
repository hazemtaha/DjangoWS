# encoding: utf-8
from __future__ import unicode_literals
from django.contrib.auth.admin import User
from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator



class Post(models.Model):

	uid=models.ForeignKey(User ,on_delete=models.CASCADE);
	body=models.TextField()
	def __unicode__(self):
		return self.uid


class App (models.Model):
	app_name=models.CharField(max_length=255)
	uri=models.URLField(max_length=255)
	devID=models.ForeignKey(User ,on_delete=models.CASCADE);
	clientID=models.IntegerField();

	secretKey=models.IntegerField();
	#rec_id=models.ForeignKey(Users ,default=1)



class AccessToken(models.Model):
	
	appID=models.ForeignKey(App ,on_delete=models.CASCADE);
	uid=models.ForeignKey(User ,on_delete=models.CASCADE);
	exp_date=models.DateField();
	refreshToken=models.IntegerField(null=True,blank=True);



class Code(models.Model):
	
	appID=models.ForeignKey(App ,on_delete=models.CASCADE);
	uid=models.ForeignKey(User ,on_delete=models.CASCADE);
	code=models.IntegerField();

