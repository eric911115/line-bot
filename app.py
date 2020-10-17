from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage,
     TextSendMessage,
    TemplateSendMessage,
    ButtonsTemplate,
    MessageTemplateAction
)

app = Flask(__name__)

line_bot_api = LineBotApi('1dTO7g1uJGmYytCGvr0XSDGrweTNI1AnIyfu/1rX9ms1qHi1P+7Uq9zmeBFMCzIVAdmrEc3nKYU5nbrP1WZbtbB3H88oNRTToOntthD5uRaEIWLHvSc+RPY5pUOahbA4iEtSKorPJezO7PATguX+oAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('99fceeadf48dbe1ab2cf4325896cee4a')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    r = '我想上大學，想要知道為什麼請打"關於瑋彥"'

    if msg == '你好' :
        r = '你好'
    elif msg == '為什麼要瑋彥':
        r = '太可愛'
    elif msg == "關於瑋彥":
                line_bot_api.reply_message(  # 回復傳入的訊息文字
                    event.reply_token,
                    TemplateSendMessage(
                        alt_text='Buttons template',
                        template=ButtonsTemplate(
                            title='瑋彥的作品集',
                            text='請選擇作品',
                            actions=[
                                MessageTemplateAction(
                                    label='IG濾鏡',
                                    text='IG濾鏡'
                                ),
                                MessageTemplateAction(
                                    label='youtube',
                                    text='youtube'
                                ),
                                MessageTemplateAction(
                                    label='網頁',
                                    text='網頁'
                                )
                            ]
                        )
                    )
                )
    elif msg == "IG濾鏡":
                    arousel_template = TemplateSendMessage(
        alt_text='Carousel template',
        template=CarouselTemplate(
        columns=[
            CarouselColumn(
                thumbnail_image_url='顯示在開頭的大圖片網址',
                title='this is menu1',
                text='description1',
                actions=[
                    PostbackTemplateAction(
                        label='postback1',
                        text='postback text1',
                        data='action=buy&itemid=1'
                    ),
                    MessageTemplateAction(
                        label='message1',
                        text='message text1'
                    ),
                    URITemplateAction(
                        label='uri1',
                        uri='http://example.com/1'
                    )
                ]
            ),
            CarouselColumn(
                thumbnail_image_url='顯示在開頭的大圖片網址',
                title='this is menu2',
                text='description2',
                actions=[
                    PostbackTemplateAction(
                        label='postback2',
                        text='postback text2',
                        data='action=buy&itemid=2'
                    ),
                    MessageTemplateAction(
                        label='message2',
                        text='message text2'
                    ),
                    URITemplateAction(
                        label='連結2',
                        uri='http://example.com/2'
                    )
                ]
            )
        ]
    )
    )
                    
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=r))

    


if __name__ == "__main__":
    app.run()