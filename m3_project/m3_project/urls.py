from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.shortcuts import render

from m3 import get_app_urlpatterns
from app.actions import extSelectData

def workspace(request):
	"""
	Возвращает view для отображения Рабочего Стола на
	основе шаблона m3

	:param request:
	:return:
	"""
	return render(
			request,
			'm3_workspace.html',
			context={'debug': settings.DEBUG},
	)


urlpatterns = [
	url(r'^admin/', admin.site.urls),
	url(r'^$', workspace),
	url(r'^data/contenttypes',extSelectData)
]
# Собираем шаблоны урлов из app_meta
# подключенных приложений
urlpatterns.extend(get_app_urlpatterns())
