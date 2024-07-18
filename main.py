from aiogram import Bot, Dispatcher, types, filters
import asyncio
from pytube import YouTube
import ssl
from aiogram.types import FSInputFile

ssl._create_default_https_context = ssl._create_unverified_context

bot = Bot(token='6459329359:AAG7SCLGzJ99pHdGof0ege9UNWO_OvYV-PY')
dp = Dispatcher(bot=bot)


@dp.message(filters.Command("start"))
async def start_function(message: types.Message):
    await message.answer("Xush kelibsiz youtube botiga. Link jo'natsez man sizga video qilib yozib beraman")


@dp.message()
async def download_function(message: types.Message):
    url = YouTube(url=message.text)
    video = url.streams.get_highest_resolution()
    result = video.download()
    final_result = FSInputFile(result)
    await message.answer_video(video=final_result)


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
