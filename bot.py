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
      keyboard.add(*[types.KeyboardButton(name) for name in ['ПА и ПВ','Прочее']])
      msg = bot.send_message(o.chat.id, 'Выберите блок!',
        reply_markup=keyboard)
def first(m):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(name) for name in ['Розн.Блок', 'Кор.Блок']])
    keyboard.add(*[types.KeyboardButton(name) for name in ['ПА и ПВ','Прочее']])
    msg = bot.send_message(m.chat.id, 'Выберите блок!',
        reply_markup=keyboard)
@bot.message_handler(func=lambda m:True)
def name(m):
    if m.text == 'Розн.Блок':
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name
                    in ['Общие положения']])
        keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name
                    in ['Распоряжение-420']])
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
        msg = bot.send_message(m.chat.id,'--------Выберите подразделение-------',reply_markup=keyboard)
    elif m.text =='ПА и ПВ':
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name
                    in ['Физ. лица']])
        keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name
                    in ['Юр. Лица']])
        keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name
                    in ['Руководство']])
        msg = bot.send_message(m.chat.id,'--------Выберите подразделение-------',reply_markup=keyboard)
    elif m.text =='Прочее':
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name
                    in ['1031']])
        keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name
                    in ['1201']])
        keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name
                    in ['3794']])
        keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name
                    in ['3775']])
        msg = bot.send_message(m.chat.id,'-------Выберите методику-----',reply_markup=keyboard)    
@bot.callback_query_handler(func=lambda c:True)
def inline(c):
    if c.data == 'Общие положения':
        bot.send_document(c.message.chat.id,"BQADAgADNgEAAqZFOEu14-39LThhrAI")
    elif c.data == 'Консультант':
        bot.send_document(c.message.chat.id,"BQADAgADvAEAAodDcUvAqyVLcx-0RwI")
    elif c.data == 'М-р по обслуж':
        bot.send_document(c.message.chat.id,"BQADAgADAwEAAj_5eEtIaxIqjy0xhAI")
    elif c.data == 'Асс-т КМ СБ-Премьер' :
        bot.send_document(c.message.chat.id,"BQADAgADvQEAAodDcUuZe2rQ6xCCfQI")
    elif c.data == 'Сервис-менеджер':
        bot.send_document(c.message.chat.id,"BQADAgADNQEAAqZFOEuzBMNc0oT5OAI")
    elif c.data == 'М-р по продажам':
        bot.send_document(c.message.chat.id,"BQADAgADNwEAAqZFOEvPnvPq3a08AwI")
    elif c.data == 'КМ СБ-Премьер':
        bot.send_document(c.message.chat.id,"BQADAgADOAEAAqZFOEvV4YNH1gMQnQI")
    elif c.data == 'Рук центра ПО':
        bot.send_document(c.message.chat.id,"BQADAgADOQEAAqZFOEvE95CWK4DbygI")
    elif c.data == 'Рук офиса и зам':
        bot.send_document(c.message.chat.id,"BQADAgADOgEAAqZFOEtFQYsVjFQ_kwI")
    elif c.data == 'Работники ПФ':
        bot.send_document(c.message.chat.id,"BQADAgADvgEAAodDcUsdTCi7Mzg2OAI")
    elif c.data == 'Спец по обс кор кл-ов':
        bot.send_document(c.message.chat.id,"BQADAgADvwEAAodDcUubMeWeSNVs2QI")
    elif c.data == 'Зам рука по КБ':
        bot.send_document(c.message.chat.id,"BQADAgADwAEAAodDcUve_U-MzylJCwI")
    elif c.data == 'Распоряжение-420':
          keyboard = types.InlineKeyboardMarkup()
          keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name
                        in ['Распоряжение']])
          keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name
                        in ['ВСП','ОПЕРУ']])
          keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name
                        in ['Прямые продажи','Эквайринг']])
          keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name
                        in ['Партнеры','Платежи']])
          keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name
                        in ['Сбербанк1','Планирование']])
          keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name
                        in ['ЦУСУС','Назад']])
          bot.edit_message_reply_markup(c.message.chat.id,message_id=c.message.message_id,reply_markup=keyboard)    
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
       bot.send_document(c.message.chat.id,"BQADAgADOwEAAqZFOEv1nZqkMLfRoQI")
    elif c.data == 'Рук гр по ПП':
       bot.send_document(c.message.chat.id,"BQADAgADPAEAAqZFOEuTYNlSgvdd2gI")
    elif c.data == 'М-р по пр зарп пр-в':
       bot.send_document(c.message.chat.id,"BQADAgADCwEAAj_5eEuw4BJ8OPbg_wI")
    elif c.data == 'Спец по сопр зар пр-в':
       bot.send_document(c.message.chat.id,"BQADAgADDAEAAj_5eEttmss7n7rrAAEC")
    elif c.data == 'Спец по зарп пр-м':
       bot.send_document(c.message.chat.id,"BQADAgADwQEAAodDcUvijDD0UMRj9gI")
    elif c.data == 'Конс-т по ПФР':
       bot.send_document(c.message.chat.id,"BQADAgADPQEAAqZFOEuSmAoGtiU2wAI")
    elif c.data == 'М-р соц программ':
       bot.send_document(c.message.chat.id,"BQADAgADwgEAAodDcUsQbTnDlvvUDAI")
    elif c.data == 'Нач сек-а по ПФР':
       bot.send_document(c.message.chat.id,"BQADAgADYAEAAkD3OEuNDiHGNVAZeAI")
    elif c.data == 'Рук ВИП ВСП':
       bot.send_document(c.message.chat.id,"BQADAgADPgEAAqZFOEsuCVg_RklpwgI")
    elif c.data == 'Зам рука ВИП ВСП':
       bot.send_document(c.message.chat.id,"BQADAgADEAEAAj_5eEs4lxh4DN7aDwI")
    elif c.data == 'КМ ВИП':
       bot.send_document(c.message.chat.id,"BQADAgADPwEAAqZFOEvcvlxxgB_Z7AI")
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
                        in ['Спец техн подд экв','Лин-Лаб']])
          keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name
                        in ['<==','Приложение_11']])
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
       bot.send_document(c.message.chat.id,"BQADAgADQAEAAqZFOEuf9iAEbNwdbAI")
    elif c.data == 'Спец под-ки прод-ж':
       bot.send_document(c.message.chat.id,"BQADAgADGAEAAj_5eEsvMu2wpAl2RAI")
    elif c.data == 'Спец сервис подд экв':
       bot.send_document(c.message.chat.id,"BQADAgADQQEAAqZFOEuPKMI743JZfgI")
    elif c.data == 'Спец техн подд экв':
       bot.send_document(c.message.chat.id,"BQADAgADQgEAAqZFOEveoZ5JhKdtVQI")
    elif c.data == 'Лин-Лаб':
       bot.send_document(c.message.chat.id,"BQADAgADRgEAAqZFOEuRFPyGHxcENAI")   
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
    elif c.data == 'Назад':
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name
                    in ['Общие положения']])
        keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name
                    in ['Распоряжение-420']])
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
    elif c.data == 'Общие положения.':
       bot.send_document(c.message.chat.id,"BQADAgADKwEAAvp8SEj5YsV_dS1vQwI")
    elif c.data == 'Аппарат ТБ':
       bot.send_document(c.message.chat.id,"BQADAgADLQEAAgwLSUiP4SljCfTQyQI")
       bot.send_document(c.message.chat.id,"BQADAgADLgEAAgwLSUjYT3-ZqvvZwwI")
    elif c.data == 'Малый и микро-бизнес':
       bot.send_document(c.message.chat.id,"BQADAgADLAEAAvp8SEhdZ2nuThsCtwI")
       bot.send_document(c.message.chat.id,"BQADAgADLQEAAvp8SEg9pvsHcmSIbAI")
    elif c.data == 'Крупный и средний бизнес':
       bot.send_document(c.message.chat.id,"BQADAgADLgEAAvp8SEgmEW0CmHyC4AI")
       bot.send_document(c.message.chat.id,"BQADAgADLwEAAgwLSUhVoDTB7zN7DgI")
    elif c.data == 'Клиентские подр-ия':
       bot.send_document(c.message.chat.id,"BQADAgADLwEAAvp8SEhOwZpSe2-gdQI")
       bot.send_document(c.message.chat.id,"BQADAgADMAEAAgwLSUiOMyWUlOmBAQI")
    elif c.data == 'Кредит. подр-я и мон-г залогов':
       bot.send_document(c.message.chat.id,"BQADAgADMAEAAvp8SEhEuTDjMyVrgAI")
       bot.send_document(c.message.chat.id,"BQADAgADMQEAAgwLSUiA_tjfHf_fpAI")
    elif c.data == 'Центр залог экспертизы':
       bot.send_document(c.message.chat.id,"BQADAgADMQEAAvp8SEhdgqC1H3fYOgI")
       bot.send_document(c.message.chat.id,"BQADAgADMgEAAvp8SEhQZXQh07FP0AI")
    elif c.data == 'Транзакц-ый бизнес':
       bot.send_document(c.message.chat.id,"BQADAgADMgEAAgwLSUiR69zK1zvZvgI")
       bot.send_document(c.message.chat.id,"BQADAgADMwEAAgwLSUir_m967CZc7wI")
    elif c.data == 'Центр корп-х решений':
       bot.send_document(c.message.chat.id,"BQADAgADMwEAAvp8SEgzPoXmHstChwI")
       bot.send_document(c.message.chat.id,"BQADAgADNAEAAgwLSUgfd-fbVf1G_wI")
    elif c.data == 'Лин-лаборатория':
       bot.send_document(c.message.chat.id,"BQADAgADNQEAAgwLSUh026pr3vxqPwI")

    elif c.data == 'Физ. лица':
       bot.send_document(c.message.chat.id,"BQADAgADJAEAAgwLSUj3TXHT7BWQQwI")
       bot.send_document(c.message.chat.id,"BQADAgADJQEAAvp8SEhJVnFfClWmSgI")
    elif c.data == 'Юр. Лица':
       bot.send_document(c.message.chat.id,"BQADAgADJgEAAvp8SEhc_sZJ4kdCvwI")
       bot.send_document(c.message.chat.id,"BQADAgADJwEAAvp8SEj-NMRWftYMLwI")   
    elif c.data == 'Распоряжение':
       bot.send_document(c.message.chat.id,"BQADAgADJQEAAgwLSUgUYJNeczIEKwI")
    elif c.data == 'ВСП':
       bot.send_document(c.message.chat.id,"BQADAgADKAEAAvp8SEgHXlhXqWdicAI")
    elif c.data == 'ОПЕРУ':
       bot.send_document(c.message.chat.id,"BQADAgADJgEAAgwLSUj0yE5Go5dxNwI")
    elif c.data == 'Прямые продажи':
       bot.send_document(c.message.chat.id,"BQADAgADJwEAAgwLSUhK2o4cycEj-gI")
    elif c.data == 'Эквайринг':
       bot.send_document(c.message.chat.id,"BQADAgADKQEAAvp8SEg-KzCxFKCV4gI")
    elif c.data == 'Партнеры':
       bot.send_document(c.message.chat.id,"BQADAgADKAEAAgwLSUjrXZ32MM3SjgI")
    elif c.data == 'Платежи':
       bot.send_document(c.message.chat.id,"BQADAgADKQEAAgwLSUiWXKrROJe8YwI")
    elif c.data == 'Сбербанк1':
       bot.send_document(c.message.chat.id,"BQADAgADKgEAAgwLSUjfhzTvddfpjgI")
    elif c.data == 'Планирование':
       bot.send_document(c.message.chat.id,"BQADAgADKgEAAvp8SEg_mSIOr6APFwI")
    elif c.data == 'ЦУСУС':
       bot.send_document(c.message.chat.id,"BQADAgADKwEAAgwLSUhCn7Tb4CcusQI")
    elif c.data == 'Приложение_11':
       bot.send_document(c.message.chat.id,"BQADAgADLAEAAgwLSUi7d33k2UaKjgI")
    elif c.data == 'Руководство':
       bot.send_document(c.message.chat.id,"BQADAgADVwEAAvp8QEjj4Qvpvhe26wI")   
    elif c.data == '1031':
       bot.send_document(c.message.chat.id,"BQADAgADhQEAAgwLQUg68DAuJKLQUQI")
    elif c.data == '1201':
       bot.send_document(c.message.chat.id,"BQADAgADhgEAAgwLQUhFN6udzQKRBAI")
    elif c.data == '3794':
       bot.send_document(c.message.chat.id,"BQADAgADhwEAAgwLQUjpI1_j3shx7AI")
    elif c.data == '3775':
       bot.send_document(c.message.chat.id,"BQADAgADiAEAAgwLQUidEommUSA-jwI")
       bot.send_document(c.message.chat.id,"BQADAgADiQEAAgwLQUhroPfCTGVHlAI")
       bot.send_document(c.message.chat.id,"BQADAgADWAEAAvp8QEhmhGvCGayUKwI") 
       
       
        




        
while True: 
    try:
        bot.polling(none_stop=True)

    except Exception as e:
        print(e)
        time.sleep(15)

  
