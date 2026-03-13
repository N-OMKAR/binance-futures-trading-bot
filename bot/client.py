import argparse
from bot.orders import (
    place_market_order,
    place_limit_order,
    place_stop_order
)

from bot.validators import (
    validate_symbol,
    validate_side,
    validate_order_type
)

from bot.logging_config import logger


def main():

    parser = argparse.ArgumentParser(
        description="Binance Futures Testnet Trading Bot"
    )

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", required=True, type=float)

    parser.add_argument("--price", type=float)
    parser.add_argument("--stop_price", type=float)

    args = parser.parse_args()

    try:

        symbol = validate_symbol(args.symbol)
        side = validate_side(args.side)
        order_type = validate_order_type(args.type)

        print("\nOrder Request")
        print("-------------------")
        print(f"Symbol: {symbol}")
        print(f"Side: {side}")
        print(f"Type: {order_type}")
        print(f"Quantity: {args.quantity}")
        print(f"Price: {args.price}")
        print(f"Stop Price: {args.stop_price}")

        if order_type == "MARKET":

            order = place_market_order(
                symbol,
                side,
                args.quantity
            )

        elif order_type == "LIMIT":

            if args.price is None:
                raise ValueError("LIMIT order requires --price")

            order = place_limit_order(
                symbol,
                side,
                args.quantity,
                args.price
            )

        else:

            if args.price is None or args.stop_price is None:
                raise ValueError("STOP order requires --price and --stop_price")

            order = place_stop_order(
                symbol,
                side,
                args.quantity,
                args.price,
                args.stop_price
            )

        print("\nOrder Response")
        print("-------------------")
        print("Order ID:", order.get("orderId"))
        print("Status:", order.get("status"))
        print("Executed Qty:", order.get("executedQty"))
        print("Avg Price:", order.get("avgPrice"))

        print("\nOrder placed successfully")

        logger.info(order)

    except Exception as e:

        logger.error(str(e))
        print("Error:", str(e))


if __name__ == "__main__":
    main()