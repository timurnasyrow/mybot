import telebot
from telebot import types
from telebot import apihelper
token = '571605115:AAHdwzWhtYUjxbvvnRzyNEYsIQ1xllt2s8c'
apihelper.proxy = {'https': 'socks5://163.172.152.192:1080'}
bot = telebot.TeleBot(token)
@bot.message_handler(commands=['start','help'])
def start(o):
      bot.send_message(o.chat.id,'Привет, воспользуйся кнопками меню!')
      keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
      keyboard.add(*[types.KeyboardButton(name) for name in ['Розн.Блок', 'Кор.Блок']])
      msg = bot.send_message(o.chat.id, 'Выберите блок!',
        reply_markup=keyboard)
def first(m):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(name) for name in ['Розн.Блок', 'Кор.Блок']])   
    msg = bot.send_message(m.chat.id, 'Выберите блок!',
        reply_markup=keyboard)
@bot.message_handler(func=lambda m:True)
def name(m):
    if m.text == 'Розн.Блок':
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name
                    in ['Общие положения']])
        keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name
                    in ['Консультант','М-р по обслуж']])
        keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name
                    in ['Асс-т КМ СБ-Премьер','Сервис-менеджер']])
        keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name
                    in ['М-р по продажам','КМ СБ-Премьер']])
        keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name
                    in ['Рук центра ПО','Рук офиса и зам']])
        keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name
                    in ['Работники ПФ','Спец по обс кор кл-ов']])
        keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name
                    in ['Зам рука по КБ','=>']])
        msg = bot.send_message(m.chat.id,'-----------Выберите должность----------',reply_markup=keyboard)
    elif m.text =='Кор.Блок':
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name
                    in ['Общие положения.']])
        keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name
                    in ['Аппарат ТБ']])
        keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name
                    in ['Малый и микро-бизнес']])
        keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name
                    in ['Крупный и средний бизнес']])
        keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name
                    in ['Клиентские подр-ия']])
        keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name
                    in ['Кредит. подр-я и мон-г залогов']])
        keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name
                    in ['->']])
        msg = bot.send_message(m.chat.id,'----------Выберите должность---------',reply_markup=keyboard)       
@bot.callback_query_handler(func=lambda c:True)
def inline(c):
    if c.data == 'Общие положения':
        bot.send_document(c.message.chat.id,"BQADAgADuwEAAodDcUvTUaeGmfZ3ggI")
    elif c.data == 'Консультант':
        bot.send_document(c.message.chat.id,"BQADAgADvAEAAodDcUvAqyVLcx-0RwI")
    elif c.data == 'М-р по обслуж':
        bot.send_document(c.message.chat.id,"BQADAgADAwEAAj_5eEtIaxIqjy0xhAI")
    elif c.data == 'Асс-т КМ СБ-Премьер' :
        bot.send_document(c.message.chat.id,"BQADAgADvQEAAodDcUuZe2rQ6xCCfQI")
    elif c.data == 'Сервис-менеджер':
        bot.send_document(c.message.chat.id,"BQADAgADBAEAAj_5eEupUy2_WYc2wAI")
    elif c.data == 'М-р по продажам':
        bot.send_document(c.message.chat.id,"BQADAgADBQEAAj_5eEv5VTB_aVEemAI")
    elif c.data == 'КМ СБ-Премьер':
        bot.send_document(c.message.chat.id,"BQADAgADBgEAAj_5eEvBa_27drNXpAI")
    elif c.data == 'Рук центра ПО':
        bot.send_document(c.message.chat.id,"BQADAgADBwEAAj_5eEu4aC-EN5ROuQI")
    elif c.data == 'Рук офиса и зам':
        bot.send_document(c.message.chat.id,"BQADAgADCAEAAj_5eEsi7_btSiJ6GQI")
    elif c.data == 'Работники ПФ':
        bot.send_document(c.message.chat.id,"BQADAgADvgEAAodDcUsdTCi7Mzg2OAI")
    elif c.data == 'Спец по обс кор кл-ов':
        bot.send_document(c.message.chat.id,"BQADAgADvwEAAodDcUubMeWeSNVs2QI")
    elif c.data == 'Зам рука по КБ':
        bot.send_document(c.message.chat.id,"BQADAgADwAEAAodDcUve_U-MzylJCwI")
    elif c.data == '=>':
          keyboard = types.InlineKeyboardMarkup()
          keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name
                        in ['Спец по ПП','Рук гр по ПП']])
          keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name
                        in ['М-р по пр зарп пр-в','Спец по сопр зар пр-в']])
          keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name
                        in ['Спец по зарп пр-м','Конс-т по ПФР']])
          keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name
                        in ['М-р соц программ','Нач сек-а по ПФР']])
          keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name
                        in ['Рук ВИП ВСП','Зам рука ВИП ВСП']])
          keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name
                        in ['КМ ВИП','Опер-й м-р']])
          keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name
                        in ['Адм-р зала']])
          keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name
                        in ['<=','==>']])
          bot.edit_message_reply_markup(c.message.chat.id,message_id=c.message.message_id,reply_markup=keyboard)
    elif c.data == 'Спец по ПП':
       bot.send_document(c.message.chat.id,"BQADAgADCQEAAj_5eEtA6CDqRnyyygI")
    elif c.data == 'Рук гр по ПП':
       bot.send_document(c.message.chat.id,"BQADAgADCgEAAj_5eEuDPRb3E2MErAI")
    elif c.data == 'М-р по пр зарп пр-в':
       bot.send_document(c.message.chat.id,"BQADAgADCwEAAj_5eEuw4BJ8OPbg_wI")
    elif c.data == 'Спец по сопр зар пр-в':
       bot.send_document(c.message.chat.id,"BQADAgADDAEAAj_5eEttmss7n7rrAAEC")
    elif c.data == 'Спец по зарп пр-м':
       bot.send_document(c.message.chat.id,"BQADAgADwQEAAodDcUvijDD0UMRj9gI")
    elif c.data == 'Конс-т по ПФР':
       bot.send_document(c.message.chat.id,"BQADAgADDQEAAj_5eEsrUNBvIYIy_gI")
    elif c.data == 'М-р соц программ':
       bot.send_document(c.message.chat.id,"BQADAgADwgEAAodDcUsQbTnDlvvUDAI")
    elif c.data == 'Нач сек-а по ПФР':
       bot.send_document(c.message.chat.id,"BQADAgADDgEAAj_5eEv9e9eUYquo6gI")
    elif c.data == 'Рук ВИП ВСП':
       bot.send_document(c.message.chat.id,"BQADAgADDwEAAj_5eEsbHXS6reJLOAI")
    elif c.data == 'Зам рука ВИП ВСП':
       bot.send_document(c.message.chat.id,"BQADAgADEAEAAj_5eEs4lxh4DN7aDwI")
    elif c.data == 'КМ ВИП':
       bot.send_document(c.message.chat.id,"BQADAgADwwEAAodDcUu7CqugWn-CdAI")
    elif c.data == 'Опер-й м-р':
       bot.send_document(c.message.chat.id,"BQADAgADEQEAAj_5eEvnnjbDPv4UiAI")
    elif c.data == 'Адм-р зала':
       bot.send_document(c.message.chat.id,"BQADAgADEgEAAj_5eEsFxu2NXJGc9wI")    
    elif c.data == '==>':
          keyboard = types.InlineKeyboardMarkup()
          keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name
                        in ['М-р по ипот кр','М-р по обс ипот кр']])
          keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name
                        in ['Рук и зам ЦИК','Рук офисов ИК']])
          keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name
                        in ['М-р по ключ парт ЖК','М-р по парт-м ЖК']])
          keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name
                        in ['Спец ЦОПП','Рук гр ЦОПП']])
          keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name
                        in ['Нач ЦОПП','М-р по пр эквайринга']])
          keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name
                        in ['Спец под-ки прод-ж','Спец сервис подд экв']])
          keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name
                        in ['<==','Спец техн подд экв']])
          bot.edit_message_reply_markup(c.message.chat.id,message_id=c.message.message_id,reply_markup=keyboard)
    elif c.data == 'М-р по ипот кр':
       bot.send_document(c.message.chat.id,"BQADAgADxAEAAodDcUtLEk-L0SRrrQI")
    elif c.data == 'М-р по обс ипот кр':
       bot.send_document(c.message.chat.id,"BQADAgADxQEAAodDcUt6VEsqkrZSiQI")
    elif c.data == 'Рук и зам ЦИК':
       bot.send_document(c.message.chat.id,"BQADAgADxgEAAodDcUumul9rUX10LQI")
    elif c.data == 'Рук офисов ИК':
       bot.send_document(c.message.chat.id,"BQADAgADxwEAAodDcUsw4UufLs8CugI")
    elif c.data == 'М-р по ключ парт ЖК':
       bot.send_document(c.message.chat.id,"BQADAgADEwEAAj_5eEsBonK1zO6R3QI")
    elif c.data == 'М-р по парт-м ЖК':
       bot.send_document(c.message.chat.id,"BQADAgADFAEAAj_5eEuDx5__fMo51AI")
    elif c.data == 'Спец ЦОПП':
       bot.send_document(c.message.chat.id,"BQADAgADFQEAAj_5eEuEaowXH8F_JQI")
    elif c.data == 'Рук гр ЦОПП':
       bot.send_document(c.message.chat.id,"BQADAgADFgEAAj_5eEsWSlsPQIu-nwI")
    elif c.data == 'Нач ЦОПП':
       bot.send_document(c.message.chat.id,"BQADAgADyAEAAodDcUvZEl0kBAQvYQI")
    elif c.data == 'М-р по пр эквайринга':
       bot.send_document(c.message.chat.id,"BQADAgADFwEAAj_5eEsC_POue2R0cAI")
    elif c.data == 'Спец под-ки прод-ж':
       bot.send_document(c.message.chat.id,"BQADAgADGAEAAj_5eEsvMu2wpAl2RAI")
    elif c.data == 'Спец сервис подд экв':
       bot.send_document(c.message.chat.id,"BQADAgADyQEAAodDcUtSBkyZup7UCwI")
    elif c.data == 'Спец техн подд экв':
       bot.send_document(c.message.chat.id,"BQADAgADygEAAodDcUtxyNnI8y59HAI")       
    elif c.data == '<==':
          keyboard = types.InlineKeyboardMarkup()
          keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name
                        in ['Спец по ПП','Рук гр по ПП']])
          keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name
                        in ['М-р по пр зарп пр-в','Спец по сопр зар пр-в']])
          keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name
                        in ['Спец по зарп пр-м','Конс-т по ПФР']])
          keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name
                        in ['М-р соц программ','Нач сек-а по ПФР']])
          keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name
                        in ['Рук ВИП ВСП','Зам рука ВИП ВСП']])
          keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name
                        in ['КМ ВИП','Опер-й м-р']])
          keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name
                        in ['Адм-р зала']])
          keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name
                        in ['<=','==>']])
          bot.edit_message_reply_markup(c.message.chat.id,message_id=c.message.message_id,reply_markup=keyboard)
    elif c.data == '<=':
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name
                    in ['Общие положения']])
        keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name
                    in ['Консультант','М-р по обслуж']])
        keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name
                    in ['Асс-т КМ СБ-Премьер','Сервис-менеджер']])
        keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name
                    in ['М-р по продажам','КМ СБ-Премьер']])
        keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name
                    in ['Рук центра ПО','Рук офиса и зам']])
        keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name
                    in ['Работники ПФ','Спец по обс кор кл-ов']])
        keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name
                    in ['Зам рука по КБ','=>']])
        bot.edit_message_reply_markup(c.message.chat.id,message_id=c.message.message_id,reply_markup=keyboard)
    elif c.data == '->':
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name
                    in ['Центр залог экспертизы']])
        keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name
                    in ['Транзакц-ый бизнес']])
        keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name
                    in ['Центр корп-х решений']])
        keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name
                    in ['Лин-лаборатория']])
        keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name
                    in ['<-']])
        bot.edit_message_reply_markup(c.message.chat.id,message_id=c.message.message_id,reply_markup=keyboard)
    elif c.data == '<-':      
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name
                    in ['Общие положения.']])
        keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name
                    in ['Аппарат ТБ']])
        keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name
                    in ['Малый и микро-бизнес']])
        keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name
                    in ['Крупный и средний бизнес']])
        keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name
                    in ['Клиентские подр-ия']])
        keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name
                    in ['Кредит. подр-я и мон-г залогов']])
        bot.edit_message_reply_markup(c.message.chat.id,message_id=c.message.message_id,reply_markup=keyboard)
    elif c.data == 'Общие положения.':
       bot.send_document(c.message.chat.id,"BQADAgADUwEAArUYqUuQYmeegNXVcAI")
    elif c.data == 'Аппарат ТБ':
       bot.send_document(c.message.chat.id,"BQADAgADYwQAAhdNoEv7oMIYgjxBHwI")
       bot.send_document(c.message.chat.id,"BQADAgADZAQAAhdNoEu5s84dE2kfJAI")
    elif c.data == 'Малый и микро-бизнес':
       bot.send_document(c.message.chat.id,"BQADAgADVAEAArUYqUvzw-vsdi38MQI")
       bot.send_document(c.message.chat.id,"BQADAgADVQEAArUYqUsoKBdxA0IlmgI")
    elif c.data == 'Крупный и средний бизнес':
       bot.send_document(c.message.chat.id,"BQADAgADVgEAArUYqUs8ag4pKQYt_wI")
       bot.send_document(c.message.chat.id,"BQADAgADVwEAArUYqUsI0alxCK9J9QI")
    elif c.data == 'Клиентские подр-ия':
       bot.send_document(c.message.chat.id,"BQADAgADaQQAAhdNoEsepnx2J0lSkgI")
       bot.send_document(c.message.chat.id,"BQADAgADWAEAArUYqUvY73970A4a3AI")
    elif c.data == 'Кредит. подр-я и мон-г залогов':
       bot.send_document(c.message.chat.id,"BQADAgADWQEAArUYqUssTljCpVllEAI")
       bot.send_document(c.message.chat.id,"BQADAgADWgEAArUYqUtJeVIrfXjwQQI")
    elif c.data == 'Центр залог экспертизы':
       bot.send_document(c.message.chat.id,"BQADAgADXQEAArUYqUsaWJue0R6h_wI")
       bot.send_document(c.message.chat.id,"BQADAgADXgEAArUYqUtJ718lSkA7dAI")
    elif c.data == 'Транзакц-ый бизнес':
       bot.send_document(c.message.chat.id,"BQADAgADagQAAhdNoEta8pByCcpiyQI")
       bot.send_document(c.message.chat.id,"BQADAgADawQAAhdNoEu98tX8W9BmQQI")
    elif c.data == 'Центр корп-х решений':
       bot.send_document(c.message.chat.id,"BQADAgADYgEAArUYqUvOsEITdJQtMAI")
       bot.send_document(c.message.chat.id,"BQADAgADYwEAArUYqUvLkGGVw-9q3gI")
    elif c.data == 'Лин-лаборатория':
       bot.send_document(c.message.chat.id,"BQADAgADbAQAAhdNoEvJRTBQktWGrgI")     
        




        
while True: 
    try:
        bot.polling(none_stop=True)

    except Exception as e:
        print(e)
        time.sleep(15)

  
