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
                    in ['Консультант','М-р по обслуж']])
        keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name
                    in ['Сервис-менеджер','М-р по продажам']])
        keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name
                    in ['КМ СБ-Премьер','Рук ЦПО']])
        keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name
                    in ['РВСП(ЗРВСП)','Работники ПФ']])
        keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name
                    in ['Спец по ПП','=>']])
        msg = bot.send_message(m.chat.id,'-----------Выберите должность----------',reply_markup=keyboard)
        
    elif m.text =='Кор.Блок':
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name
                    in ['4440-3']])
        keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name
                    in ['Часть 1.1 Соот-я весов']])
        keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name
                    in ['Часть 1.2 Шкалы 5+']])
        keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name
                    in ['Часть 1.3 Цели КИБ']])
        keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name
                    in ['Часть 1.4 Особ-ти тер КИБ']])
        keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name
                    in ['Часть 3.1 Цели ММБ']])
        keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name
                    in ['Часть 4.1 Цели КПК']])
        keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name
                    in ['->']])
        msg = bot.send_message(m.chat.id,'--------Выберите приложение-------',reply_markup=keyboard)
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
        keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name
                    in ['3333']])
        msg = bot.send_message(m.chat.id,'-------Выберите методику-----',reply_markup=keyboard)    
@bot.callback_query_handler(func=lambda c:True)
def inline(c):
    if c.data == 'Общие положения':
        bot.send_document(c.message.chat.id,"BQADAgADCQQAAoDWcUh0BszbndALtQI")
    elif c.data == 'Консультант':
        bot.send_document(c.message.chat.id,"BQADAgADlwMAAkcYaUg8ml6Rk0XUSAI")
    elif c.data == 'М-р по обслуж':
        bot.send_document(c.message.chat.id,"BQADAgADmAMAAkcYaUh9I15TxkUaaQI")
    elif c.data == 'Сервис-менеджер':
        bot.send_document(c.message.chat.id,"BQADAgADDAQAAoDWcUhGqoT588dGRgI")
    elif c.data == 'М-р по продажам':
        bot.send_document(c.message.chat.id,"BQADAgADmQMAAkcYaUiYTYyoMTDdVgI")
    elif c.data == 'КМ СБ-Премьер':
        bot.send_document(c.message.chat.id,"BQADAgADmwMAAkcYaUj_odC-aO0y1QI")
    elif c.data == 'Рук ЦПО':
        bot.send_document(c.message.chat.id,"BQADAgADnAMAAkcYaUhCq_98VTabIQI")
    elif c.data == 'РВСП(ЗРВСП)':
        bot.send_document(c.message.chat.id,"BQADAgADnQMAAkcYaUgHVhUFSWnDLQI")
    elif c.data == 'Работники ПФ':
        bot.send_document(c.message.chat.id,"BQADAgADngMAAkcYaUjvZ-M7JuIFgwI")
    elif c.data == 'Спец по ПП':
       bot.send_document(c.message.chat.id,"BQADAgADoAMAAkcYaUgvltegNm-eRQI")

    elif c.data == '=>':
          keyboard = types.InlineKeyboardMarkup()
          keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name
                        in ['М-р по продаже ЗП','Конс-т ПФР']])
          keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name
                        in ['Нач сектора ПФР','Рук ВИП ВСП']])
          keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name
                        in ['КМ ВИП','Фин советник']])
          keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name
                        in ['М-р по пр экв','Спец сервис подд экв']])
          keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name
                        in ['Спец техн подд экв','Долж-ти по норм-ву']])
          keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name
                        in ['<=','==>']])
          bot.edit_message_reply_markup(c.message.chat.id,message_id=c.message.message_id,reply_markup=keyboard)

       
    elif c.data == 'М-р по продаже ЗП':
       bot.send_document(c.message.chat.id,"BQADAgADoQMAAkcYaUjyLmKQlpjr_AI")
    elif c.data == 'Конс-т ПФР':
       bot.send_document(c.message.chat.id,"BQADAgADogMAAkcYaUhsy2nK2mUTBAI")
    elif c.data == 'Нач сектора ПФР':
       bot.send_document(c.message.chat.id,"BQADAgADowMAAkcYaUhMY5caU-b68gI")                          
    elif c.data == 'Рук ВИП ВСП':
       bot.send_document(c.message.chat.id,"BQADAgADEQQAAoDWcUg6Bqmx2kgTxAI")
    elif c.data == 'Фин советник':
       bot.send_document(c.message.chat.id,"BQADAgADpAMAAkcYaUjcD1E8RX8peQI")                                   
    elif c.data == 'КМ ВИП':
       bot.send_document(c.message.chat.id,"BQADAgADpQMAAkcYaUgDEBsoZ_vFkQI")
    elif c.data == 'М-р по пр экв':
       bot.send_document(c.message.chat.id,"BQADAgADpwMAAkcYaUjPgCaWfU3JdQI")
    elif c.data == 'Спец сервис подд экв':
       bot.send_document(c.message.chat.id,"BQADAgADqwIAAvFhcUhNCMz9B4VmDQI")                                     
    elif c.data == 'Спец техн подд экв':
       bot.send_document(c.message.chat.id,"BQADAgADqAMAAkcYaUhcu0PxXUvOFgI")
    elif c.data == 'Долж-ти по норм-ву':
       bot.send_document(c.message.chat.id,"BQADAgADrgIAAvFhcUhVnW15yM3ZZgI")
                                         
    elif c.data == '==>':
          keyboard = types.InlineKeyboardMarkup()
          keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name
                        in ['Расчет УП','Лин-Лаб']])
          keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name
                        in ['<==','Приложение_11']])
          bot.edit_message_reply_markup(c.message.chat.id,message_id=c.message.message_id,reply_markup=keyboard)
    
    elif c.data == 'Лин-Лаб':
       bot.send_document(c.message.chat.id,"BQADAgADRgEAAqZFOEuRFPyGHxcENAI")
     
    elif c.data == 'Расчет УП':
       bot.send_document(c.message.chat.id,"BQADAgADrwIAAvFhcUg_C7wPOH488wI")
    elif c.data == 'Приложение_11':
       bot.send_document(c.message.chat.id,"BQADAgADLAEAAgwLSUi7d33k2UaKjgI")  
       
    elif c.data == '<==':
          keyboard = types.InlineKeyboardMarkup()
          keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name
                        in ['М-р по продаже ЗП','Конс-т ПФР']])
          keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name
                        in ['Нач сектора ПФР','Рук ВИП ВСП']])
          keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name
                        in ['КМ ВИП','Фин советник']])
          keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name
                        in ['М-р по пр экв','Спец сервис подд экв']])
          keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name
                        in ['Спец техн подд экв','Долж-ти по норм-ву']])
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
                    in ['Сервис-менеджер','М-р по продажам']])
        keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name
                    in ['КМ СБ-Премьер','Рук ЦПО']])
        keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name
                    in ['РВСП(ЗРВСП)','Работники ПФ']])
        keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name
                    in ['Спец по ПП','=>']])
        bot.edit_message_reply_markup(c.message.chat.id,message_id=c.message.message_id,reply_markup=keyboard)
        
    elif c.data == '->':
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name
                    in ['Часть 5.1 Клиент-ие подр-я']])
        keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name
                    in ['Часть 6.1 Кредит-ые подр-я']])
        keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name
                    in ['Часть 7.1 Цели ПЦП ЦЗЭ']])
        keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name
                    in ['Часть 8.1 Транз-ые подр-я']])
        keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name
                    in ['Часть 9.2 Цели ПЦП ЦКР']])
        keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name
                    in ['<-']])
        bot.edit_message_reply_markup(c.message.chat.id,message_id=c.message.message_id,reply_markup=keyboard)
    elif c.data == '<-':      
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name
                    in ['4440-3']])
        keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name
                    in ['Часть 1.1 Соот-я весов']])
        keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name
                    in ['Часть 1.2 Шкалы 5+']])
        keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name
                    in ['Часть 1.3 Цели КИБ']])
        keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name
                    in ['Часть 1.4 Особ-ти тер КИБ']])
        keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name
                    in ['Часть 3.1 Цели ММБ']])
        keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name
                    in ['Часть 4.1 Цели КПК']])
        keyboard.add(*[types.InlineKeyboardButton(text=name,callback_data=name) for name
                    in ['->']])
        bot.edit_message_reply_markup(c.message.chat.id,message_id=c.message.message_id,reply_markup=keyboard)

    
    elif c.data == '4440-3':
       bot.send_document(c.message.chat.id,"BQADAgADQgMAAkcYcUiG0SIf2d4PHQI")
    elif c.data == 'Часть 1.1 Соот-я весов':
       bot.send_document(c.message.chat.id,"BQADAgADQwMAAkcYcUiwPGexBvGQNgI")
    elif c.data == 'Часть 1.2 Шкалы 5+':
       bot.send_document(c.message.chat.id,"BQADAgADRAMAAkcYcUgE39Kt6OIM2wI")
    elif c.data == 'Часть 1.3 Цели КИБ':
       bot.send_document(c.message.chat.id,"BQADAgADRQMAAkcYcUjOcwm__egJYgI")
    elif c.data == 'Часть 1.4 Особ-ти тер КИБ':
       bot.send_document(c.message.chat.id,"BQADAgADywIAAvFhcUhzvy_fkbPpXAI")
    elif c.data == 'Часть 3.1 Цели ММБ':
       bot.send_document(c.message.chat.id,"BQADAgADzAIAAvFhcUjb8wdK8-ZyhwI")
    elif c.data == 'Часть 4.1 Цели КПК':
       bot.send_document(c.message.chat.id,"BQADAgADRwMAAkcYcUhldT4332rEcQI")
    elif c.data == 'Часть 5.1 Клиент-ие подр-я':
       bot.send_document(c.message.chat.id,"BQADAgADzgIAAvFhcUhyi5j921vjZAI")
    elif c.data == 'Часть 6.1 Кредит-ые подр-я':
       bot.send_document(c.message.chat.id,"BQADAgAD0QIAAvFhcUhTLMdNphzo9gI")
    elif c.data == 'Часть 7.1 Цели ПЦП ЦЗЭ':
       bot.send_document(c.message.chat.id,"BQADAgAD0wIAAvFhcUiHjQv_NPkH5AI")
    elif c.data == 'Часть 8.1 Транз-ые подр-я':
       bot.send_document(c.message.chat.id,"BQADAgAD1QIAAvFhcUiv8VXZuXAJRgI")
    elif c.data == 'Часть 9.2 Цели ПЦП ЦКР':
       bot.send_document(c.message.chat.id,"BQADAgADSQMAAkcYcUinNlmFIr32XAI")

    elif c.data == 'Физ. лица':
       bot.send_document(c.message.chat.id,"BQADAgADTAMAAkcYcUhkjYOSmMm6XgI")
       bot.send_document(c.message.chat.id,"BQADAgADTQMAAkcYcUi49Y7pHN-J2gI")
    elif c.data == 'Юр. Лица':
       bot.send_document(c.message.chat.id,"BQADAgADSgMAAkcYcUh1kUfhFcvC3wI")
       bot.send_document(c.message.chat.id,"BQADAgADSwMAAkcYcUh803ugo9I2nwI")   
     
    elif c.data == '1031':
       bot.send_document(c.message.chat.id,"BQADAgADkAMAAkcYaUhh0ksgLc-APgI")
    elif c.data == '1201':
       bot.send_document(c.message.chat.id,"BQADAgADjwMAAkcYaUjGPrrfgMwmyAI")
    elif c.data == '3794':
       bot.send_document(c.message.chat.id,"BQADAgADhwEAAgwLQUjpI1_j3shx7AI")
    elif c.data == '3775':
       bot.send_document(c.message.chat.id,"BQADAgADiAEAAgwLQUidEommUSA-jwI")
       bot.send_document(c.message.chat.id,"BQADAgADiQEAAgwLQUhroPfCTGVHlAI")
       bot.send_document(c.message.chat.id,"BQADAgADWAEAAvp8QEhmhGvCGayUKwI") 
    elif c.data == '3333':
       bot.send_document(c.message.chat.id,"BQADAgADkwMAAkcYaUhFEeX_bsIoVQI")   
       bot.send_document(c.message.chat.id,"BQADAgADlAMAAkcYaUh4-2aT3K8IIQI")
        




        
while True: 
    try:
        bot.polling(none_stop=True)

    except Exception as e:
        print(e)
        time.sleep(15)

  
