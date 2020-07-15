from __future__ import absolute_import

from django.conf.urls import url

from objectpack import desktop

from . import actions
from . import controller


def register_urlpatterns():
	"""
	Регистрация конфигурации урлов для приложения
	"""
	return [url(*controller.action_controller.urlpattern),url(*controller.action_controller_aaa.urlpattern)]


def register_actions():
	"""
	регистрация экшенов
	"""
	controller.action_controller_aaa.packs.extend([
		actions.UserPack(),
		actions.GroupPack(),
		# actions.ContentTypeChoosePack(),
	])
	controller.action_controller.packs.extend([
		actions.PermissionPack(),
		actions.ContentTypePack(),
	])


def register_desktop_menu():
	"""
	регистрация элеметов рабочего стола
	"""
	desktop.uificate_the_controller(
		controller.action_controller,
		menu_root=desktop.MainMenu.SubMenu(u'рас')
	)
	desktop.uificate_the_controller(
		controller.action_controller_aaa,
		menu_root=desktop.MainMenu.SubMenu(u'два')
	)