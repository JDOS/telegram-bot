from telegram.ext import Updater, CommandHandler
from telegram import ChatMemberAdministrator, ChatMemberOwner
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv("TOKEN")


from telegram.ext import ApplicationBuilder, CommandHandler

async def start(update, context):
    await update.message.reply_text('Olá! Eu sou o Snail Bot 🐌')

async def ola(update, context):
    await update.message.reply_text('🐌 Olá!!')


async def limpar(update, context):
    chat_id = update.effective_chat.id

    # Obtém o status do bot no grupo
    bot_member = await context.bot.get_chat_member(chat_id, context.bot.id)

    # Verifica se é admin com permissão de apagar mensagens
    if not isinstance(bot_member, (ChatMemberAdministrator, ChatMemberOwner)) or not bot_member.can_delete_messages:
        await update.message.reply_text("❌ Eu preciso ser administrador com permissão de apagar mensagens.")
        return

    # Apaga as últimas 20 mensagens do chat
    try:
        async for msg in context.bot.get_chat_history(chat_id, limit=20):
            try:
                await context.bot.delete_message(chat_id, msg.message_id)
            except:
                continue

        await update.message.reply_text("🧹 Limpei as últimas 20 mensagens!")
    except Exception as e:
        await update.message.reply_text(f"⚠️ Ocorreu um erro: {str(e)}")
app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("ola", ola))
app.add_handler(CommandHandler("limpar", limpar))


app.run_polling()
