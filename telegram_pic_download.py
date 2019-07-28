from telethon import TelegramClient,sync
import os
import socks #如果你不需要通过代理连接Telegram，可以删掉这一行
from telethon.tl.types import InputMessagesFilterPhotos

# =============需要被替换的值=================
'''
api_id 你的api id
api_hash 你的api hash
channel_link 要下载图片的频道链接
proxy 将localhost改成代理地址,1080改成代理端口
picture_storage_path 图片下载到的路径
'''

api_id = 80xxxxx
api_hash = "3066c1322d6931a85470xxxxxx"
channel_link = "https://t.me/xx"
proxy =(socks.SOCKS5,"0.0.0.0",1080) #不需要代理的话删掉该行
picture_storage_path = "/"
# ==========================================
client = TelegramClient('my_session',api_id=api_id,api_hash=api_hash).start()
    
photos = client.get_messages(channel_link,None,max_id=100000,min_id=0, filter=InputMessagesFilterPhotos)
    
total = len(photos)
index = 0
for photo in photos:
#    filename = picture_storage_path + "/" +str(photo.text)+"_"+str(photo.id) + ".jpg" #名字_id
    filename = picture_storage_path + "/" +str(photo.id) + ".jpg"
    index = index + 1
    print("downloading:", index, "/", total, " : ", filename)
    if  os.path.exists(filename)==False:
        client.download_media(photo, filename)
        print('done!')
    else:
        print('exist!')
client.disconnect()
print("Done.")
