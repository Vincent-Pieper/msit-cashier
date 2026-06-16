


def get_total_price():
    total_price_before_vat = input("please type in the full amount: ")
    if total_price_before_vat[-1] == "$":
        stripped_total_price_before_vat = total_price_before_vat[:-1]
        stripped_total_price_before_vat_float = float(stripped_total_price_before_vat)
    else:
        stripped_total_price_before_vat_float = float(total_price_before_vat)

    return stripped_total_price_before_vat_float


def add_taxes(total_price_float, vat=11.5):
    price_after_vat = total_price_float * (1+vat/100)
    vat_amount = price_after_vat - total_price_float
    return price_after_vat, vat_amount


def get_amount_received_and_calculate_change(price_after_vat):
    cash_received = float(input("Please input the amount of cash paid: "))
    change = cash_received - price_after_vat
    return cash_received, change


def print_vat_and_change_statement(vat_amount, price_after_vat, cash_received, change):
    print(f"The total amount of your shopping was {price_after_vat}$ after {vat_amount}$ was applied. You paid {cash_received}$ and received {change}$ in change")


def main():
    total_price_float = get_total_price()
    price_after_vat, vat_amount = add_taxes(total_price_float)
    cash_received, change = get_amount_received_and_calculate_change(price_after_vat)
    print_vat_and_change_statement(vat_amount, price_after_vat, cash_received, change)


if __name__ == "__main__":
    main()