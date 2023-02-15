# simple-parser

This is simple parser for website [cs.money](https://cs.money/market/buy/). <br>
Nowadays, games have become not only a way 
of entertainment but also an income for many players,
on this site you can buy and sell skins from the
game **Counter Strike: Global Offensive**.

This parser allows you to download the necessary
information for the required category in a couple
of seconds, in order to prescribe the necessary
filters, just change the url line and you will 
receive a selection for the required request.


# You can also download this project:

Go to https://github.com/maxitoska/simple-parser click on the button Code, And choose the download method that is convenient for you. You can download it as a zip file, open it with visual studio, GitHub Desktop, or clone it to your computer.

Prepare the project

Fork the repo (GitHub repository)

Clone the forked repo

git clone https://github.com/maxitoska/simple-parser.git

You can get the link by clicking the Clone or download button in your repo

Open the project folder in your IDE

Open a terminal in the project folder

Create a branch for the solution and switch on it

git checkout -b develop

You can use any other name instead of develop

If you are using PyCharm - it may propose you to automatically create venv for your project and install requirements in it, but if not:

python -m venv venv

venv\Scripts\activate (on Windows)

source venv/bin/activate (on macOS)

pip install -r requirements.txt



# Create the Telegram Bot:

Create your own telegram.bot by using BotFather in search of Telegram,
and use command /newbot to create your Bot`s name and username (follow the prompts of BotFather).

Create file .env

After creation copy your access TOKEN and put it into .env file like: TOKEN = "your token".


# Run Program

Run program with command: python telegram_bot_logic.py

Open your Bot, write command /start to him , and by pressing the category buttons you will get the result.


