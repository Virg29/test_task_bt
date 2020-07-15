from objectpack.actions import ObjectPack
from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType
from objectpack.ui import ModelEditWindow
from . import ui
from . import controller
from django import http
from m3_ext.ui.misc import ExtDataStore
from m3_ext.ui.windows import ExtDictionaryWindow
from m3_ext.ui.fields import ExtDictSelectField




class UserPack(ObjectPack):

	model = User

	add_to_menu = True

	add_to_desktop = True

	edit_window = add_window = ui.UserAddEditWindow

class GroupPack(ObjectPack):

	model = Group

	add_to_menu = True

	add_to_desktop = True

	edit_window = add_window = ModelEditWindow.fabricate(model)

class PermissionPack(ObjectPack):

	model = Permission

	add_to_menu = True

	add_to_desktop = True

	PermissionPackModelEditWindow = ui.PermissionCTAddEditWindow.fabricate(
		model,
		field_list=['name', 'codename'],
		model_register=controller.observer,
	)

	edit_window = add_window = PermissionPackModelEditWindow

class ContentTypePack(ObjectPack):

	model = ContentType

	add_to_menu = True

	add_to_desktop = True

	edit_window = add_window = ModelEditWindow.fabricate(model)


def extSelectData(request):
	window = ExtDictionaryWindow(title=u'ahahahah hvatit',mode=1)
	window.init_grid_components()
	window.width = 500
	window.height = 400
	window.grid.add_column(header=u'id', data_index='content_type_id')
	window.grid.add_column(header=u'name', data_index='model')
	print(ContentType.objects.values('id','model'))
	res = []
	for obj in ContentType.objects.values('id','model'):
		v,k = obj.values()
		res.append([v,k])
	print(res)
	window.grid.set_store(ExtDataStore(res))
	window.column_name_on_select = 'content_type_id'
	return http.HttpResponse(window.get_script())

