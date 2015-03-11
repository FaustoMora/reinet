from swampdragon import route_handler
from swampdragon.route_handler import ModelPubRouter
from usuarios.models import Notification
from .serializers import NotificationSerializer


class NotificationRouter(ModelPubRouter):
	valid_verbs = ['subscribe']
	route_name = 'notifications'
	model = Notification
	serializer_class = NotificationSerializer

	@login_required(login_url='/ingresar/')
	def subscribe(self, **kwargs):
		id_session=request.session['id_user']
		print "ESTA ES LA SESSION QUE SE USA",id_session
		super().subscribe(**kwargs)

	def get_subscription_contexts(self, **kwargs):
		return {'id_user': self.connection.user.pk}

	route_handler.register(NotificationRouter)
