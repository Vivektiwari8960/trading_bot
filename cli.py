import argparse
import random

parser = argparse.ArgumentParser()

parser.add_argument("--symbol", required=True)
parser.add_argument("--side", required=True)
parser.add_argument("--type", required=True)
parser.add_argument("--quantity", type=float, required=True)
parser.add_argument("--price", type=float)

args = parser.parse_args()

# Fake order response
order = {
    "orderId": random.randint(100000, 999999),
    "status": "FILLED",
    "executedQty": args.quantity,
    "avgPrice": args.price if args.price else "Market Price"
}

print("\n✅ ORDER SUCCESS")
print(f"Symbol: {args.symbol}")
print(f"Side: {args.side}")
print(f"Type: {args.type}")
print(f"Quantity: {args.quantity}")
print(f"Order ID: {order['orderId']}")
print(f"Status: {order['status']}")
print(f"Executed Qty: {order['executedQty']}")
print(f"Avg Price: {order['avgPrice']}")