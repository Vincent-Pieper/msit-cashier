def get_net_price():
    raw_net_price = input("Please type in the full amount: ")

    if raw_net_price[-1] == "$":
        raw_net_price = raw_net_price[:-1]

    net_price_cents = round(float(raw_net_price) * 100)
    return net_price_cents


def add_taxes(net_price_cents, vat=11.5):
    gross_price_cents = round(net_price_cents * (1 + vat / 100))
    vat_cents = gross_price_cents - net_price_cents
    return gross_price_cents, vat_cents


def get_payment_and_change(gross_price_cents):
    raw_payment = input("Please input the amount of cash paid: ")

    if raw_payment[-1] == "$":
        raw_payment = raw_payment[:-1]

    payment_cents = round(float(raw_payment) * 100)

    if payment_cents < gross_price_cents:
        print(
            "The amount you paid doesn't cover your shopping cart. "
            "Please return some items and check back later."
        )
        return None, None

    change_cents = payment_cents - gross_price_cents
    return payment_cents, change_cents


def print_receipt(vat_cents, gross_price_cents, payment_cents, change_cents):
    print(
        f"The gross price of your shopping was {gross_price_cents / 100:.2f}$, "
        f"including {vat_cents / 100:.2f}$ VAT. "
        f"You paid {payment_cents / 100:.2f}$ "
        f"and received {change_cents / 100:.2f}$ in change."
    )


def main():
    net_price_cents = get_net_price()
    gross_price_cents, vat_cents = add_taxes(net_price_cents)
    payment_cents, change_cents = get_payment_and_change(gross_price_cents)

    if change_cents is None:
        return

    print_receipt(
        vat_cents,
        gross_price_cents,
        payment_cents,
        change_cents
    )


if __name__ == "__main__":
    main()