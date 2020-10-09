import requests
from pprint import pprint

"""
https://yandex.ru/dev/disk/rest/

"""
class YaDiskFolders():
    URL='https://cloud-api.yandex.net'
    RESOURSE='/v1/disk/resources'
    # взял с полигона
    TOKEN='AgAAAAAEjRl2AADLWxu9VDr8q0N4sZ1GeLmmCtI'

    def __init__(self):
        pass


    #вызов внешнего API выносим в отдельную функцию - для удобства тестирования
    def make_request(self, folder_name):
        path={'path': f'/{folder_name}'}
        header={'Authorization': YaDiskFolders.TOKEN}

        resp=requests.put(YaDiskFolders.URL+YaDiskFolders.RESOURSE,params=path,headers=header)
        return resp


    # функция создания папки на Yandex Disk
    def create_folder(self, folder_name):

        # запрос к API
        resp=self.make_request(folder_name)

        if resp.status_code == 201:
            return [resp.reason, folder_name]
        else:
            return ['Ошибка!', resp.text]


#my_disk=YaDiskFolders()
#res=my_disk.create_folder('2020-10-07-5')
#pprint(res)



