# import time
#
# from locust import HttpLocust, TaskSet, task
#
# import random
# import string
# import json
# import base64
#
#
# class UserOperator:
#
#     pubkey = None
#
#     def __init__(self, client):
#         self.client = client
#
#
#     def getUserToken(self, username, passwd):
#         rep = self.userLogin(username, passwd)
#         if (rep.status_code == 200):
#             return json.loads(rep.content)['token']
#         return ''
#
#
#     def getAdminToken(self):
#         return self.getUserToken('admin', 'icenter')
#
#     def getAdminRequestHeader(self):
#         token = self.getAdminToken()
#         headers = {'Authorization': token}
#         return headers
#
#     def createUser(self, username):
#         password = self.encryptPassword(username)
#         rep = self.client.post("/user/api/v1/users", json = {
#             'baseRoles': [],
#             'userInfo': {
#                 'username': username,
#                 'password': password
#             }
#         }, headers=self.getAdminRequestHeader(), name="create user")
#
#     def getUserIdByName(self, username):
#         rep = self.client.get('/user/api/v1/user/userinfo/' + username, headers=self.getAdminRequestHeader(), name='getUserInfo')
#         if (rep.status_code == 200):
#             userInfo = json.loads(rep.content)
#             return userInfo['userInfo']['id']
#         return - 1
#
#     def deleteUserByName(self, username):
#         userId = self.getUserIdByName(username)
#         if (userId == -1):
#             pass
#         else:
#             self.client.delete('/user/api/v1/users/' + str(userId), headers=self.getAdminRequestHeader(), name='delete user')
#
# def userLogin(self, username, passwd):
#     password = self.encryptPassword(passwd)
#     return self.client.post("/api/auth/jwt/token", json={"username": username, "password": password}, name='login')
#
#     def getUserInfo(self, token):
#         return self.client.get('/user/api/v1/user/userinfo', headers = {'Authorization': token}, name = 'getuserinfo')
#
#     @classmethod
#     def loadPubKey(cls):
#         with open('./user_login_public_key.pem', 'r') as f:
#             cls.pubkey = rsa.PublicKey.load_pkcs1_openssl_pem(f.read())
#
#
#     @classmethod
#     def encryptPassword(cls, passwd):
#         enctyptBytes = rsa.encrypt(passwd, cls.pubkey)
#         return base64.b64encode(enctyptBytes)
#
#
# class UserLoginTask(TaskSet):
#
#     def on_start(self):
#         self.userOp = UserOperator(self.client)
#         self.username = "".join(random.sample(string.ascii_letters, random.randint(5, 10)))
#         print 'begin create user: ' + self.username
#         self.userOp.createUser(self.username)
#         print 'end create user: ' + self.username
#
#     def on_stop(self):
#         self.userOp.deleteUserByName(self.username)
#
#     @task
#     def login(self):
#         self.userOp.userLogin(self.username, self.username)
#
#
# class UserGetStatusTask(TaskSet):
#
#     def on_start(self):
#         self.userOp = UserOperator(self.client)
#         self.username = "".join(random.sample(string.ascii_letters, random.randint(5, 10)))
#         self.userOp.createUser(self.username)
#         self.userToken = self.userOp.getUserToken(self.username, self.username)
#         print self.userToken
#
#     def on_stop(self):
#         self.userOp.deleteUserByName(self.username)
#
#     @task
#     def getStatus(self):
#         self.userOp.getUserInfo(self.userToken)
#
# class UserTaskRunner(HttpLocust):
#     task_set = UserGetStatusTask
#     min_wait = 10
#     max_wait = 30
#
#     def setup(self):
#         UserOperator.loadPubKey()
#
# class DataManagerTest(TaskSet):
#     # Server import rate test
#
#     def fileImport(self):
#         info = self.client.post("/datamanager/api/v1/server/fileImport",
#                                 json={"filePath": "/home/iCenter/data/import-data/111/1.zip",
#                                       "destPath": "/home/iCenter/data/service-data/datamanager/dir/0/aa",
#                                       "fileType": "other", "parentId": "1", "status": "2"}, name='ServerImport')
#         jsonb = info.json()
#         self.client.delete("/datamanager/api/v1/folders",
#                            json={"ids": [jsonb['id']]}, name='DeleteFile')
#         self.client.delete(
#             "/datamanager/api/v1/test2?path=/home/iCenter/data/service-data/datamanager/realfile/8f64eb4b9917114a0ca2405cd58e7ee7_1.zip&MD5=8f64eb4b9917114a0ca2405cd58e7ee7",
#             name='DeleteRealFile')
#         return ""
#
#     # Multi-user download test
#     @task
#     def multiDownload(self):
#         self.client.get("/datamanager/api/v1/files/" + str(18952) + "/download", name='MultiDownload')
#         return ""
#
#     # Single user local upload test
#
#
#     def singleUpload(self):
#         for i in range(0, 448):
#             self.client.post(
#                 "/datamanager/api/v1/files/upload?wholeMd5=b27e98fd19fe8e2923000ab6d6a44128&start=0&end=5242880&chunks=448&chunk=" + str(
#                     i),
#                 files={'file': open('F:\\b27e98fd19fe8e2923000ab6d6a44128\\' + str(i) + '_448.part', 'rb')},
#                 name='UploadChuck_' + '%03d' % i)
#
#         self.client.post(
#             "/datamanager/api/v1/files/mergeChunks",
#             json={"md5": "b27e98fd19fe8e2923000ab6d6a44128",
#                   "name": "TRIPLESAT_1_PMS_"+time.strftime('%H:%M:%S',time.localtime(time.time()))+".zip", "ext": "zip",
#                   "createTime": "2019-10-25T06:40:59.529Z", "size": "2344909809", "type": "application/octet-stream",
#                   "parentId": -1, "fileType": "originalImage"},
#             name='MergeChunks')
#         return ""
#     # @task
#     # def test(self):
#     #     self.client.post('', files={'test': open('', 'rb')})
#
#
# # requests
#
# class UserTaskRunner(HttpLocust):
#     task_set = DataManagerTest
#     min_wait = 10
#     max_wait = 30
#
#     # def setup(self):
#     #     UserOperator.loadPubKey()
#
#
# # if __name__ == '__main__':
# #     print time.strftime('%H:%M:%S',time.localtime(time.time()))
