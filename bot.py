from email.message import Message
from aiogram import Bot, Dispatcher, executor, types
import keyboard
import messages
from aiogram.types import ContentType, Message, InputFile, MediaGroup, InputMediaPhoto


TOKEN = '5623610960:AAFqbpgYuc-1kFEkZ_HhZ2138Ftx90pNBsc'
APP_NAME = 'tsarenkoubot'
bot = Bot(TOKEN)
dp = Dispatcher(bot)



@dp.message_handler(commands=['start'])
async def show_conditions(message: types.Message):
    await message.answer(text=messages.start(),
                         reply_markup=keyboard.START)

@dp.message_handler(commands=['conditions'])
async def show_conditions(message: types.Message):
    await message.answer(text=messages.conditions(),
                         reply_markup=keyboard.CONDITIONS)

    
@dp.message_handler(text='pictures')
async def send_album(message: Message):
    album = MediaGroup()
    photo_bytes1 = InputFile(path_or_bytesio='media/content1.jpg')
    photo_bytes2 = InputFile(path_or_bytesio='media/express1.jpg')
    photo_bytes3 = InputFile(path_or_bytesio='media/family1.jpg')
    photo_bytes4 = InputFile(path_or_bytesio='media/food1.jpg')
    photo_bytes5 = InputFile(path_or_bytesio='media/individ2.jpg')
    photo_bytes6 = InputFile(path_or_bytesio='media/love2.jpg')
    photo_bytes7 = InputFile(path_or_bytesio='media/TFP1.jpg')
    
    album.attach_photo(photo=photo_bytes1)
    album.attach_photo(photo=photo_bytes2)
    album.attach_photo(photo=photo_bytes3)
    album.attach_photo(photo=photo_bytes4)
    album.attach_photo(photo=photo_bytes5)
    album.attach_photo(photo=photo_bytes6)
    album.attach_photo(photo=photo_bytes7)
    await message.answer_media_group(media=album)
    await bot.send_media_group
   

@dp.message_handler(commands=['variants'])
async def show_variants(message: types.Message):
    await message.answer(text=messages.variants(),
                         reply_markup=keyboard.VARIANTS)

@dp.message_handler(commands=['express'])
async def show_variants(message: types.Message):
    await message.answer(text=messages.express(),
                        reply_markup=keyboard.EXPRESS)

@dp.message_handler(commands=['content'])
async def show_variants(message: types.Message):
    await message.answer(text=messages.content(),
                         reply_markup=keyboard.CONTENT)

@dp.message_handler(commands=['tfp'])
async def show_variants(message: types.Message):
    await message.answer(text=messages.tfp(),
                         reply_markup=keyboard.TFP)

@dp.message_handler(commands=['food'])
async def show_variants(message: types.Message):
    await message.answer(text=messages.food(),
                         reply_markup=keyboard.FOOD)

@dp.message_handler(commands=['love'])
async def show_variants(message: types.Message):
    await message.answer(text=messages.love(),
                         reply_markup=keyboard.LOVE)

@dp.message_handler(commands=['family'])
async def show_variants(message: types.Message):
    await message.answer(text=messages.family(),
                         reply_markup=keyboard.FAMILY)

@dp.message_handler(commands=['wrt'])
async def show_conditions(message: types.Message):
    await message.answer(text=messages.wrt(),
                         reply_markup=keyboard.WRT)  





@dp.callback_query_handler(text='conditions')
async def process_callback_conditions(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(
        callback_query.from_user.id,
        text=messages.conditions(),
        reply_markup=keyboard.CONDITIONS
    )

@dp.callback_query_handler(text='pictures')
async def send_album(callback_query: types.CallbackQuery):
    album = MediaGroup()
    await bot.answer_callback_query(callback_query.id)
    photo_bytes1 = InputFile(path_or_bytesio='media/content1.jpg')
    photo_bytes2 = InputFile(path_or_bytesio='media/express1.jpg')
    photo_bytes3 = InputFile(path_or_bytesio='media/family1.jpg')
    photo_bytes4 = InputFile(path_or_bytesio='media/food1.jpg')
    photo_bytes5 = InputFile(path_or_bytesio='media/individ2.jpg')
    photo_bytes6 = InputFile(path_or_bytesio='media/love2.jpg')
    photo_bytes7 = InputFile(path_or_bytesio='media/TFP1.jpg')
    
    album.attach_photo(photo=photo_bytes1)
    album.attach_photo(photo=photo_bytes2)
    album.attach_photo(photo=photo_bytes3)
    album.attach_photo(photo=photo_bytes4)
    album.attach_photo(photo=photo_bytes5)
    album.attach_photo(photo=photo_bytes6)
    album.attach_photo(photo=photo_bytes7)
    await bot.send_media_group(
        callback_query.from_user.id,
        album
        )

@dp.callback_query_handler(text='variants')
async def process_callback_conditions(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(
        callback_query.from_user.id,
        text=messages.variants(),
        reply_markup=keyboard.VARIANTS
    )

@dp.callback_query_handler(text='express')
async def process_callback_conditions(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(
        callback_query.from_user.id,
        text=messages.express(),
        reply_markup=keyboard.EXPRESS
    )

@dp.callback_query_handler(text='content')
async def process_callback_variants(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(
        callback_query.from_user.id,
        text=messages.content(),
        reply_markup=keyboard.CONTENT
    )

@dp.callback_query_handler(text='tfp')
async def process_callback_variants(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(
        callback_query.from_user.id,
        text=messages.tfp(),
        reply_markup=keyboard.TFP
    )

@dp.callback_query_handler(text='food')
async def process_callback_variants(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(
        callback_query.from_user.id,
        text=messages.food(),
        reply_markup=keyboard.FOOD
    )

@dp.callback_query_handler(text='individual')
async def process_callback_variants(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(
        callback_query.from_user.id,
        text=messages.individual(),
        reply_markup=keyboard.INDIVIDUAL
    )

@dp.callback_query_handler(text='love')
async def process_callback_variants(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(
        callback_query.from_user.id,
        text=messages.love(),
        reply_markup=keyboard.LOVE
    )

@dp.callback_query_handler(text='family')
async def process_callback_variants(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(
        callback_query.from_user.id,
        text=messages.family(),
        reply_markup=keyboard.FAMILY
    )    

@dp.callback_query_handler(text='wrt')
async def process_callback_variants(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(
        callback_query.from_user.id,
        text=messages.wrt(),
        reply_markup=keyboard.WRT
    )



# ----------------------------------------------




@dp.message_handler(text='photo1')
async def send_album(message: Message):
    album1 = MediaGroup()
    photo_bytes1 = InputFile(path_or_bytesio='media/content1.jpg')
    photo_bytes2 = InputFile(path_or_bytesio='media/content2.jpg')
    album1.attach_photo(photo=photo_bytes1)
    album1.attach_photo(photo=photo_bytes2)
    await message.answer_media_group(media=album1)

@dp.message_handler(text='photo2')
async def send_album(message: Message):
    album2 = MediaGroup()
    photo_bytes1 = InputFile(path_or_bytesio='media/express1.jpg')
    photo_bytes2 = InputFile(path_or_bytesio='media/express2.jpg')
    album2.attach_photo(photo=photo_bytes1)
    album2.attach_photo(photo=photo_bytes2)
    await message.answer_media_group(media=album2)

@dp.message_handler(text='photo3')
async def send_album(message: Message):
    album3 = MediaGroup()
    photo_bytes1 = InputFile(path_or_bytesio='media/family1.jpg')
    photo_bytes2 = InputFile(path_or_bytesio='media/family2.jpg')
    album3.attach_photo(photo=photo_bytes1)
    album3.attach_photo(photo=photo_bytes2)
    await message.answer_media_group(media=album3)  

@dp.message_handler(text='photo4')
async def send_album(message: Message):
    album4 = MediaGroup()
    photo_bytes1 = InputFile(path_or_bytesio='media/food1.jpg')
    photo_bytes2 = InputFile(path_or_bytesio='media/food2.jpg')
    album4.attach_photo(photo=photo_bytes1)
    album4.attach_photo(photo=photo_bytes2)
    await message.answer_media_group(media=album4) 

@dp.message_handler(text='photo5')
async def send_album(message: Message):
    album5 = MediaGroup()
    photo_bytes1 = InputFile(path_or_bytesio='media/individ1.jpg')
    photo_bytes2 = InputFile(path_or_bytesio='media/individ2.jpg')
    album5.attach_photo(photo=photo_bytes1)
    album5.attach_photo(photo=photo_bytes2)
    await message.answer_media_group(media=album5) 

@dp.message_handler(text='photo6')
async def send_album(message: Message):
    album6 = MediaGroup()
    photo_bytes1 = InputFile(path_or_bytesio='media/love1.jpg')
    photo_bytes2 = InputFile(path_or_bytesio='media/love2.jpg')
    album6.attach_photo(photo=photo_bytes1)
    album6.attach_photo(photo=photo_bytes2)
    await message.answer_media_group(media=album6) 

@dp.message_handler(text='photo7')
async def send_album(message: Message):
    album7 = MediaGroup()
    photo_bytes1 = InputFile(path_or_bytesio='media/TFP1.jpg')
    photo_bytes2 = InputFile(path_or_bytesio='media/TFP2.jpg')
    album7.attach_photo(photo=photo_bytes1)
    album7.attach_photo(photo=photo_bytes2)
    await message.answer_media_group(media=album7)  



@dp.callback_query_handler(text='photo1')
async def process_callback_variants(callback_query: types.CallbackQuery):
    album1 = MediaGroup()
    photo_bytes1 = InputFile(path_or_bytesio='media/content1.jpg')
    photo_bytes2 = InputFile(path_or_bytesio='media/content2.jpg')
    album1.attach_photo(photo=photo_bytes1)
    album1.attach_photo(photo=photo_bytes2)
    await bot.send_media_group(
        callback_query.from_user.id,
        album1
    )    

@dp.callback_query_handler(text='photo2')
async def process_callback_variants(callback_query: types.CallbackQuery):
    album2 = MediaGroup()
    await bot.answer_callback_query(callback_query.id)
    photo_bytes1 = InputFile(path_or_bytesio='media/express1.jpg')
    photo_bytes2 = InputFile(path_or_bytesio='media/express2.jpg')
    album2.attach_photo(photo=photo_bytes1)
    album2.attach_photo(photo=photo_bytes2)
    await bot.send_media_group(
        callback_query.from_user.id,
        album2
    )

@dp.callback_query_handler(text='photo3')
async def process_callback_variants(callback_query: types.CallbackQuery):
    album3 = MediaGroup()
    photo_bytes1 = InputFile(path_or_bytesio='media/family1.jpg')
    photo_bytes2 = InputFile(path_or_bytesio='media/family2.jpg')
    album3.attach_photo(photo=photo_bytes1)
    album3.attach_photo(photo=photo_bytes2) 
    await bot.send_media_group(
        callback_query.from_user.id,
        album3
    )    

@dp.callback_query_handler(text='photo4')
async def process_callback_variants(callback_query: types.CallbackQuery):
    album4 = MediaGroup()
    photo_bytes1 = InputFile(path_or_bytesio='media/food1.jpg')
    photo_bytes2 = InputFile(path_or_bytesio='media/food2.jpg')
    album4.attach_photo(photo=photo_bytes1)
    album4.attach_photo(photo=photo_bytes2)
    await bot.send_media_group(
        callback_query.from_user.id,
        album4
    )        

@dp.callback_query_handler(text='photo5')
async def process_callback_variants(callback_query: types.CallbackQuery):
    album5 = MediaGroup()
    photo_bytes1 = InputFile(path_or_bytesio='media/individ1.jpg')
    photo_bytes2 = InputFile(path_or_bytesio='media/individ2.jpg')
    album5.attach_photo(photo=photo_bytes1)
    album5.attach_photo(photo=photo_bytes2)
    await bot.send_media_group(
        callback_query.from_user.id,
        album5
    )     

@dp.callback_query_handler(text='photo6')
async def process_callback_variants(callback_query: types.CallbackQuery):
    album6 = MediaGroup()
    photo_bytes1 = InputFile(path_or_bytesio='media/love1.jpg')
    photo_bytes2 = InputFile(path_or_bytesio='media/love2.jpg')
    album6.attach_photo(photo=photo_bytes1)
    album6.attach_photo(photo=photo_bytes2)
    await bot.send_media_group(
        callback_query.from_user.id,
        album6
    )     

@dp.callback_query_handler(text='photo7')
async def process_callback_variants(callback_query: types.CallbackQuery):
    album7 = MediaGroup()
    photo_bytes1 = InputFile(path_or_bytesio='media/TFP1.jpg')
    photo_bytes2 = InputFile(path_or_bytesio='media/TFP2.jpg')
    album7.attach_photo(photo=photo_bytes1)
    album7.attach_photo(photo=photo_bytes2)
    await bot.send_media_group(
        callback_query.from_user.id,
        album7
    )     



if __name__ == "__main__":
    print("Bot started successfuly!")
    executor.start_polling(dp)



