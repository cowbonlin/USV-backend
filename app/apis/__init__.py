from .vehicle import VehicleAPI
# from .mission import MissionAPI

def add_all_resources(api):
    api.add_resource(VehicleAPI, '/vehicle/', '/vehicle/<int:vid>')
    # api.add_resource(MissionAPI, '/mission/', '/mission/<int:mid>')
