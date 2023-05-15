"""
TODO: FIX MODULE
"""


from application.infra.frameworks.network_traffic_provider.sockets import SocketIO
from application.infra.ui.rest.web.flask_ui import FlaskUI


UI_INJECTION = FlaskUI()
NETWORK_TRAFFIC_PROVIDER_INJECTION = SocketIO()
