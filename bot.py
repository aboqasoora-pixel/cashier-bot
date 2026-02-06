from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# التوكن رح نحطه لاحقًا داخل Render بشكل آمن
TOKEN = "PUT_YOUR_TOKEN_HERE"


def main_menu():
    keyboard = [
        [InlineKeyboardButton("⚡ شحن وسحب حساب Ichancy", callback_data="main_charge")],

        [
            InlineKeyboardButton("📩 سحب حوالة", callback_data="withdraw"),
            InlineKeyboardButton("📩 شحن البوت", callback_data="charge"),
        ],

        [InlineKeyboardButton("👤 معلومات الملف الشخصي", callback_data="profile")],

        [
            InlineKeyboardButton("🏆 أكواد الجوائز", callback_data="codes"),
            InlineKeyboardButton("🎁 إهداء الرصيد", callback_data="gift"),
        ],

        [InlineKeyboardButton("💸 الاسترداد الخاص بالبوت", callback_data="refund")],

        [
            InlineKeyboardButton("🔁 استرداد حوالة", callback_data="refund_money"),
            InlineKeyboardButton("✉️ تواصل مع الدعم", callback_data="support"),
        ],

        [InlineKeyboardButton("👥 برنامج الإحالات", callback_data="referrals")],
        [InlineKeyboardButton("🗄 عرض السجل المالي", callback_data="history")],
    ]

    return InlineKeyboardMarkup(keyboard)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "أهلاً بك 👋\nاختر من القائمة:",
        reply_markup=main_menu()
    )


async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "withdraw":
        await query.message.reply_text("📩 أدخل مبلغ الحوالة للسحب:")
    elif query.data == "charge":
        await query.message.reply_text("💳 أدخل مبلغ شحن البوت:")
    elif query.data == "support":
        await query.message.reply_text("✉️ الدعم: @SupportUser")
    else:
        await query.message.reply_text("🔘 هذا الخيار قيد التطوير...")


def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(buttons))

    app.run_polling()


if __name__ == "__main__":
    main()
