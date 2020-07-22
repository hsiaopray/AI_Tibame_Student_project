# 1.引用套件
from flask import Flask, request, abort

from linebot import (
        LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, FollowEvent, ImageSendMessage,
    TemplateSendMessage, ButtonsTemplate, MessageAction, URIAction, PostbackAction,
    PostbackEvent, QuickReply, QuickReplyButton, LocationAction, ImageMessage,
    VideoMessage, FlexSendMessage
)
import requests
import json
import random

# 2.準備素材
app = Flask(__name__)
# 常見問題
# 沒複製完整
# 注意開頭和結尾的單(雙)引號
line_bot_api = LineBotApi('2i2Q2ShkvC0nOWZ+9E6AsMPsF/UMEC3+ihtoaOo99/sNFYtNwsRKnZbGeDizNAYXT1g8BWJIlXvkYcs+g7ED51dNQ+zyYQdo28q1T0tKpNH9lF9EYtt6AsGMIBKkMnkZXLoLPgGA+hys4D3/U45/3QdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('a5618f76d67f485e9f8554eb00dead12')

'''
總機收信的驗證流程
1. 驗證信件
2. 信件轉發給部門
3. 處理不合格的信件

handler得如何處理傳來的消息
1. 驗證消息
2. 轉發
3. 處理不合規的消息

'''
@app.route("/callback", methods=['POST'])
def callback():

    # 取出驗證所需的東西
    # 固定的，不需要修改，誰改，誰就是小雞雞。
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)

    # 把寄過來的消息，都印出來
    app.logger.info("Request body: " + body)
    print(body)  #   印出來，方便 Debug

    # handle webhook body
    try:
        # handler 將 body 跟 signature 拿來確認消息的合法性
        # 另外還有一個用途，轉發給後續的業務邏輯
        handler.handle(body, signature)
       # 若訊息不合法，做下面處理
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        # 忽略消息，並告知 Line 400狀態
        abort(400)
    # 若都沒有問題，則都回傳 OK
    return 'OK'

# 客戶端的自製邏輯
'''
告知handler
若收到關注事件，
    則取人家個資，準備存成檔案
            引用json
                把python的變數轉換成json格式
                用with純入指定檔案
'''

@handler.add(FollowEvent)
def handle_follow(event):
    # 取得用戶個資
    user_profile = line_bot_api.get_profile(event.source.user_id)

    # 開啟一個檔案，將用戶個資轉換成json格式，存入檔案
    with open("./user.txt" , "a") as myfile:
        myfile.write(
            json.dumps(
                vars(user_profile)
            )
        )
        # 新資料換行
        myfile.write("\r\n")

    # 建立文字消息
    follow_text_send_messange = TextSendMessage("你迷迷糊糊地回家門口，被告知因為剛從疫區回國，需要自主隔離")

    # 建立範本消息
    buttons_template_message = TemplateSendMessage(
        alt_text='Buttons template',
        template=ButtonsTemplate(
            thumbnail_image_url='https://github.com/hsiaopray/student_project/blob/master/start.jpg?raw=true',
            title='COVIN-19 (武漢肺炎)',
            text='政府公告: 旅遊疫情建議「第一級」及「第二級」國家入境旅客，入境後須自主健康管理14天',
            actions=[
                # 如何解析多欄位的 data
                # python querystring parser
                MessageAction(
                    label="開始你的隔離生活",
                    text="點選圖片前往指定地點"
                )
            ]
        )
    )

    # 麻煩line_bot_api 把文字消息、圖片消息、範本消息、json生成的模本消息交給line
    line_bot_api.reply_message(event.reply_token, [follow_text_send_messange, buttons_template_message])
'''
創建rich menu
    先利用line bot designer 做出 rich menu 的 body
    將rich menu 的框架丟給 line bot api，得到這個rich menu 的 id
    再將rich menu 的圖片傳給line bot api
        當底下需要圖文選單時，再利用rich menu 的 id 呼叫
'''
# 一開始進門的玄關

# 房間全覽

# 客廳

# 書房

# 廚房

# 廁所

# 陽台

# 臥室

'''
告知 handler 收到 Postback event 做xxx事情

    判斷postback的data
        若為
'''
@handler.add(MessageEvent, message=TextMessage)
def handle_postback_event(event):

    reply_text_messge = TextSendMessage(event.message.text)
    if reply_text_messge.text == "前往客廳":
        line_bot_api.link_rich_menu_to_user(
            user_id=line_bot_api.get_profile(event.source.user_id).user_id,
            rich_menu_id="richmenu-aa539642a4e870c6bcfaff4eab1d78b7"
        )

    elif reply_text_messge.text == "前往大廳":
        line_bot_api.link_rich_menu_to_user(
            user_id=line_bot_api.get_profile(event.source.user_id).user_id,
            rich_menu_id="richmenu-ddeca7d9b46777ff8afe73b5875a38c0"
        )

    elif reply_text_messge.text == "前往廚房":
        line_bot_api.link_rich_menu_to_user(
            user_id=line_bot_api.get_profile(event.source.user_id).user_id,
            rich_menu_id="richmenu-7e1cbf2b1f5653d672e06c7fed11ea72"
        )
    elif reply_text_messge.text == "前往玄關":
        line_bot_api.link_rich_menu_to_user(
            user_id=line_bot_api.get_profile(event.source.user_id).user_id,
            rich_menu_id="richmenu-5ce99f617283f7be62f5613a1b03781e"
        )

    elif reply_text_messge.text == "前往書房":
        line_bot_api.link_rich_menu_to_user(
            user_id=line_bot_api.get_profile(event.source.user_id).user_id,
            rich_menu_id="richmenu-be72968b52bad1ea3297223564b96dd8"
        )

    elif reply_text_messge.text == "前往廁所":
        line_bot_api.link_rich_menu_to_user(
            user_id=line_bot_api.get_profile(event.source.user_id).user_id,
            rich_menu_id="richmenu-a483bc2452bbe7691de931760645af47"
        )

    elif reply_text_messge.text == "前往臥室":
        line_bot_api.link_rich_menu_to_user(
            user_id=line_bot_api.get_profile(event.source.user_id).user_id,
            rich_menu_id="richmenu-3d72221c0ce598cc6f9ec723c08b10d3"
        )

    elif reply_text_messge.text == "前往陽台":
        line_bot_api.link_rich_menu_to_user(
            user_id=line_bot_api.get_profile(event.source.user_id).user_id,
            rich_menu_id="richmenu-e5be13aea8b048f1e43dbf9c0513f9a5"
        )

    # 開始的互動
    elif reply_text_messge.text == "點選圖片前往指定地點":
        line_bot_api.link_rich_menu_to_user(
            user_id=line_bot_api.get_profile(event.source.user_id).user_id,
            rich_menu_id="richmenu-5ce99f617283f7be62f5613a1b03781e"
        )

    # 玄關的互動訊息
    elif reply_text_messge.text == "是 Lucky！":
        image_message = ImageSendMessage(
            original_content_url='https://i2.kknews.cc/SIG=qggjlr/ctp-vzntr/94792o175ro14951n6o0032ps905864n.jpg ',
            preview_image_url='https://images2.gamme.com.tw/news2/2017/52/41/qZqZo6SVk6ecq6Q.jpg'
        )
        line_bot_api.reply_message(event.reply_token, image_message)

    elif reply_text_messge.text == "隔離中，請勿出門!!!!!!!!!":
        image_message = ImageSendMessage(
            original_content_url='https://www.health.taichung.gov.tw/media/541906/%E5%B1%85%E5%AE%B6%E6%AA%A2%E7%96%AB-%E9%9A%94%E9%9B%A2%E8%80%85%E7%A6%81%E6%AD%A2%E8%B6%B4%E8%B6%B4%E8%B5%B0.jpg',
            preview_image_url='https://www.health.taichung.gov.tw/media/541906/%E5%B1%85%E5%AE%B6%E6%AA%A2%E7%96%AB-%E9%9A%94%E9%9B%A2%E8%80%85%E7%A6%81%E6%AD%A2%E8%B6%B4%E8%B6%B4%E8%B5%B0.jpg'
        )
        line_bot_api.reply_message(event.reply_token, image_message)

    # 客廳的互動訊息
    elif reply_text_messge.text == "來看電視吧":
        # 創造QuickReplyButton
        text_quireply_first = QuickReplyButton(action=MessageAction(label="Netflix", text="最近冰與火之歌好像完結了"))
        text_quireply_second = QuickReplyButton(action=MessageAction(label="新聞", text="台灣新聞真的莫名其妙= ="))
        text_quireply_third = QuickReplyButton(action=MessageAction(label="電影", text="看點經典的吧"))

        # 創造一個QuickReply，並把剛剛創建的button放進去
        quick_reply_array = QuickReply(items=[text_quireply_first, text_quireply_second, text_quireply_third])

        # line_bot_api 傳送回去
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='請選擇你要的節目',quick_reply=quick_reply_array))

    elif reply_text_messge.text == "最近冰與火之歌好像完結了":
        buttons_template_message = TemplateSendMessage(
            alt_text='Buttons template',
            template=ButtonsTemplate(
                thumbnail_image_url='https://www.dramaqueen.com.tw/upload/images/mgot_s8_character_art_dany.jpg',
                title='冰與火之歌',
                text='《權力遊戲》是一部中世紀奇幻題材的電視連續劇。改編自喬治·R·R·馬丁的奇幻小說系列《冰與火之歌》的《權力遊戲》',
                actions=[
                    # 如何解析多欄位的 data
                    # python querystring parser
                    MessageAction(
                        label="開始觀看",
                        text="結局也太...")
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, buttons_template_message)

    elif reply_text_messge.text == "台灣新聞真的莫名其妙= =":
        buttons_template_message = TemplateSendMessage(
            alt_text='Buttons template',
            template=ButtonsTemplate(
                thumbnail_image_url='https://im.marieclaire.com.tw/m800c533h100b0/assets/mc/202006/5ED69328505111591120680.jpeg',
                title='振興三倍券',
                text='振興三倍券6大QA！超商預購、郵局購買、信用卡綁定優惠...懶人包幫你整理好了',
                actions=[
                    # 如何解析多欄位的 data
                    # python querystring parser
                    MessageAction(
                        label="開始觀看",
                        text="關在裡面領不到...")
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, buttons_template_message)

    elif reply_text_messge.text == "看點經典的吧":
        buttons_template_message = TemplateSendMessage(
            alt_text='Buttons template',
            template=ButtonsTemplate(
                thumbnail_image_url='https://img.myvideo.net.tw/images/WAR020/0000/0033/201309181832000352_420x600.jpg',
                title='全面啟動 INCEPTION',
                text='偷技高超的神偷唐姆柯比，目標是趁對象進入深沉的睡眠、心智遂呈現最脆弱狀態時，入侵其潛意識...',
                actions=[
                    # 如何解析多欄位的 data
                    # python querystring parser
                    MessageAction(
                        label="開始觀看",
                        text="太厲害啦!!!")
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, buttons_template_message)
        
    # 書房互動
    elif reply_text_messge.text == "來玩些遊戲吧":
        # 創造QuickReplyButton
        text_quireply_first = QuickReplyButton(action=MessageAction(label="switch", text="現在的 Switch好貴喔"))
        text_quireply_second = QuickReplyButton(action=MessageAction(label="ps4", text="PS5年底就要出了ㄟ，要買嗎？"))

        # 創造一個QuickReply，並把剛剛創建的button放進去
        quick_reply_array = QuickReply(items=[text_quireply_first, text_quireply_second])

        # line_bot_api 傳送回去
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='請選擇你想玩的遊戲', quick_reply=quick_reply_array))

    elif reply_text_messge.text == "現在的 Switch好貴喔":
        buttons_template_message = TemplateSendMessage(
            alt_text='Buttons template',
            template=ButtonsTemplate(
                thumbnail_image_url='https://ct.yimg.com/xd/api/res/1.2/3l5IRqFyeKqfj_m8SxVQkA--/YXBwaWQ9eXR3YXVjdGlvbnNlcnZpY2U7aD03MDA7cT04NTtyb3RhdGU9YXV0bzt3PTQxNw--/https://s.yimg.com/ob/image/4d965226-b7bd-411b-8470-68d6d992cf71.jpg',
                title='薩爾達傳說 曠野之息',
                text='薩爾達傳說是任天堂自1986年起推出的動作冒險遊戲系列，創始人為宮本茂。遊戲以奇幻世界為背景，描述著林克的冒險經歷...',
                actions=[
                    # 如何解析多欄位的 data
                    # python querystring parser
                    MessageAction(
                        label="開始遊戲",
                        text="真好玩")
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, buttons_template_message)

    elif reply_text_messge.text == "PS5年底就要出了ㄟ，要買嗎？":
        buttons_template_message = TemplateSendMessage(
            alt_text='Buttons template',
            template=ButtonsTemplate(
                thumbnail_image_url='https://upload.wikimedia.org/wikipedia/zh/f/f2/The_last_of_us_part_2_cover.jpg',
                title='最後生還者 第II章',
                text='《最後生還者 第II章》是一款由頑皮狗開發的生存恐怖動作遊戲。本作是2013年遊戲《最後生還者》的續作...',
                actions=[
                    # 如何解析多欄位的 data
                    # python querystring parser
                    MessageAction(
                        label="開始遊戲",
                        text="玩得好累阿")
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, buttons_template_message)

    elif reply_text_messge.text == "看些書好了":
        # 創造QuickReplyButton
        text_quireply_first = QuickReplyButton(action=MessageAction(label="富爸爸，窮爸爸", text="看完了我也能發財嗎？"))
        text_quireply_second = QuickReplyButton(action=MessageAction(label="哆啦Ａ夢 第０集", text="這也算書吧？"))
        text_quireply_third = QuickReplyButton(action=MessageAction(label="野貓軍團 咖哩飯", text="看完都餓了..."))

        # 創造一個QuickReply，並把剛剛創建的button放進去
        quick_reply_array = QuickReply(items=[text_quireply_first, text_quireply_second, text_quireply_third])

        # line_bot_api 傳送回去
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='請選擇你要的節目', quick_reply=quick_reply_array))

    # 廁所
    # elif reply_text_messge.text == "我真帥":
    #     image_message = ImageSendMessage(
    #         original_content_url='https://s.newtalk.tw/album/news/207/5c64e354b5868.jpg',
    #         preview_image_url='https://github.com/hsiaopray/student_project/blob/master/handsome.png?raw=true'
    #     )
    #     line_bot_api.reply_message(event.reply_token, image_message)

    elif reply_text_messge.text == "我真帥":
        with open("./mirror.json", "r", encoding="utf-8") as mirror:
            json_object = json.load(mirror)

        template_message_from_json = TemplateSendMessage.new_from_json_dict(json_object)

        line_bot_api.reply_message(event.reply_token, template_message_from_json)

    elif reply_text_messge.text == "嘩啦啦嘩啦啦嘩啦啦......":
        # 創造一個圖片訊息
        image_message = ImageSendMessage(
            original_content_url='https://pic.17qq.com/uploads/ckcnmpgcpv.jpeg',
            preview_image_url='https://img.itw01.com/images/2018/03/16/23/2535_l5FZM5_V24RNEC.jpg!r800x0.jpg'
        )
        # line_bot_api 傳送過去
        line_bot_api.reply_message(event.reply_token, image_message)

    # 廚房互動
    elif reply_text_messge.text == "來喝點東西吧":
        # 創造QuickReplyButton
        text_quireply_first = QuickReplyButton(action=MessageAction(label="喝酒", text="好暈喔 @@"))
        text_quireply_second = QuickReplyButton(action=MessageAction(label="可口可樂", text="快樂肥宅水，讚啦！"))
        text_quireply_third = QuickReplyButton(action=MessageAction(label="果汁", text="好甜喔！是濃縮的吧！"))

        # 創造一個QuickReply，並把剛剛創建的button放進去
        quick_reply_array = QuickReply(items=[text_quireply_first, text_quireply_second, text_quireply_third])

        # line_bot_api 傳過回去
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='請選擇你要的飲品', quick_reply=quick_reply_array))

    elif reply_text_messge.text == "肚子有點餓了":
        # 創造QuickReplyButton
        text_quireply_first = QuickReplyButton(action=MessageAction(label="咖哩", text="自己煮的果然不能吃 = ="))
        text_quireply_second = QuickReplyButton(action=MessageAction(label="泡麵", text="最簡單的，最好吃！"))
        text_quireply_third = QuickReplyButton(action=MessageAction(label="牛排", text="啊!回來的太急，沒有買"))

        # 創造一個QuickReply，並把剛剛創建的button放進去
        quick_reply_array = QuickReply(items=[text_quireply_first, text_quireply_second, text_quireply_third])

        # line_bot_api 傳過回去
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='請選擇你要的飲品', quick_reply=quick_reply_array))

    elif reply_text_messge.text == "現在都封城，外面都沒人了":
        # 創造一個圖片訊息
        image_message = ImageSendMessage(
            original_content_url='https://s.rfi.fr/media/display/0a0719cc-4073-11ea-af6d-005056a98db9/w:1280/p:16x9/2020-01-26t065742z_155462673_rc2ine9bvjjo_rtrmadp_3_china-health.jpg',
            preview_image_url='https://s.rfi.fr/media/display/0a0719cc-4073-11ea-af6d-005056a98db9/w:1280/p:16x9/2020-01-26t065742z_155462673_rc2ine9bvjjo_rtrmadp_3_china-health.jpg'
        )
        # line_bot_api 傳送過去
        line_bot_api.reply_message(event.reply_token, image_message)

    elif reply_text_messge.text == "來洗衣服好了":
        with open("./wash_clothes.json", "r", encoding="utf-8") as wash_clothes:
            json_object = json.load(wash_clothes)

        template_message_from_json = TemplateSendMessage.new_from_json_dict(json_object)

        line_bot_api.reply_message(event.reply_token, template_message_from_json)

    elif reply_text_messge.text == "來做個乾淨的孩子吧":
        with open("./clothes_item.json", "r", encoding="utf-8") as clothes_item:
            json_object = json.load(clothes_item)

        template_message_from_json = TemplateSendMessage.new_from_json_dict(json_object)

        line_bot_api.reply_message(event.reply_token, template_message_from_json)

    elif reply_text_messge.text == "看看是什麼":
        item_first = "是張便利商店的發票阿，都變得破破爛爛的了"
        item_second = "撿到一百塊，超爽der"
        item_third = "是臥室房間的鑰匙"

        item_message = random.choice([item_first, item_second, item_third])

        line_bot_api.reply_message(event.reply_token, TextSendMessage(item_message))

        if item_message == "是臥室房間的鑰匙":
            # with open("./bedroom_key.json", "r", encoding="utf-8") as key:
            #     json_object = json.load(key)
            #
            # template_message_from_json = TemplateSendMessage.new_from_json_dict(json_object)
            #
            # line_bot_api.reply_message(event.reply_token, template_message_from_json)
            # if reply_text_messge.text == "是":
                line_bot_api.link_rich_menu_to_user(
                    user_id=line_bot_api.get_profile(event.source.user_id).user_id,
                    rich_menu_id="richmenu-3d72221c0ce598cc6f9ec723c08b10d3"
                )
    elif reply_text_messge.text == "看些床邊故事吧":
        with open("./bed_read.json", "r", encoding="utf-8") as bed_read:
            json_object = json.load(bed_read)

        template_message_from_json =  FlexSendMessage.new_from_json_dict(json_object)

        line_bot_api.reply_message(event.reply_token, template_message_from_json)

    elif reply_text_messge.text == "原來都是夢阿":

        dream_send_message = TextSendMessage(text="還好你在台灣，所以沒有這麼嚴重的疫情，不過還是要記得做好防疫工作喔！")
        dream_send_image = ImageSendMessage(
            original_content_url='https://github.com/hsiaopray/student_project/blob/master/dream_wash_hands.jpg?raw=true',
            preview_image_url='https://github.com/hsiaopray/student_project/blob/master/dream_wash_hands.jpg?raw=true')
        dream_send_vidoe_message = TextSendMessage(text="防疫新生活" + "https://www.youtube.com/watch?v=uiYtECIpbqQ")

        line_bot_api.reply_message(event.reply_token, [dream_send_message, dream_send_image, dream_send_vidoe_message])

        line_bot_api.link_rich_menu_to_user(
            user_id=line_bot_api.get_profile(event.source.user_id).user_id,
            rich_menu_id="richmenu-470c864eafa5de695a37b9388eb53ece"
        )

    elif reply_text_messge.text == "重新開始":
        # 建立文字消息
        follow_text_send_messange = TextSendMessage("境外移入記得隔離14天喔！")

        # 建立範本消息
        buttons_template_message = TemplateSendMessage(
            alt_text='Buttons template',
            template=ButtonsTemplate(
                thumbnail_image_url='https://github.com/hsiaopray/student_project/blob/master/start.jpg?raw=true',
                title='COVIN-19 (武漢肺炎)',
                text='政府公告: 旅遊疫情建議「第一級」及「第二級」國家入境旅客，入境後須自主健康管理14天',
                actions=[
                    # 如何解析多欄位的 data
                    # python querystring parser
                    MessageAction(
                        label="開始你的隔離生活",
                        text="點選圖片前往指定地點"
                    )
                ]
            )
        )

        # 麻煩line_bot_api 把文字消息、圖片消息、範本消息、json生成的模本消息交給line
        line_bot_api.reply_message(event.reply_token, [follow_text_send_messange, buttons_template_message])

        line_bot_api.link_rich_menu_to_user(
            user_id=line_bot_api.get_profile(event.source.user_id).user_id,
            rich_menu_id="richmenu-5ce99f617283f7be62f5613a1b03781e"
        )


@handler.add(MessageEvent, message=ImageMessage)
def handle_image_message(event):

    mirror_send_message_first = TextSendMessage(text="你真帥")
    mirror_send_message_second = TextSendMessage(text="你好帥")
    mirror_send_message_third = TextSendMessage(text="還是算了吧")

    # mirror_send_message = random.choice([mirror_send_message_first, mirror_send_message_second, mirror_send_message_third]

    line_bot_api.reply_message(event.reply_token, random.choice([mirror_send_message_first, mirror_send_message_second, mirror_send_message_third]))



# 伺服器啟用
if __name__ == "__main__":
    app.run(host = "0.0.0.0")