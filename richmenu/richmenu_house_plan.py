import requests
import json

# headers = {"Authorization":"Bearer 2i2Q2ShkvC0nOWZ+9E6AsMPsF/UMEC3+ihtoaOo99/sNFYtNwsRKnZbGeDizNAYXT1g8BWJIlXvkYcs+g7ED51dNQ+zyYQdo28q1T0tKpNH9lF9EYtt6AsGMIBKkMnkZXLoLPgGA+hys4D3/U45/3QdB04t89/1O/w1cDnyilFU=","Content-Type":"application/json"}
#
# body = {
#   "size": {
#     "width": 2500,
#     "height": 1686
#   },
#   "selected": "true",
#   "name": "house_plan",
#   "chatBarText": "關於家",
#   "areas": [
#     {
#       "bounds": {
#         "x": 0,
#         "y": 8,
#         "width": 1304,
#         "height": 690
#       },
#       "action": {
#         "type": "message",
#         "text": "臥室門鎖住了"
#       }
#     },
#     {
#       "bounds": {
#         "x": 1295,
#         "y": 8,
#         "width": 753,
#         "height": 118
#       },
#       "action": {
#         "type": "message",
#         "text": "好像沒辦法直接過去"
#       }
#     },
#     {
#       "bounds": {
#         "x": 1304,
#         "y": 130,
#         "width": 748,
#         "height": 556
#       },
#       "action": {
#         "type": "message",
#         "text": "前往廚房"
#       }
#     },
#     {
#       "bounds": {
#         "x": 2061,
#         "y": 13,
#         "width": 429,
#         "height": 685
#       },
#       "action": {
#         "type": "message",
#         "text": "前往玄關"
#       }
#     },
#     {
#       "bounds": {
#         "x": 967,
#         "y": 698,
#         "width": 1531,
#         "height": 976
#       },
#       "action": {
#         "type": "message",
#         "text": "前往客廳"
#       }
#     },
#     {
#       "bounds": {
#         "x": 8,
#         "y": 1035,
#         "width": 959,
#         "height": 651
#       },
#       "action": {
#         "type": "message",
#         "text": "前往書房"
#       }
#     },
#     {
#       "bounds": {
#         "x": 0,
#         "y": 698,
#         "width": 597,
#         "height": 337
#       },
#       "action": {
#         "type": "message",
#         "text": "前往廁所"
#       }
#     }
#   ]
# }
#
# req = requests.request('POST', 'https://api.line.me/v2/bot/richmenu',
#                        headers=headers,data=json.dumps(body).encode('utf-8'))
#
# print(req.text)

# {"richMenuId":"richmenu-ddeca7d9b46777ff8afe73b5875a38c0"}

# 設定 Rich menus 的圖片
# from linebot import (
#     LineBotApi, WebhookHandler
# )
#
# line_bot_api = LineBotApi('2i2Q2ShkvC0nOWZ+9E6AsMPsF/UMEC3+ihtoaOo99/sNFYtNwsRKnZbGeDizNAYXT1g8BWJIlXvkYcs+g7ED51dNQ+zyYQdo28q1T0tKpNH9lF9EYtt6AsGMIBKkMnkZXLoLPgGA+hys4D3/U45/3QdB04t89/1O/w1cDnyilFU=')
#
# with open("image/image_menus_1.png", 'rb') as f:
#     line_bot_api.set_rich_menu_image("richmenu-ddeca7d9b46777ff8afe73b5875a38c0", "image/jpeg", f)

# 啟用 Rich menus
import requests

headers = {"Authorization":"Bearer 2i2Q2ShkvC0nOWZ+9E6AsMPsF/UMEC3+ihtoaOo99/sNFYtNwsRKnZbGeDizNAYXT1g8BWJIlXvkYcs+g7ED51dNQ+zyYQdo28q1T0tKpNH9lF9EYtt6AsGMIBKkMnkZXLoLPgGA+hys4D3/U45/3QdB04t89/1O/w1cDnyilFU=","Content-Type":"application/json"}

req = requests.request('POST', 'https://api.line.me/v2/bot/user/all/richmenu/richmenu-ddeca7d9b46777ff8afe73b5875a38c0',
                       headers=headers)

print(req.text)


# 查看所有 Rich menus
from linebot import (
    LineBotApi, WebhookHandler
)

line_bot_api = LineBotApi('2i2Q2ShkvC0nOWZ+9E6AsMPsF/UMEC3+ihtoaOo99/sNFYtNwsRKnZbGeDizNAYXT1g8BWJIlXvkYcs+g7ED51dNQ+zyYQdo28q1T0tKpNH9lF9EYtt6AsGMIBKkMnkZXLoLPgGA+hys4D3/U45/3QdB04t89/1O/w1cDnyilFU=')

rich_menu_list = line_bot_api.get_rich_menu_list()

for rich_menu in rich_menu_list:
    print(rich_menu.rich_menu_id)


# 刪除rich menu
# from linebot import (
#     LineBotApi, WebhookHandler
# )
#
# line_bot_api = LineBotApi('2i2Q2ShkvC0nOWZ+9E6AsMPsF/UMEC3+ihtoaOo99/sNFYtNwsRKnZbGeDizNAYXT1g8BWJIlXvkYcs+g7ED51dNQ+zyYQdo28q1T0tKpNH9lF9EYtt6AsGMIBKkMnkZXLoLPgGA+hys4D3/U45/3QdB04t89/1O/w1cDnyilFU=')
#
# line_bot_api.delete_rich_menu('richmenu-3c0fd9c6c1184d4014e4bbe44789dead')


