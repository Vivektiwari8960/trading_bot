# Trading Bot (Binance Futures - Mock)

## Features
- Place MARKET and LIMIT orders
- Supports BUY and SELL
- CLI-based input
- Input validation
- Logging support

## Tech Stack
- Python
- argparse

## How to Run

### Install dependencies
pip install -r requirements.txt

### Run Market Order
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01

### Run Limit Order
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.01 --price 50000

## Output Example
✅ ORDER SUCCESS  
{ "orderId": 123456, "status": "FILLED" }

## Note
Due to testnet access restrictions, this version uses mock responses.
The structure is ready for real Binance API integration.
