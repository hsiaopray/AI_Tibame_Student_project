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
#   "name": "outside",
#   "chatBarText": "關於陽台",
#   "areas": [
#     {
#       "bounds": {
#         "x": 917,
#         "y": 842,
#         "width": 706,
#         "height": 664
#       },
#       "action": {
#         "type": "message",
#         "text": "來洗衣服好了"
#       }
#     },
#     {
#       "bounds": {
#         "x": 1669,
#         "y": 126,
#         "width": 831,
#         "height": 1560
#       },
#       "action": {
#         "type": "message",
#         "text": "現在都封城，外面都沒人了"
#       }
#     },
#     {
#       "bounds": {
#         "x": 17,
#         "y": 38,
#         "width": 723,
#         "height": 1648
#       },
#       "action": {
#         "type": "message",
#         "text": "前往廚房"
#       }
#     }
#   ]
# }
#
# req = requests.request('POST', 'https://api.line.me/v2/bot/richmenu',
#                        headers=headers,data=json.dumps(body).encode('utf-8'))
#
# print(req.text)

# {"richMenuId":"richmenu-e5be13aea8b048f1e43dbf9c0513f9a5"}

# 設定 Rich menus 的圖片
# from linebot import (
#     LineBotApi, WebhookHandler
# )
#
# line_bot_api = LineBotApi('2i2Q2ShkvC0nOWZ+9E6AsMPsF/UMEC3+ihtoaOo99/sNFYtNwsRKnZbGeDizNAYXT1g8BWJIlXvkYcs+g7ED51dNQ+zyYQdo28q1T0tKpNH9lF9EYtt6AsGMIBKkMnkZXLoLPgGA+hys4D3/U45/3QdB04t89/1O/w1cDnyilFU=')
#
# with open("image/outside.jpg", 'rb') as f:
#     line_bot_api.set_rich_menu_image("richmenu-e5be13aea8b048f1e43dbf9c0513f9a5", "image/jpeg", f)

# 啟用 Rich menus
import requests

headers = {"Authorization":"Bearer 2i2Q2ShkvC0nOWZ+9E6AsMPsF/UMEC3+ihtoaOo99/sNFYtNwsRKnZbGeDizNAYXT1g8BWJIlXvkYcs+g7ED51dNQ+zyYQdo28q1T0tKpNH9lF9EYtt6AsGMIBKkMnkZXLoLPgGA+hys4D3/U45/3QdB04t89/1O/w1cDnyilFU=","Content-Type":"application/json"}

req = requests.request('POST', 'https://api.line.me/v2/bot/user/all/richmenu/richmenu-e5be13aea8b048f1e43dbf9c0513f9a5',
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