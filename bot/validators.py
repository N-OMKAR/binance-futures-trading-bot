def validate_symbol(symbol):

    if not symbol:
        raise ValueError("Symbol cannot be empty")

    return symbol.upper()


def validate_side(side):

    side = side.upper()

    if side not in ["BUY", "SELL"]:
        raise ValueError("Side must be BUY or SELL")

    return side


def validate_order_type(order_type):

    order_type = order_type.upper()

    if order_type not in ["MARKET", "LIMIT", "STOP"]:
        raise ValueError("Order type must be MARKET, LIMIT, or STOP")

    return order_type