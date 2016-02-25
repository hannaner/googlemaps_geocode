
from system.core.router import routes

routes['default_controller'] = 'Maps'
# routes['POST']['/directions'] = 'Maps#get_directions'


#the route to give back the lat/long information

# routes['/locations'] = 'Maps#show"'

routes['POST']['/testform'] = 'Maps#translate'

routes['/view'] = 'Maps#show'