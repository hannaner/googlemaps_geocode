from system.core.model import Model

class Map(Model):
  def __init__(self):
    super(Map, self).__init__()


  def create_new_address(self, geo_info):
  	# query = "INSERT INTO googlemaptest (address, lat, lng, created_at, updated_at) VALUES (%s, %s, %s, NOW(), NOW())".format(geo_info['address'],geo_info['lat'],geo_info['lng'])

  	query = "INSERT INTO googlemaptest (address, lat, lng, created_at, updated_at) VALUES (%s, %s, %s, NOW(), NOW())"
  	data = [geo_info['address'], geo_info['lat'], geo_info['lng']]

  	return self.db.query_db(query, data)


  # def addresses(self):
  # 	query = "SELECT * FROM addresses WHERE id = %s "

  # 	info = self.db.query_db(query)
  # 	return {'info' : info[0]}

  def show_marker(self):
  	# changed 'select lat, lng' to 'select *'
  	# grab full address to display in window
  	query = "SELECT * FROM googlemaptest"
  	return self.db.query_db(query)




