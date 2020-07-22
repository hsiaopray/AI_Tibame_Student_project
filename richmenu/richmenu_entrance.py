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
#   "name": "entrance",
#   "chatBarText": "關於玄關",
#   "areas": [
#     {
#       "bounds": {
#         "x": 1476,
#         "y": 0,
#         "width": 820,
#         "height": 395
#       },
#       "action": {
#         "type": "message",
#         "text": "備忘錄，我是不是又忘了什麼？"
#       }
#     },
#     {
#       "bounds": {
#         "x": 1527,
#         "y": 605,
#         "width": 967,
#         "height": 598
#       },
#       "action": {
#         "type": "message",
#         "text": "今天下雨了，鞋子濕了一整天，真不舒服"
#       }
#     },
#     {
#       "bounds": {
#         "x": 353,
#         "y": 1094,
#         "width": 1110,
#         "height": 312
#       },
#       "action": {
#         "type": "message",
#         "text": "隔離中，請勿出門!!!!!!!!!"
#       }
#     },
#     {
#       "bounds": {
#         "x": 614,
#         "y": 513,
#         "width": 559,
#         "height": 505
#       },
#       "action": {
#         "type": "message",
#         "text": "是 Lucky！"
#       }
#     },
#     {
#       "bounds": {
#         "x": 0,
#         "y": 25,
#         "width": 362,
#         "height": 1381
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

# {"richMenuId":"richmenu-5ce99f617283f7be62f5613a1b03781e"}

# 設定 Rich menus 的圖片
# from linebot import (
#     LineBotApi, WebhookHandler
# )
#
# line_bot_api = LineBotApi('2i2Q2ShkvC0nOWZ+9E6AsMPsF/UMEC3+ihtoaOo99/sNFYtNwsRKnZbGeDizNAYXT1g8BWJIlXvkYcs+g7ED51dNQ+zyYQdo28q1T0tKpNH9lF9EYtt6AsGMIBKkMnkZXLoLPgGA+hys4D3/U45/3QdB04t89/1O/w1cDnyilFU=')
#
# with open("image/entrance.jpg", 'rb') as f:
#     line_bot_api.set_rich_menu_image("richmenu-5ce99f617283f7be62f5613a1b03781e", "image/jpeg", f)

# 啟用 Rich menus
# import requests
#
# headers = {"Authorization":"Bearer 2i2Q2ShkvC0nOWZ+9E6AsMPsF/UMEC3+ihtoaOo99/sNFYtNwsRKnZbGeDizNAYXT1g8BWJIlXvkYcs+g7ED51dNQ+zyYQdo28q1T0tKpNH9lF9EYtt6AsGMIBKkMnkZXLoLPgGA+hys4D3/U45/3QdB04t89/1O/w1cDnyilFU=","Content-Type":"application/json"}
#
# req = requests.request('POST', 'https://api.line.me/v2/bot/user/all/richmenu/richmenu-5ce99f617283f7be62f5613a1b03781e',
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