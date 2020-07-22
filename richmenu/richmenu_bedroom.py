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
#   "name": "bedroom",
#   "chatBarText": "關於臥室",
#   "areas": [
#     {
#       "bounds": {
#         "x": 0,
#         "y": 1291,
#         "width": 2498,
#         "height": 383
#       },
#       "action": {
#         "type": "message",
#         "text": "前往大廳"
#       }
#     },
#     {
#       "bounds": {
#         "x": 1035,
#         "y": 938,
#         "width": 1261,
#         "height": 345
#       },
#       "action": {
#         "type": "message",
#         "text": "原來都是夢阿"
#       }
#     },
#     {
#       "bounds": {
#         "x": 1001,
#         "y": 585,
#         "width": 740,
#         "height": 332
#       },
#       "action": {
#         "type": "message",
#         "text": "看些床邊故事吧"
#       }
#     },
#     {
#       "bounds": {
#         "x": 450,
#         "y": 749,
#         "width": 534,
#         "height": 395
#       },
#       "action": {
#         "type": "message",
#         "text": "隔離不能出門，老闆還交代了一堆工作，真累..."
#       }
#     }
#   ]
# }
#
# req = requests.request('POST', 'https://api.line.me/v2/bot/richmenu',
#                        headers=headers,data=json.dumps(body).encode('utf-8'))
#
# print(req.text)

# {"richMenuId":"richmenu-3d72221c0ce598cc6f9ec723c08b10d3"}

# 設定 Rich menus 的圖片
from linebot import (
    LineBotApi, WebhookHandler
)

line_bot_api = LineBotApi('2i2Q2ShkvC0nOWZ+9E6AsMPsF/UMEC3+ihtoaOo99/sNFYtNwsRKnZbGeDizNAYXT1g8BWJIlXvkYcs+g7ED51dNQ+zyYQdo28q1T0tKpNH9lF9EYtt6AsGMIBKkMnkZXLoLPgGA+hys4D3/U45/3QdB04t89/1O/w1cDnyilFU=')

with open("image/bedroom.jpg", 'rb') as f:
    line_bot_api.set_rich_menu_image("richmenu-3d72221c0ce598cc6f9ec723c08b10d3", "image/jpeg", f)

# 啟用 Rich menus
# import requests
#
# headers = {"Authorization":"Bearer 2i2Q2ShkvC0nOWZ+9E6AsMPsF/UMEC3+ihtoaOo99/sNFYtNwsRKnZbGeDizNAYXT1g8BWJIlXvkYcs+g7ED51dNQ+zyYQdo28q1T0tKpNH9lF9EYtt6AsGMIBKkMnkZXLoLPgGA+hys4D3/U45/3QdB04t89/1O/w1cDnyilFU=","Content-Type":"application/json"}
#
# req = requests.request('POST', 'https://api.line.me/v2/bot/user/all/richmenu/richmenu-3d72221c0ce598cc6f9ec723c08b10d3',
#                        headers=headers)
#
# print(req.text)


# 查看所有 Rich menus
# from linebot import (
#     LineBotApi, WebhookHandler
# )
#
# line_bot_api = LineBotApi('2i2Q2ShkvC0nOWZ+9E6AsMPsF/UMEC3+ihtoaOo99/sNFYtNwsRKnZbGeDizNAYXT1g8BWJIlXvkYcs+g7ED51dNQ+zyYQdo28q1T0tKpNH9lF9EYtt6AsGMIBKkMnkZXLoLPgGA+hys4D3/U45/3QdB04t89/1O/w1cDnyilFU=')
#
# rich_menu_list = line_bot_api.get_rich_menu_list()
#
# for rich_menu in rich_menu_list:
#     print(rich_menu.rich_menu_id)


# 刪除rich menu
# from linebot import (
#     LineBotApi, WebhookHandler
# )
#
# line_bot_api = LineBotApi('2i2Q2ShkvC0nOWZ+9E6AsMPsF/UMEC3+ihtoaOo99/sNFYtNwsRKnZbGeDizNAYXT1g8BWJIlXvkYcs+g7ED51dNQ+zyYQdo28q1T0tKpNH9lF9EYtt6AsGMIBKkMnkZXLoLPgGA+hys4D3/U45/3QdB04t89/1O/w1cDnyilFU=')
#
# line_bot_api.delete_rich_menu(rich_menu.rich_menu_id)