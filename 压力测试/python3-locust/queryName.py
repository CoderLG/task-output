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

    def placeLikeQuery(self,likeName,type):
        self.client.get("/placeservice/api/v1/query/placeName="+likeName,name='placeLikeQuery'+str(type))

#    @task
    def tiltphotoTask(self):
        # 下载瓦片
        with open('csv/tiltphoto/download18.csv', 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                self.tiltDownload(row[0])

    @task
    def placeTask(self):

        # 一个字
        self.placeLikeQuery(chr(random.randint(0x4e00, 0x9fbf)),1)

        # 两个字
        self.placeLikeQuery(chr(random.randint(0x4e00, 0x9fbf))+chr(random.randint(0x4e00, 0x9fbf)),2)


        #三个字以上
        self.placeLikeQuery(chr(random.randint(0x4e00, 0x9fbf)) + chr(random.randint(0x4e00, 0x9fbf))+chr(random.randint(0x4e00, 0x9fbf)), 3)



class UserTaskRunner(HttpLocust):
    task_set = lgTasting
    min_wait = 10
    max_wait = 30
    # stop_timeout = 10
    # wait_time = between(0.0001, 0.0001)





