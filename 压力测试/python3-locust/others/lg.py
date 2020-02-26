import csv
from locust import HttpLocust, TaskSet, task


class lg_tilephotp(TaskSet):
      def multiDownload(self, url,i):
          self.client.get(url, name='MultiDownload'+str(i))

      @task
      def cir(self):
          with open('C:\\Users\\admin\Desktop\\1127\\lg\\tiltphoto_csv\\download18.csv', 'r') as f:
              reader = csv.reader(f)
              i=0
              for row in reader:
                  self.multiDownload(row[0],i)
                  i+=1

class UserTaskRunner(HttpLocust):
    task_set = lg_tilephotp
    min_wait = 10
    max_wait = 30