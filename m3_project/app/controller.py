from objectpack.observer import (
	ObservableController,
	Observer,
)
 
observer = Observer()
action_controller = ObservableController(
	url='actions',
	observer=observer,
)
action_controller_aaa = ObservableController(
	url='actionsaaa',
	observer=observer,
)


# @observer.subscribe
# class StarToHash(object):

# 	listen = ['.*/PermiasdasdssionPack/.*']

# 	def prepare_obj(self, obj):
# 		print(obj)
# 		# return obj