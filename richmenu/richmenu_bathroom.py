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
#   "name": "bathroom",
#   "chatBarText": "關於廁所",
#   "areas": [
#     {
#       "bounds": {
#         "x": 1775,
#         "y": 311,
#         "width": 706,
#         "height": 1367
#       },
#       "action": {
#         "type": "message",
#         "text": "我真帥"
#       }
#     },
#     {
#       "bounds": {
#         "x": 841,
#         "y": 370,
#         "width": 917,
#         "height": 808
#       },
#       "action": {
#         "type": "message",
#         "text": "嘩啦啦嘩啦啦嘩啦啦......"
#       }
#     },
#     {
#       "bounds": {
#         "x": 412,
#         "y": 463,
#         "width": 496,
#         "height": 950
#       },
#       "action": {
#         "type": "message",
#         "text": "等等，我的肚子...."
#       }
#     },
#     {
#       "bounds": {
#         "x": 799,
#         "y": 1427,
#         "width": 808,
#         "height": 259
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

# {"richMenuId":"richmenu-a483bc2452bbe7691de931760645af47"}

# 設定 Rich menus 的圖片
# from linebot import (
#     LineBotApi, WebhookHandler
# )
#
# line_bot_api = LineBotApi('2i2Q2ShkvC0nOWZ+9E6AsMPsF/UMEC3+ihtoaOo99/sNFYtNwsRKnZbGeDizNAYXT1g8BWJIlXvkYcs+g7ED51dNQ+zyYQdo28q1T0tKpNH9lF9EYtt6AsGMIBKkMnkZXLoLPgGA+hys4D3/U45/3QdB04t89/1O/w1cDnyilFU=')
#
# with open("image/bathroom.jpg", 'rb') as f:
#     line_bot_api.set_rich_menu_image("richmenu-a483bc2452bbe7691de931760645af47", "image/jpeg", f)

# 啟用 Rich menus
import requests

headers = {"Authorization":"Bearer 2i2Q2ShkvC0nOWZ+9E6AsMPsF/UMEC3+ihtoaOo99/sNFYtNwsRKnZbGeDizNAYXT1g8BWJIlXvkYcs+g7ED51dNQ+zyYQdo28q1T0tKpNH9lF9EYtt6AsGMIBKkMnkZXLoLPgGA+hys4D3/U45/3QdB04t89/1O/w1cDnyilFU=","Content-Type":"application/json"}

req = requests.request('POST', 'https://api.line.me/v2/bot/user/all/richmenu/richmenu-a483bc2452bbe7691de931760645af47',
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
# line_bot_api.delete_rich_menu(rich_menu.rich_menu_id)