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
#   "name": "livingroom",
#   "chatBarText": "關於客廳",
#   "areas": [
#     {
#       "bounds": {
#         "x": 1589,
#         "y": 723,
#         "width": 825,
#         "height": 653
#       },
#       "action": {
#         "type": "postback",
#         "text": "來看電視吧",
#         "data": "action=play&item=tv_ entertainment"
#       }
#     },
#     {
#       "bounds": {
#         "x": 118,
#         "y": 525,
#         "width": 1396,
#         "height": 859
#       },
#       "action": {
#         "type": "message",
#         "text": "沙發坐起來真舒服，好像...快睡著了..."
#       }
#     },
#     {
#       "bounds": {
#         "x": 1741,
#         "y": 479,
#         "width": 269,
#         "height": 207
#       },
#       "action": {
#         "type": "message",
#         "text": "時鐘好像壞掉了，指針都沒有在動"
#       }
#     },
#     {
#       "bounds": {
#         "x": 25,
#         "y": 17,
#         "width": 2461,
#         "height": 429
#       },
#       "action": {
#         "type": "message",
#         "text": "燈好像怪怪的..."
#       }
#     },
#     {
#       "bounds": {
#         "x": 8,
#         "y": 1422,
#         "width": 2490,
#         "height": 244
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

# {"richMenuId":"richmenu-aa539642a4e870c6bcfaff4eab1d78b7"}

# 設定 Rich menus 的圖片
# from linebot import (
#     LineBotApi, WebhookHandler
# )
#
# line_bot_api = LineBotApi('2i2Q2ShkvC0nOWZ+9E6AsMPsF/UMEC3+ihtoaOo99/sNFYtNwsRKnZbGeDizNAYXT1g8BWJIlXvkYcs+g7ED51dNQ+zyYQdo28q1T0tKpNH9lF9EYtt6AsGMIBKkMnkZXLoLPgGA+hys4D3/U45/3QdB04t89/1O/w1cDnyilFU=')
#
# with open("image/livingroom.jpg", 'rb') as f:
#     line_bot_api.set_rich_menu_image("richmenu-aa539642a4e870c6bcfaff4eab1d78b7", "image/jpeg", f)

# 啟用 Rich menus
# import requests
#
# headers = {"Authorization":"Bearer 2i2Q2ShkvC0nOWZ+9E6AsMPsF/UMEC3+ihtoaOo99/sNFYtNwsRKnZbGeDizNAYXT1g8BWJIlXvkYcs+g7ED51dNQ+zyYQdo28q1T0tKpNH9lF9EYtt6AsGMIBKkMnkZXLoLPgGA+hys4D3/U45/3QdB04t89/1O/w1cDnyilFU=","Content-Type":"application/json"}
#
# req = requests.request('POST', 'https://api.line.me/v2/bot/user/all/richmenu/richmenu-aa539642a4e870c6bcfaff4eab1d78b7',
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