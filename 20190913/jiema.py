#!/usr/bin/env python
# coding:utf-8
from PIL import Image
import requests
from hashlib import md5

class Chaojiying_Client(object):

    def __init__(self, username, password, soft_id):
        self.username = username
        password =  password.encode('utf8')
        self.password = md5(password).hexdigest()
        self.soft_id = soft_id
        self.base_params = {
            'user': self.username,
            'pass2': self.password,
            'softid': self.soft_id,
        }
        self.headers = {
            'Connection': 'Keep-Alive',
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)',
        }


    def PostPic(self, im, codetype):
        """
        im: 图片字节
        codetype: 题目类型 参考 http://www.chaojiying.com/price.html
        """

        params = {
            'codetype': codetype, # 返回1到4个坐标
        } 
        params.update(self.base_params)
        files = {'userfile': ('captcha1.png', im)}
        r = requests.post('http://upload.chaojiying.net/Upload/Processing.php', data=params, files=files, headers=self.headers)
        return r.json()

    def ReportError(self, im_id):
        """
        im_id:报错题目的图片ID
        """
        params = {
            'id': im_id,
        }
        params.update(self.base_params)
        r = requests.post('http://upload.chaojiying.net/Upload/ReportError.php', data=params, headers=self.headers)
        print(r.json())
        return r.json()






# if __name__ == '__main__':
#     chaojiying = Chaojiying_Client('15872998154', 'qwer66668888', '901519')	#用户中心>>软件ID 生成一个替换 96001
#     # img.open('./')
#     im = open('./captcha1.png', 'rb').read()

#     Image.open('./captcha1.png').show()
#     res_str = chaojiying.PostPic(im, 9004)
#     if res_str['err_no'] == 0:
#         pic_id = res_str['pic_id']
#         pic_str = res_str['pic_str']
#         print(pic_id, pic_str)
#         													#本地图片文件路径 来替换 a.jpg 有时WIN系统须要//
#     print(res_str)												#1902 验证码类型  官方网站>>价格体系 3.4+版 print 后要加()

