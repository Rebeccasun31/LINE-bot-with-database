from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError, LineBotApiError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, TemplateSendMessage, ButtonsTemplate, MessageTemplateAction, PostbackEvent, PostbackTemplateAction, StickerMessage
)

import os
import json
import boto3
import psycopg2
import random

line_bot_api = LineBotApi(os.environ['Channel_access_token'])
handler = WebhookHandler(os.environ['Channel_secret'])

def getCredentials():
    credential = {}
    
    secret_name = "drinkbot-rds-secret"
    region_name = "us-east-1"
    
    client = boto3.client(
      service_name='secretsmanager',
      region_name=region_name
    )
    
    get_secret_value_response = client.get_secret_value(
      SecretId=secret_name
    )
    
    secret = json.loads(get_secret_value_response['SecretString'])
    
    credential['username'] = secret['username']
    credential['password'] = secret['password']
    credential['host'] = "drinkbot.cp8zgbkpy7vl.us-east-1.rds.amazonaws.com"
    credential['db'] = "drinks"
    
    return credential

def lambda_handler(event, context):
    credential = getCredentials()
    connection = psycopg2.connect(user=credential['username'], password=credential['password'], host=credential['host'], database=credential['db'])
    cursor = connection.cursor()
    
    query_c1 = "select * from drink where 價錢 <= 40 and editors_choice = '推'"
    cursor.execute(query_c1)
    result_c1 = cursor.fetchall()
    
    query_c2 = "select * from drink where 價錢 <= 60 and editors_choice = '推'"
    cursor.execute(query_c2)
    result_c2 = cursor.fetchall()
    
    query_c3 = "select * from drink where editors_choice = '推'"
    cursor.execute(query_c3)
    result_c3 = cursor.fetchall()
    
    query_w1 = "select * from drink where 價錢 <= 40 and 甜度 < 3  and 加料 = '無' and 水果 = '無' and 乳製品 = '無'"
    cursor.execute(query_w1)
    result_w1 = cursor.fetchall()
    
    query_w2 = "select * from drink where 價錢 <= 60 and 甜度 < 3 and 加料 = '無' and 水果 = '無' and 乳製品 = '無'"
    cursor.execute(query_w2)
    result_w2 = cursor.fetchall()
    
    query_w3 = "select * from drink where 甜度 < 3 and 加料 = '無' and 水果 = '無' and 乳製品 = '無'"
    cursor.execute(query_w3)
    result_w3 = cursor.fetchall()
    
    query_w4 = "select * from drink where 價錢 <= 40 and 甜度 = 3 and 加料 = '無' and 水果 = '無' and 乳製品 = '無'"
    cursor.execute(query_w4)
    result_w4 = cursor.fetchall()
    
    query_w5 = "select * from drink where 價錢 <= 60 and 甜度 = 3 and 加料 = '無' and 水果 = '無' and 乳製品 = '無'"
    cursor.execute(query_w5)
    result_w5 = cursor.fetchall()
    
    query_w6 = "select * from drink where 甜度 = 3 and 加料 = '無' and 水果 = '無' and 乳製品 = '無'"
    cursor.execute(query_w6)
    result_w6 = cursor.fetchall()
    
    query_w7 = "select * from drink where 價錢 <= 40 and 甜度 > 3 and 加料 = '無' and 水果 = '無' and 乳製品 = '無'"
    cursor.execute(query_w7)
    result_w7 = cursor.fetchall()
    
    query_w8 = "select * from drink where 價錢 <= 60 and 甜度 > 3 and 加料 = '無' and 水果 = '無' and 乳製品 = '無'"
    cursor.execute(query_w8)
    result_w8 = cursor.fetchall()
    
    query_w9 = "select * from drink where 甜度 > 3 and 加料 = '無' and 水果 = '無' and 乳製品 = '無'"
    cursor.execute(query_w9)
    result_w9 = cursor.fetchall()


    query_n1 = "select * from drink where 價錢 <= 40 and 甜度 < 3 and 水果 = '有'"
    cursor.execute(query_n1)
    result_n1 = cursor.fetchall()
    
    query_n2 = "select * from drink where 價錢 <= 60 and 甜度 < 3 and 水果 = '有'"
    cursor.execute(query_n2)
    result_n2 = cursor.fetchall()
    
    query_n3 = "select * from drink where 甜度 < 3 and 水果 = '有'"
    cursor.execute(query_n3)
    result_n3 = cursor.fetchall()
    
    query_n4 = "select * from drink where 價錢 <= 40 and 甜度 = 3 and 水果 = '有'"
    cursor.execute(query_n4)
    result_n4 = cursor.fetchall()
    
    query_n5 = "select * from drink where 價錢 <= 60 and 甜度 = 3 and 水果 = '有'"
    cursor.execute(query_n5)
    result_n5 = cursor.fetchall()
    
    query_n6 = "select * from drink where 甜度 = 3 and 水果 = '有'"
    cursor.execute(query_n6)
    result_n6 = cursor.fetchall()
    
    query_n7 = "select * from drink where 價錢 <= 40 and 甜度 > 3 and 水果 = '有'"
    cursor.execute(query_n7)
    result_n7 = cursor.fetchall()
    
    query_n8 = "select * from drink where 價錢 <= 60 and 甜度 > 3 and 水果 = '有'"
    cursor.execute(query_n8)
    result_n8 = cursor.fetchall()
    
    query_n9 = "select * from drink where 甜度 > 3 and 水果 = '有'"
    cursor.execute(query_n9)
    result_n9 = cursor.fetchall()


    query_y1 = "select * from drink where 價錢 <= 40 and 甜度 > 3 and 加料 = '有'"
    cursor.execute(query_y1)
    result_y1 = cursor.fetchall()
    
    query_y2 = "select * from drink where 價錢 <= 40 and 甜度 = 3 and 加料 = '有'"
    cursor.execute(query_y2)
    result_y2 = cursor.fetchall()
    
    query_y3 = "select * from drink where 價錢 <= 40 and 甜度 < 3 and 加料 = '有'"
    cursor.execute(query_y3)
    result_y3 = cursor.fetchall()
    
    query_y4 = "select * from drink where 價錢 <= 60 and 甜度 > 3 and 加料 = '有'"
    cursor.execute(query_y4)
    result_y4 = cursor.fetchall()
    
    query_y5 = "select * from drink where 價錢 <= 60 and 甜度 = 3 and 加料 = '有'"
    cursor.execute(query_y5)
    result_y5 = cursor.fetchall()
    
    query_y6 = "select * from drink where 價錢 <= 60 and 甜度 < 3 and 加料 = '有'"
    cursor.execute(query_y6)
    result_y6 = cursor.fetchall()
    
    query_y7 = "select * from drink where 甜度 > 3 and 加料 = '有'"
    cursor.execute(query_y7)
    result_y7 = cursor.fetchall()
    
    query_y8 = "select * from drink where 甜度 = 3 and 加料 = '有'"
    cursor.execute(query_y8)
    result_y8 = cursor.fetchall()
    
    query_y9 = "select * from drink where 甜度 < 3 and 加料 = '有'"
    cursor.execute(query_y9)
    result_y9 = cursor.fetchall()
    

    query_r1 = "select * from drink where 價錢 <= 40 and 甜度 < 3 and 乳製品 = '有'"
    cursor.execute(query_r1)
    result_r1 = cursor.fetchall()
    
    query_r2 = "select * from drink where 價錢 <= 60 and 甜度 < 3 and 乳製品 = '有'"
    cursor.execute(query_r2)
    result_r2 = cursor.fetchall()
    
    query_r3 = "select * from drink where 甜度 < 3 and 乳製品 = '有'"
    cursor.execute(query_r3)
    result_r3 = cursor.fetchall()
    
    query_r4 = "select * from drink where 價錢 <= 40 and 甜度 = 3 and 乳製品 = '有'"
    cursor.execute(query_r4)
    result_r4 = cursor.fetchall()
    
    query_r5 = "select * from drink where 價錢 <= 60 and 甜度 = 3 and 乳製品 = '有'"
    cursor.execute(query_r5)
    result_r5 = cursor.fetchall()
    
    query_r6 = "select * from drink where 甜度 = 3 and 乳製品 = '有'"
    cursor.execute(query_r6)
    result_r6 = cursor.fetchall()
    
    query_r7 = "select * from drink where 價錢 <= 40 and 甜度 > 3 and 乳製品 = '有'"
    cursor.execute(query_r7)
    result_r7 = cursor.fetchall()
    
    query_r8 = "select * from drink where 價錢 <= 60 and 甜度 > 3 and 乳製品 = '有'"
    cursor.execute(query_r8)
    result_r8 = cursor.fetchall()
    
    query_r9 = "select * from drink where 甜度 > 3 and 乳製品 = '有'"
    cursor.execute(query_r9)
    result_r9 = cursor.fetchall()

    # ------------------------------------------------------------------------------------

 
    
    
    @handler.add(MessageEvent, message=StickerMessage)
    def handle_message(event):
        # if event.message.text == '嗨':
        line_bot_api.reply_message(
            event.reply_token,
            TemplateSendMessage(
                alt_text = 'buttons templates',
                template = ButtonsTemplate(
                    title='你有多少錢',
                    text='哇勒',
                    actions=[
                        PostbackTemplateAction(
                            label='40below',
                            text='我超窮',
                            data='A&40'
                            ),
                        PostbackTemplateAction(
                            label='60below',
                            text='我還好',
                            data='A&60'
                            ),
                        PostbackTemplateAction(
                            label='infinity',
                            text='我超有錢錢',
                            data='A&70'
                            )
                        ]
                    )
                )
            )
            
            
    @handler.add(PostbackEvent)
    def handle_postback(event):
        
        if event.postback.data[0:1] == 'A':
            price = event.postback.data[2:]
            
            
            line_bot_api.reply_message(
            event.reply_token,
            TemplateSendMessage(
                alt_text = 'buttons templates',
                template = ButtonsTemplate(
                    title='今天想怎樣',
                    text='==',
                    actions=[
                        PostbackTemplateAction(
                            label='我自己選',
                            text='包我選',
                            data = 'B&' + price
                            ),
                        PostbackTemplateAction(
                            label='我不知道',
                            text='幫我選',
                            data = 'C&' + price + '&幫我選'
                            )
                        ]
                    )
                )
            )
            
        elif event.postback.data[0:1] == 'B':
            result = event.postback.data[2:]
            
            
            line_bot_api.reply_message(
            event.reply_token,
            TemplateSendMessage(
                alt_text = 'buttons templates',
                template = ButtonsTemplate(
                    title='今天想怎樣',
                    text='==',
                    actions=[
                        PostbackTemplateAction(
                            label='加料',
                            text='嚼嚼',
                            data = 'D&' + result + '&加料'
                            ),
                        PostbackTemplateAction(
                            label='水果',
                            text='補充維他命',
                            data = 'D&' + result + '&水果'
                            ),
                        PostbackTemplateAction(
                            label='牛奶',
                            text='我想長高',
                            data = 'D&' + result + '&牛奶'
                            ),
                        PostbackTemplateAction(
                            label='都不要',
                            text='都不要',
                            data = 'D&' + result + '&都不要'
                            )
                        ]
                    )
                )
            )
            
        elif event.postback.data[0:1] == 'D':
            re = event.postback.data[2:]
            
            
            line_bot_api.reply_message(
            event.reply_token,
            TemplateSendMessage(
                alt_text = 'buttons templates',
                template = ButtonsTemplate(
                    title='甜',
                    text='你有多甜',
                    actions=[
                        PostbackTemplateAction(
                            label='小甜',
                            text='小田',
                            data = 'E&' + re + '&小'
                            ),
                        PostbackTemplateAction(
                            label='中甜',
                            text='中田',
                            data = 'E&' + re + '&中'
                            ),
                        PostbackTemplateAction(
                            label='大甜',
                            text='大田',
                            data = 'E&' + re + '&大'
                            )
                        ]
                    )
                )
            )
        elif event.postback.data[0:1] == 'E':
            r = event.postback.data[2:].split('&')
            
            p = r[0]
            o = r[1]
            s = r[2]
            
            if p == '40' and o == '加料' and s == '大':
                r_index = random.randint(0,len(result_y1)-1)
                te = TextSendMessage(text = result_y1[r_index][0] + result_y1[r_index][1] + ' $' + str(result_y1[r_index][2]))
                line_bot_api.reply_message(event.reply_token,te)
                
            elif p == '40' and o == '都不要' and s == '小':
                r_index = random.randint(0,len(result_w1)-1)
                te = TextSendMessage(text = result_w1[r_index][0] + result_w1[r_index][1] + ' $' + str(result_w1[r_index][2]))
                line_bot_api.reply_message(event.reply_token,te)

            elif p == '60' and o == '都不要' and s == '小':
                r_index = random.randint(0,len(result_w2)-1)
                te = TextSendMessage(text = result_w2[r_index][0] + result_w2[r_index][1] + ' $' + str(result_w2[r_index][2]))
                line_bot_api.reply_message(event.reply_token,te)

            elif p == '70' and o == '都不要' and s == '小':
                r_index = random.randint(0,len(result_w3)-1)
                te = TextSendMessage(text = result_w3[r_index][0] + result_w3[r_index][1] + ' $' + str(result_w3[r_index][2]))
                line_bot_api.reply_message(event.reply_token,te)

            elif p == '40' and o == '都不要' and s == '中':
                r_index = random.randint(0,len(result_w4)-1)
                te = TextSendMessage(text = result_w4[r_index][0] + result_w4[r_index][1] + ' $' + str(result_w4[r_index][2]))
                line_bot_api.reply_message(event.reply_token,te)

            elif p == '60' and o == '都不要' and s == '中':
                r_index = random.randint(0,len(result_w5)-1)
                te = TextSendMessage(text = result_w5[r_index][0] + result_w5[r_index][1] + ' $' + str(result_w5[r_index][2]))
                line_bot_api.reply_message(event.reply_token,te)

            elif p == '70' and o == '都不要' and s == '中':
                r_index = random.randint(0,len(result_w6)-1)
                te = TextSendMessage(text = result_w6[r_index][0] + result_w6[r_index][1] + ' $' + str(result_w6[r_index][2]))
                line_bot_api.reply_message(event.reply_token,te)

            elif p == '40' and o == '都不要' and s == '大':
                r_index = random.randint(0,len(result_w7)-1)
                te = TextSendMessage(text = result_w7[r_index][0] + result_w7[r_index][1] + ' $' + str(result_w7[r_index][2]))
                line_bot_api.reply_message(event.reply_token,te)

            elif p == '60' and o == '都不要' and s == '大':
                r_index = random.randint(0,len(result_w8)-1)
                te = TextSendMessage(text = result_w8[r_index][0] + result_w8[r_index][1] + ' $' + str(result_w8[r_index][2]))
                line_bot_api.reply_message(event.reply_token,te)

            elif p == '70' and o == '都不要' and s == '大':
                r_index = random.randint(0,len(result_w9)-1)
                te = TextSendMessage(text = result_w9[r_index][0] + result_w9[r_index][1] + ' $' + str(result_w9[r_index][2]))
                line_bot_api.reply_message(event.reply_token,te)

            elif p == '40' and o == '水果' and s == '小':
                r_index = random.randint(0,len(result_n1)-1)
                te = TextSendMessage(text = result_n1[r_index][0] + result_n1[r_index][1] + ' $' + str(result_n1[r_index][2]))
                line_bot_api.reply_message(event.reply_token,te)

            elif p == '60' and o == '水果' and s == '小':
                r_index = random.randint(0,len(result_n2)-1)
                te = TextSendMessage(text = result_n2[r_index][0] + result_n2[r_index][1] + ' $' + str(result_n2[r_index][2]))
                line_bot_api.reply_message(event.reply_token,te)

            elif p == '70' and o == '水果' and s == '小':
                r_index = random.randint(0,len(result_n3)-1)
                te = TextSendMessage(text = result_n3[r_index][0] + result_n3[r_index][1] + ' $' + str(result_n3[r_index][2]))
                line_bot_api.reply_message(event.reply_token,te)

            elif p == '40' and o == '水果' and s == '中':
                r_index = random.randint(0,len(result_n4)-1)
                te = TextSendMessage(text = result_n4[r_index][0] + result_n4[r_index][1] + ' $' + str(result_n4[r_index][2]))
                line_bot_api.reply_message(event.reply_token,te)

            elif p == '60' and o == '水果' and s == '中':
                r_index = random.randint(0,len(result_n5)-1)
                te = TextSendMessage(text = result_n5[r_index][0] + result_n5[r_index][1] + ' $' + str(result_n5[r_index][2]))
                line_bot_api.reply_message(event.reply_token,te)

            elif p == '70' and o == '水果' and s == '中':
                r_index = random.randint(0,len(result_n6)-1)
                te = TextSendMessage(text = result_n6[r_index][0] + result_n6[r_index][1] + ' $' + str(result_n6[r_index][2]))
                line_bot_api.reply_message(event.reply_token,te)

            elif p == '40' and o == '水果' and s == '大':
                r_index = random.randint(0,len(result_n7)-1)
                te = TextSendMessage(text = result_n7[r_index][0] + result_n7[r_index][1] + ' $' + str(result_n7[r_index][2]))
                line_bot_api.reply_message(event.reply_token,te)

            elif p == '60' and o == '水果' and s == '大':
                r_index = random.randint(0,len(result_n8)-1)
                te = TextSendMessage(text = result_n8[r_index][0] + result_n8[r_index][1] + ' $' + str(result_n8[r_index][2]))
                line_bot_api.reply_message(event.reply_token,te)

            elif p == '70' and o == '水果' and s == '大':
                r_index = random.randint(0,len(result_n9)-1)
                te = TextSendMessage(text = result_n9[r_index][0] + result_n9[r_index][1] + ' $' + str(result_n9[r_index][2]))
                line_bot_api.reply_message(event.reply_token,te)

            elif p == '40' and o == '加料' and s == '中':
                r_index = random.randint(0,len(result_y2)-1)
                te = TextSendMessage(text = result_y2[r_index][0] + result_y2[r_index][1] + ' $' + str(result_y2[r_index][2]))
                line_bot_api.reply_message(event.reply_token,te)

            elif p == '40' and o == '加料' and s == '小':
                r_index = random.randint(0,len(result_y3)-1)
                te = TextSendMessage(text = result_y3[r_index][0] + result_y3[r_index][1] + ' $' + str(result_y3[r_index][2]))
                line_bot_api.reply_message(event.reply_token,te)

            elif p == '60' and o == '加料' and s == '大':
                r_index = random.randint(0,len(result_y4)-1)
                te = TextSendMessage(text = result_y4[r_index][0] + result_y4[r_index][1] + ' $' + str(result_y4[r_index][2]))
                line_bot_api.reply_message(event.reply_token,te)

            elif p == '60' and o == '加料' and s == '中':
                r_index = random.randint(0,len(result_y5)-1)
                te = TextSendMessage(text = result_y5[r_index][0] + result_y5[r_index][1] + ' $' + str(result_y5[r_index][2]))
                line_bot_api.reply_message(event.reply_token,te)

            elif p == '60' and o == '加料' and s == '小':
                r_index = random.randint(0,len(result_y6)-1)
                te = TextSendMessage(text = result_y6[r_index][0] + result_y6[r_index][1] + ' $' + str(result_y6[r_index][2]))
                line_bot_api.reply_message(event.reply_token,te)

            elif p == '70' and o == '加料' and s == '大':
                r_index = random.randint(0,len(result_y7)-1)
                te = TextSendMessage(text = result_y7[r_index][0] + result_y7[r_index][1] + ' $' + str(result_y7[r_index][2]))
                line_bot_api.reply_message(event.reply_token,te)

            elif p == '70' and o == '加料' and s == '中':
                r_index = random.randint(0,len(result_y8)-1)
                te = TextSendMessage(text = result_y8[r_index][0] + result_y8[r_index][1] + ' $' + str(result_y8[r_index][2]))
                line_bot_api.reply_message(event.reply_token,te)

            elif p == '70' and o == '加料' and s == '小':
                r_index = random.randint(0,len(result_y9)-1)
                te = TextSendMessage(text = result_y9[r_index][0] + result_y9[r_index][1] + ' $' + str(result_y9[r_index][2]))
                line_bot_api.reply_message(event.reply_token,te)


            elif p == '40' and o == '牛奶' and s == '小':
                r_index = random.randint(0,len(result_r1)-1)
                te = TextSendMessage(text = result_r1[r_index][0] + result_r1[r_index][1] + ' $' + str(result_r1[r_index][2]))
                line_bot_api.reply_message(event.reply_token,te)

            elif p == '60' and o == '牛奶' and s == '小':
                r_index = random.randint(0,len(result_r2)-1)
                te = TextSendMessage(text = result_r2[r_index][0] + result_r2[r_index][1] + ' $' + str(result_r2[r_index][2]))
                line_bot_api.reply_message(event.reply_token,te)

            elif p == '70' and o == '牛奶' and s == '小':
                r_index = random.randint(0,len(result_r3)-1)
                te = TextSendMessage(text = result_r3[r_index][0] + result_r3[r_index][1] + ' $' + str(result_r3[r_index][2]))
                line_bot_api.reply_message(event.reply_token,te)

            elif p == '40' and o == '牛奶' and s == '中':
                r_index = random.randint(0,len(result_r4)-1)
                te = TextSendMessage(text = result_r4[r_index][0] + result_r4[r_index][1] + ' $' + str(result_r4[r_index][2]))
                line_bot_api.reply_message(event.reply_token,te)

            elif p == '60' and o == '牛奶' and s == '中':
                r_index = random.randint(0,len(result_r5)-1)
                te = TextSendMessage(text = result_r5[r_index][0] + result_r5[r_index][1] + ' $' + str(result_r5[r_index][2]))
                line_bot_api.reply_message(event.reply_token,te)

            elif p == '70' and o == '牛奶' and s == '中':
                r_index = random.randint(0,len(result_r6)-1)
                te = TextSendMessage(text = result_r6[r_index][0] + result_r6[r_index][1] + ' $' + str(result_r6[r_index][2]))
                line_bot_api.reply_message(event.reply_token,te)

            elif p == '40' and o == '牛奶' and s == '大':
                r_index = random.randint(0,len(result_r7)-1)
                te = TextSendMessage(text = result_r7[r_index][0] + result_r7[r_index][1] + ' $' + str(result_r7[r_index][2]))
                line_bot_api.reply_message(event.reply_token,te)

            elif p == '60' and o == '牛奶' and s == '大':
                r_index = random.randint(0,len(result_r8)-1)
                te = TextSendMessage(text = result_r8[r_index][0] + result_r8[r_index][1] + ' $' + str(result_r8[r_index][2]))
                line_bot_api.reply_message(event.reply_token,te)

            elif p == '70' and o == '牛奶' and s == '大':
                r_index = random.randint(0,len(result_r9)-1)
                te = TextSendMessage(text = result_r9[r_index][0] + result_r9[r_index][1] + ' $' + str(result_r9[r_index][2]))
                line_bot_api.reply_message(event.reply_token,te)

                
            
            #tbc
            
        elif event.postback.data[0:1] == 'C':
            r = event.postback.data[2:].split('&')
            p = r[0]
            if p == '40':
                r_index = random.randint(0,len(result_c1)-1)
                te = TextSendMessage(text = result_c1[r_index][0] + result_c1[r_index][1] + ' $' + str(result_c1[r_index][2]))
                line_bot_api.reply_message(event.reply_token,te)
                
            elif p == '60':
                r_index = random.randint(0,len(result_c2)-1)
                te = TextSendMessage(text = result_c2[r_index][0] + result_c2[r_index][1] + ' $' + str(result_c2[r_index][2]))
                line_bot_api.reply_message(event.reply_token,te)
            elif p == '70':
                r_index = random.randint(0,len(result_c3)-1)
                te = TextSendMessage(text = result_c3[r_index][0] + result_c3[r_index][1] + ' $' + str(result_c3[r_index][2]))
                line_bot_api.reply_message(event.reply_token,te)
                
            
             
             
    

    # ------------------------------------------------------------------------------------
    
    connection.commit()
    connection.close()

    # get X-Line-Signature header value
    signature = event['headers']['x-line-signature']

    # get request body as text
    body = event['body']

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        return {
            'statusCode': 502,
            'body': json.dumps("Invalid signature. Please check your channel access token/channel secret.")
            }
    
    return {
        'statusCode': 200,
        'body': json.dumps("Successfully.")
        }