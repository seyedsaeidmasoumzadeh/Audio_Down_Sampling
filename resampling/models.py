# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Audio(models.Model):
    audio_name = models.CharField(max_length=200)
    audio_file = models.FileField(upload_to="audio")