def get_total_price():
    total_price_before_vat = input("please type in the full amount: ")
    if total_price_before_vat[-1] == "$":
        stripped_total_price_before_vat = total_price_before_vat[:-1]
        stripped_total_price_before_vat_float = float(stripped_total_price_before_vat)
    else:
        stripped_total_price_before_vat_float = float(total_price_before_vat)
    total_price_int = round(stripped_total_price_before_vat_float * 100) # makes float to int full amount in cents
    return total_price_int


def add_taxes(total_price_int, vat=11.5):
    price_after_vat_int = round(total_price_int * (1+vat/100))
    vat_amount = price_after_vat_int - total_price_int
    return price_after_vat_int, vat_amount

def get_amount_received_and_calculate_change(price_after_vat_int):
    cash_received_before_cleanup = input("Please input the amount of cash paid: ")

    if cash_received_before_cleanup[-1] == "$":
        cash_received_after_cleanup = cash_received_before_cleanup[:-1]
    else:
        cash_received_after_cleanup = cash_received_before_cleanup

    cash_received_float = float(cash_received_after_cleanup) # makes str to float so we can get the full cents amount
    cash_received_int = round(cash_received_float * 100) # makes float to int full amount in cents

    if cash_received_int < price_after_vat_int:
        print("the amount you paid doesnt cover your shopping cart. please return some items and chack back later.")
        return None, None
    change = cash_received_int - price_after_vat_int
    return cash_received_int, change


def print_vat_and_change_statement(vat_amount, price_after_vat_int, cash_received_int, change):
    print(f"The total amount of your shopping was {price_after_vat_int/100:.2f}$ after {vat_amount/100:.2f}$ was applied. You paid {cash_received_int/100:.2f}$ and received {change/100:.2f}$ in change")


def main():
    total_price_int = get_total_price()
    price_after_vat_int, vat_amount = add_taxes(total_price_int)
    cash_received_int, change = get_amount_received_and_calculate_change(price_after_vat_int)
    if change is None:
        return
    print_vat_and_change_statement(vat_amount, price_after_vat_int, cash_received_int, change)


if __name__ == "__main__":
    main()