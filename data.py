from string import ascii_letters, digits

user_datas = [
    "start",
    "randomness",
    "random_number_input"
]

symbols = list(ascii_letters + digits + "!#$%&?@")

start_text = (
    '<b>🤖 Випадковий Бот 🤖</b>'
    '\n\n⚙ Що ж він вміє:'
    '\n🔢 Згенерувати випадкове число'
    '\n🔐 Згенерувати пароль'
    '\n🗃 Вибрати випадковий варіант зі списку'
    '\n🎲 Кинути кубик'
    '\n<u>🔎 І багато іншого</u>'
    '\n\n🔆 Цей бот абсолютно безкоштовний 🔆'
    '\n\n⬇️ Щоб розпочати натисніть "🌀 Випадковість"'
)

randomness_SelectButton_text = (
    "Вибери потрібну дію, натиснувши на відповідну кнопку що розташована нижче ⬇️"
)

range_input_text = (
    "Введіть діапазон у форматі:"
    "\n<pre>&lt;число1&gt; - &lt;число2&gt;</pre>"
)

password_length_input = "Введіть довжину пароля:"

items_input_text = (
    "Введіть список значень у форматі:"
    "\n<pre>&lt;значення1, значення2, значення3, ... значення&gt;</pre>"
)
