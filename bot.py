from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, BaseFilter
from aiogram.types import Message

from config import BOT_TOKEN, ADMIN_ID


dp = Dispatcher()

class ChatFilter(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        if message.chat.type == "private":
            return True
        return False
    
class AdminFilter(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        return message.from_user.id == ADMIN_ID
    
class NotAdminFilter(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        return message.from_user.id != ADMIN_ID

@dp.message(CommandStart(), ChatFilter())
async def start(message: Message) -> any:
    await message.answer("Hi! Say anything you want and I forward it to admin.")

@dp.message(ChatFilter(), NotAdminFilter())
async def forward_to_admin(message: Message) -> any:
    await message.forward(ADMIN_ID)
    await message.answer("Message sent to admin! Wait for reply.")

@dp.message(AdminFilter())
async def reply(message: Message) -> any:
    if message.reply_to_message:
        target_user_id = message.reply_to_message.forward_from.id

        await message.bot.send_message(target_user_id, message.text)
        await message.answer("Reply sent to user!")
    else:
        await message.answer("Reply directly to user message and then type your response!")

def main() -> any:
    bot = Bot(token=BOT_TOKEN)

    print("Bot is starting...")
    dp.run_polling(bot)

if __name__ == "__main__":
    main()