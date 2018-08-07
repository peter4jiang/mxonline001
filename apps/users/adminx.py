# _*_ coding: utf-8 _*_
import xadmin
from xadmin import views


class GlobalSettings(object):
    site_title = 'abc'
    site_footer = 'abc'
    menu_style = 'accordion'


xadmin.site.register(views.CommAdminView, GlobalSettings)