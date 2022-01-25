import requests
import json

class Capsules:
    def __init__(self, dict):
        self.reuse_count = dict['reuse_count']
        self.water_landings = dict['water_landings']
        self.land_landings = dict['land_landings']
        self.last_update = dict['last_update']
        self.launches = dict['launches']
        self.serial = dict['serial']
        self.status = dict['status']
        self.tipe = dict['type']
        self.id = dict['id']

    def __str__(self) -> str:
        return f'Capsula {self.id}, Serial {self.serial}, Tipo {self.tipe} - Participou dos lançamentos: {self.launches}, reutilizado {self.reuse_count} vezes, pousou {self.water_landings} vezes na água e {self.land_landings} em terra - Última atualização: {self.last_update}'
    
    def get_all_capsules():
        response = requests.get('https://api.spacexdata.com/v4/capsules')
        r = response.json()
        try:
            for i in r:
              yield Capsules(i)
              return i
        except:
            raise

    def get_upcoming_capsule():
        response = requests.get('https://api.spacexdata.com/v3/capsules/upcoming')
        r = response.json()
        try:
            for i in r:
              yield Capsules(i)
        except:
            raise

    def get_past_capsule():
        response = requests.get('https://api.spacexdata.com/v3/capsules/past')
        r = response.json()
        try:
            for i in r:
              yield Capsules(i)
        except:
            raise
    
    def get_info_capsule(id):
        try:
            response = requests.get('https://api.spacexdata.com/v4/capsules/%s' % id)
            r = response.json()
            return Capsules(r)
        except:
            return("")

class Company:
    def __init__(self, dict):
        self.headquarters = dict['headquarters']
        self.links = dict['links']
        self.name = dict['name']
        self.founder = dict['founder']
        self.founded = dict['founded']
        self.employees = dict['employees']
        self.vehicles = dict['vehicles']
        self.launch_sites = dict['launch_sites']
        self.test_sites = dict['test_sites']
        self.ceo = dict['ceo']
        self.cto = dict['cto']
        self.coo = dict['coo']
        self.cto_propulsion = dict['cto_propulsion']
        self.valuation = dict['valuation']
        self.summary = dict['summary']
        self.id = dict['id']
    
    def get_info_company():
        response = requests.get('https://api.spacexdata.com/v4/company')
        r = response.json()
        yield Company(r)

class Launches(Capsules):
    def __init__(self, data):
        print("Construindo objeto...")
        self.fairings = data['fairings']
        self.links = data['links']
        self.static_fire_date_utc = data['static_fire_date_utc']
        self.static_fire_date_unix = data['static_fire_date_unix']
        self.net = data['net']
        self.window = data['window']
        self.rocket = data['rocket']
        self.success = data['success']
        self.failures = data['failures']
        self.details = data['details']
        self.crew = data['crew']
        self.ships = data['ships']
        self.capsules = data['capsules']
        #self.capsules.append(super().get_info_capsule(self.data['capsules']))
        self.payloads = data['payloads']
        self.launchpad = data['launchpad']
        self.flight_number = data['flight_number']
        self.name = data['name']
        self.date_utc = data['date_utc']
        self.date_unix = data['date_unix']
        self.date_local = data['date_local']
        self.date_precision = data['date_precision']
        self.upcoming = data['upcoming']
        self.cores = data['cores']
        self.auto_update = data['auto_update']
        self.tbd = data['tbd']
        self.launch_library_id = data['launch_library_id']
        self.id = data['id']

    def get_latest_launch():
        response = requests.get('https://api.spacexdata.com/v4/launches/latest')
        r = response.json()
        return Launches(r)
