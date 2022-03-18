#python3
# -*- coding=utf-8
import time
from PIL import ImageGrab
from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client
import sys
import logging
import os

logging.basicConfig(level=logging.INFO, stream=sys.stdout)
secret_id = 'AKID4OXR6WgaEdmfLlwrXx72i8IEuMYUAdrp'     # 替换为用户的 SecretId，请登录访问管理控制台进行查看和管理，https://console.cloud.tencent.com/cam/capi
secret_key = 'kFUUEixwf8MK3Ypqc8RWLuDH5dvylJbp'   # 替换为用户的 SecretKey，请登录访问管理控制台进行查看和管理，https://console.cloud.tencent.com/cam/capi
region = 'ap-nanjing'      # 替换为用户的 region，已创建桶归属的region可以在控制台查看，https://console.cloud.tencent.com/cos5/bucket
                           # COS支持的所有region列表参见https://cloud.tencent.com/document/product/436/6224
token = None               # 如果使用永久密钥不需要填入token，如果使用临时密钥需要填入，临时密钥生成和使用指引参见https://cloud.tencent.com/document/product/436/14048  # 指定使用 http/https 协议来访问 COS，默认为 https，可不填
scheme = 'https'
config = CosConfig(Region=region, SecretId=secret_id, SecretKey=secret_key, Token=token, Scheme=scheme)
client = CosS3Client(config)
#proxies = {
 #   'http': 'proxy.huawei.com:8080',  # 替换为用户的 HTTP代理地址
#}
##client = CosS3Client(config)
#创建文件夹
myabsPath = os.path.abspath('.')
path = [x for x in os.listdir('.') if os.path.isdir(x)]
	# print(path)
if 'png' in path:
		#print('yes')
	pass
else:
	#print('no')
		#创建目录
	pngPath = os.path.join(myabsPath,'png')
	os.mkdir(pngPath)
#截屏
def Screenshot():
	nowtime = time.strftime('%Y_%m_%d_%H_%M_%S',time.localtime(time.time()))
	print(nowtime)
	im = ImageGrab.grab()
	im.save(r'png\%s.png' %(nowtime))
	response = client.upload_file(
		Bucket='s5-1310269866',
		LocalFilePath= 'local.txt',
		Key="1111",
		PartSize=1,
		MAXThread=10,
		EnableMD5=False
		)
	print(response['ETag'])

	os.remove(r'png\%s.png' %(nowtime))
while True:    
	print("已截图至'png'")
	Screenshot()
	print("\n")
	time.sleep(int(count))