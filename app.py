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
    MessageTemplateAction,
    ImageCarouselTemplate,
    ImageCarouselColumn,
    URITemplateAction   
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
                            thumbnail_image_url="https://lh3.googleusercontent.com/BMF7I7RSG8IapEoOiF_3mDwk30pYQsnWLmhP51ww0rhEZkiTJ6CBHrMxMUjQFoIREbgmi_krIJdbPS-gSzGMA8C2e3muiy0cSzJ33pFAm_6iKuKA9x1A9ooFuVB9ZRNX5dVCUE2m4Q=w600",
                            title='瑋彥的作品集',
                            text='請選擇濾鏡',
                            actions=[
                                MessageTemplateAction(
                                    label="IG濾鏡",
                                    text="我想看IG濾鏡"
                                ),
                                URITemplateAction(
                                    label="Youtube",
                                    uri="https://www.youtube.com/channel/UCH5tUrNXpr1x4pHpQGhfQXA?view_as=subscriber"
                                ),
                                URITemplateAction(
                                    label="網頁",
                                    uri="https://eric911115.github.io/school.html"
                                )                       
                            ]
                        )
                    )
                )  
    elif msg == "我想看IG濾鏡":
                line_bot_api.reply_message(  # 回復傳入的訊息文字
                    event.reply_token,
                    TemplateSendMessage(
                        alt_text='Buttons template',
                        template=ImageCarouselTemplate(
                            columns=[
                                ImageCarouselColumn(
                                    image_url="https://upload.cc/i1/2020/10/19/EjDUGz.jpg",
                                    action=URITemplateAction(
                                        label="學測倒數",
                                        uri="https://www.instagram.com/ar/1507952719375055/"
                                    )
                                ),
                                ImageCarouselColumn(
                                    image_url="https://upload.cc/i1/2020/10/19/AeUiZu.jpg",
                                    action=URITemplateAction(
                                        label="統測倒數",
                                        uri="https://www.instagram.com/ar/1233861126969567/"
                                    )
                                ),
                                ImageCarouselColumn(
                                    image_url="https://upload.cc/i1/2020/10/19/AmR8rf.jpg",
                                    action=URITemplateAction(
                                        label="北極沒有企鵝",
                                        uri="https://www.instagram.com/ar/651213445816757/"
                                    )
                                ),
                                ImageCarouselColumn(
                                    image_url="https://upload.cc/i1/2020/10/19/lBpEgV.jpg",
                                    action=URITemplateAction(
                                        label="豬如此類",
                                        uri="https://www.instagram.com/ar/603244753687030/"
                                    )
                                ),
                                    ImageCarouselColumn(
                                    image_url="https://upload.cc/i1/2020/10/19/VneW4d.jpg",
                                    action=URITemplateAction(
                                        label="學測戰士",
                                        uri="https://www.instagram.com/ar/690111801715364/"
                                    )
                                    )
                        )
                    )
                            ]
                )
                    
    
              
                    
    line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(r))
 


             
                
    


if __name__ == "__main__":
    app.run()