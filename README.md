# Binance Futures Testnet Trading Bot

This project is a simple Python trading bot that places orders on the Binance Futures Testnet.

## Features

- Place MARKET orders
- Place LIMIT orders
- Supports BUY and SELL
- Command Line Interface (CLI)
- Input validation
- Logging of API requests and responses
- Error handling

## Project Structure

trading_bot
│
├── bot
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   └── logging_config.py
│
├── logs
│
├── cli.py
├── requirements.txt
├── README.md
└── .env

## Setup

1. Clone the repository

2. Install dependencies

pip install -r requirements.txt

3. Create a `.env` file and add your Binance Testnet API keys

API_KEY=your_api_key
API_SECRET=your_secret_key

## Example Usage

### MARKET Order

python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001

### LIMIT Order

python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 60000

## Logs

All API requests and responses are logged in:

logs/trading_bot.log
