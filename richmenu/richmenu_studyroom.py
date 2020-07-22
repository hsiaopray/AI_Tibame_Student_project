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
#   "name": "studyroom",
#   "chatBarText": "關於書房",
#   "areas": [
#     {
#       "bounds": {
#         "x": 1307,
#         "y": 278,
#         "width": 1141,
#         "height": 942
#       },
#       "action": {
#         "type": "message",
#         "text": "來玩些遊戲吧"
#       }
#     },
#     {
#       "bounds": {
#         "x": 833,
#         "y": 282,
#         "width": 446,
#         "height": 774
#       },
#       "action": {
#         "type": "message",
#         "text": "看些書好了"
#       }
#     },
#     {
#       "bounds": {
#         "x": 0,
#         "y": 1258,
#         "width": 2490,
#         "height": 416
#       },
#       "action": {
#         "type": "message",
#         "text": "這裡什麼都沒有"
#       }
#     },
#     {
#       "bounds": {
#         "x": 420,
#         "y": 227,
#         "width": 404,
#         "height": 824
#       },
#       "action": {
#         "type": "message",
#         "text": "前往大廳"
#       }
#     }
#   ]
# }
#
# req = requests.request('POST', 'https://api.line.me/v2/bot/richmenu',
#                        headers=headers,data=json.dumps(body).encode('utf-8'))
#
# print(req.text)

# {"richMenuId":"richmenu-be72968b52bad1ea3297223564b96dd8"}

# 設定 Rich menus 的圖片
# from linebot import (
#     LineBotApi, WebhookHandler
# )
#
# line_bot_api = LineBotApi('2i2Q2ShkvC0nOWZ+9E6AsMPsF/UMEC3+ihtoaOo99/sNFYtNwsRKnZbGeDizNAYXT1g8BWJIlXvkYcs+g7ED51dNQ+zyYQdo28q1T0tKpNH9lF9EYtt6AsGMIBKkMnkZXLoLPgGA+hys4D3/U45/3QdB04t89/1O/w1cDnyilFU=')
#
# with open("image/studyroom.jpg", 'rb') as f:
#     line_bot_api.set_rich_menu_image("richmenu-be72968b52bad1ea3297223564b96dd8", "image/jpeg", f)

# 啟用 Rich menus
import requests

headers = {"Authorization":"Bearer 2i2Q2ShkvC0nOWZ+9E6AsMPsF/UMEC3+ihtoaOo99/sNFYtNwsRKnZbGeDizNAYXT1g8BWJIlXvkYcs+g7ED51dNQ+zyYQdo28q1T0tKpNH9lF9EYtt6AsGMIBKkMnkZXLoLPgGA+hys4D3/U45/3QdB04t89/1O/w1cDnyilFU=","Content-Type":"application/json"}

req = requests.request('POST', 'https://api.line.me/v2/bot/user/all/richmenu/richmenu-be72968b52bad1ea3297223564b96dd8',
                       headers=headers)

print(req.text)


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
# line_bot_api.delete_rich_menu("richmenu-87195e3899c2daebc26c81ecdf492f37")