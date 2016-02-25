from system.core.controller import *
import json

class Maps(Controller):
    def __init__(self, action):
        super(Maps, self).__init__(action)

        self.load_model('Map')

    def index(self):
        return self.load_view('index.html')

    def show(self):
        ping = self.models['Map'].show_marker()
        print ping
        return jsonify(ping=ping)


    def translate(self):
        regis_info = {'street': request.form['street'],'city': request.form['city'],'state': request.form['state'],'zip': request.form['zip']}


        url = "https://maps.googleapis.com/maps/api/geocode/json?address="+regis_info['street']+ regis_info['city']+regis_info['state']+regis_info['zip']+"&key=AIzaSyCXADpD0abRZfFzCJo5_LA8ChMnap7Zsp8"

        response = requests.get(url).content
        # print 'THIS IS THE RESPONSE'
        points = json.loads(response)
        
        address = points['results'][0]['formatted_address']
        lat_pos = points['results'][0]['geometry']['location']['lat']
        lng_pos = points['results'][0]['geometry']['location']['lng']
        # going to give us the information of this location
        # res = json.loads(response)
        # print 'THIS IS RES'
        # print res
        # print response['results'][0]['formatted_address']
        inputvalues = {"address": address,"lat": lat_pos,"lng": lng_pos}
        self.models['Map'].create_new_address(inputvalues)

        return redirect('/')





