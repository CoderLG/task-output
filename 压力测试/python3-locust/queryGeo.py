import csv
from locust import HttpLocust, TaskSet, task, between
import random


class lgTasting(TaskSet):

    def tiltDownload(self, url):
        self.client.get(url, name='tiltDownload')

    def placeGetPccGeometry(self,code):
        self.client.get("/placeservice/api/v1/vectors/district?code="+code+"&returnGeometry=true", name='placeGetPccGeometry')

    def placeCountryGeometry(self,name):
        self.client.post("/placeservice/api/v1/vectors/district/world", json={
            "dataName": name,
            "returnGeometry": "true"
        },name='placeCountryGeometry')

    def placeLikeQuery(self,name,type):
        self.client.get("/placeservice/api/v1/query/placeName="+name,name='placeLikeQuery'+str(type))

#    @task
    def tiltphotoTask(self):
        # 下载瓦片
        with open('csv/tiltphoto/download18.csv', 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                self.tiltDownload(row[0])

    @task
    def placeTask(self):

        index = 1
        #根据唯一标识code 请求省市县geometry
        with open('csv/place/pccCode.csv', 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                if(index == 300):
                    break
                self.placeGetPccGeometry(row[0])
                index = index + 1

        #根据国家名称 请求国家geometry
        with open('csv/place/CountryName.csv', 'r',encoding= 'utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                self.placeCountryGeometry(row[0])



class UserTaskRunner(HttpLocust):
    task_set = lgTasting
    min_wait = 10
    max_wait = 30

    # wait_time = between(0.0001, 0.0001)





