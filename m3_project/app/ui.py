from objectpack.ui import BaseEditWindow, ModelEditWindow
from m3_ext.ui import all_components as ext
from django.contrib.contenttypes.models import ContentType
from m3_ext.ui.misc import ExtDataStore
from m3_ext.ui.fields import ExtCheckBox, ExtDateField
class UserAddEditWindow(BaseEditWindow):

	def _init_components(self):
		"""
		Здесь следует инициализировать компоненты окна и складывать их в
		:attr:`self`.
		"""
		super(UserAddEditWindow, self)._init_components()

		self.field__name = ext.ExtStringField(
			label=u'username',
			name='username',
			allow_blank=False,
			anchor='100%')
		self.field__password = ext.ExtStringField(
			label=u'password',
			name='password',
			allow_blank=False,
			anchor='100%')
		self.field__first_name = ext.ExtStringField(
			label=u'first_name',
			name='first_name',
			allow_blank=True,
			anchor='100%')
		self.field__last_name = ext.ExtStringField(
			label=u'last_name',
			name='last_name',
			allow_blank=True,
			anchor='100%')
		self.field__email = ext.ExtStringField(
			label=u'email',
			name='email',
			allow_blank=True,
			anchor='100%')
		self.field__is_superuser = ExtCheckBox(
			label=u'is_superuser',
			name='is_superuser',
			anchor='100%',
			)
		self.field__is_staff = ExtCheckBox(
			label=u'is_staff',
			name='is_staff',
			anchor='100%',
			)
		self.field__last_login = ExtDateField(
			name='last_login',
			label=u'last_login',
			format='d.m.yy',
			)
		self.field__date_joined = ExtDateField(
			name='date_joined',
			label=u'date_joined',
			format='d.m.yy',
			)

	def _do_layout(self):
		"""
		Здесь размещаем компоненты в окне
		"""
		super(UserAddEditWindow, self)._do_layout()
		self.form.items.extend((
			self.field__name,
			self.field__password,
			self.field__first_name,
			self.field__last_name,
			self.field__email,
			self.field__is_superuser,
			self.field__is_staff,
			self.field__last_login,
			self.field__date_joined,
		))

	def set_params(self, params):
		"""
		Установка параметров окна

		:params: Словарь с параметрами, передается из пака
		"""
		super(UserAddEditWindow, self).set_params(params)
		self.height = 'auto'


class PermissionCTAddEditWindow(ModelEditWindow):

	def _init_components(self):
		"""
		Здесь следует инициализировать компоненты окна и складывать их в
		:attr:`self`.
		"""
		super(PermissionCTAddEditWindow, self)._init_components()

		self.field__content_type_id = ext.ExtDictSelectField(
			url='/data/contenttypes',
			label=u'content_type_id',
			name='content_type_id',
			allow_blank=False,
			anchor='100%')
	def _do_layout(self):
		"""
		Здесь размещаем компоненты в окне
		"""
		super(PermissionCTAddEditWindow, self)._do_layout()
		self.form.items.extend((
			self.field__content_type_id,
		))

	def set_params(self, params):
		"""
		Установка параметров окна

		:params: Словарь с параметрами, передается из пака
		"""
		super(PermissionCTAddEditWindow, self).set_params(params)
		self.height = 'auto'

