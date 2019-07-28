## Telegram_Pic_download
电报图片批量下载


环境: python3

依赖: Telethon,PySocks

### 使用方法:

https://my.telegram.org/apps 获取api-id以及api-hash

修改脚本变量

运行（首次运行脚本需要输入tg所绑定的手机号和验证码）

其他：关于Telethon的文档在这里： https://telethon.readthedocs.io/en/latest/

### 去掉重复文件（MD5比值）
···
并获取tg/目录下所有文件的md5并去重

find tg/ -maxdepth 1 -type f -print0 | xargs -0 md5sum | sort |uniq -w 32  > uniq.txt

将非重复的文件已到tg-uniq/

mkdir tg-uniq

cat uniq.txt| cut -c 35- | tr '\n' '\0' | xargs -0 -i mv {}  tg-uniq/

剩下的重复文件可以选择性删除

···
