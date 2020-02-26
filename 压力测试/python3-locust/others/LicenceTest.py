from locust import HttpLocust, TaskSet, task
import random

class LicenceTask(TaskSet):

    modules = [
        'datamanager',
        'geodata',
        'tilecache',
        'placeservice',
        'geoiot',
        'tilebuilder',
        'tiltphoto',
        'streetview',
        'systemmanager',
        'webmanager',
        'geoserverplus'
    ]

    @task
    def getStatus(self):
        module = random.choice(self.modules)
        self.client.get('/api/v1/licence/status', params = {'productName': 'icenter_112', 'moduleName': module}, name = 'getStatus')


class LicenceTaskRunner(HttpLocust):
    task_set = LicenceTask