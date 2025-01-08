import requests
import telebot

# Replace 'YOUR_TELEGRAM_BOT_TOKEN' with your actual bot token
TELEGRAM_BOT_TOKEN = '8019566249:AAGdifu0FAWxx2KKMNYTQUnSmiAE56AfLrM'
bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

def get_proxies(protocol):
    # Fetch proxies from ProxyScrape based on the requested protocol
    url = f'https://api.proxyscrape.com/v2/?request=displayproxies&protocol={protocol}'
    proxies = requests.get(url).text.splitlines()
    return proxies

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Welcome! Use /socks4, /socks5, or /https to get proxies.\nBy- @akarshxo')

@bot.message_handler(commands=['socks4'])
def socks4(message):
    proxies = get_proxies('socks4')
    send_proxies(message, proxies, 'SOCKS4')

@bot.message_handler(commands=['socks5'])
def socks5(message):
    proxies = get_proxies('socks5')
    send_proxies(message, proxies, 'SOCKS5')

@bot.message_handler(commands=['https'])
def https(message):
    proxies = get_proxies('https')
    send_proxies(message, proxies, 'HTTPS')

def send_proxies(message, proxies, protocol):
    if proxies:
        # Create a text file with the proxies
        filename = f'{protocol.lower()}_proxies.txt'
        with open(filename, 'w') as file:
            file.write("\n".join(proxies))
        
        # Send the file to the user
        with open(filename, 'rb') as file:
            bot.send_document(chat_id=message.chat.id, document=file, caption=f'Here are the {protocol} proxies:\nJoin @CCXD4RK for more')
    else:
        bot.reply_to(message, f'No {protocol} proxies found.')

def main():
    # Start polling the bot
    bot.polling()

if __name__ == '__main__':
    main()
