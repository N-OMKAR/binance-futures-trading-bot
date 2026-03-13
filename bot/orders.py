from bot.client import get_client
from bot.logging_config import logger


def place_market_order(symbol, side, quantity):

    client = get_client()

    logger.info(f"Placing MARKET order {side} {symbol} qty={quantity}")

    order = client.futures_create_order(
        symbol=symbol,
        side=side,
        type="MARKET",
        quantity=quantity
    )

    return order


def place_limit_order(symbol, side, quantity, price):

    client = get_client()

    logger.info(f"Placing LIMIT order {side} {symbol} qty={quantity} price={price}")

    order = client.futures_create_order(
        symbol=symbol,
        side=side,
        type="LIMIT",
        quantity=quantity,
        price=price,
        timeInForce="GTC"
    )

    return order


def place_stop_order(symbol, side, quantity, price, stop_price):

    client = get_client()

    logger.info(f"Placing STOP order {side} {symbol}")

    order = client.futures_create_order(
        symbol=symbol,
        side=side,
        type="STOP",
        quantity=quantity,
        price=price,
        stopPrice=stop_price,
        timeInForce="GTC"
    )

    return order