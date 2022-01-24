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
