from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from cms.models import CMSPlugin


class RSSPlugin(CMSPlugin):
    TEMPLATES = [(value, label) for value, label in
                           getattr(settings, 'CMS_RSS_PLUGIN_TEMPLATES', ())]

    count = models.IntegerField(default=6, verbose_name=_("Number of Entries"))
    title = models.CharField(max_length=200, default="Community News", null=True, blank=True,
                             help_text=_("If you specify this value, it will replace feed's title"))
    rss_url = models.CharField(max_length=512)
    open_in_new_window = models.BooleanField(default=False)
    cache_time = models.IntegerField(verbose_name=_("Cache time in seconds"))
    template = models.CharField(max_length=100, blank=True, default='',
                                                            choices=TEMPLATES)

    def __unicode__(self):
        return self.title
