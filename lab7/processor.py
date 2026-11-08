def parse_coins(coins_csv):
    """
    Parses a comma-separated string of coin values into a list of integers.
    Safely handles None, empty strings, non-numeric values, and delimiter anomalies.
    """
    if not isinstance(coins_csv, str):
        return []
    coins = []
    for c in coins_csv.split(','):
        token = c.strip()
        if not token:
            continue
        try:
            coins.append(int(token))
        except (ValueError, TypeError):
            continue
    return coins

def slot_position(code):
    """
    Converts a vending machine slot code (e.g. 'B7') into zero-indexed (row, column).
    Row is determined by letter ('A'->0, 'B'->1, ...).
    Column is determined by integer minus 1.
    Safely handles None, empty strings, malformed codes, and boundary conditions.
    """
    if not isinstance(code, str):
        return None
    code = code.strip()
    if len(code) < 2:
        return None
    first_char = code[0].upper()
    if not ('A' <= first_char <= 'Z'):
        return None
    try:
        col_num = int(code[1:])
        if col_num < 1:
            return None
        row = ord(first_char) - ord('A')
        column = col_num - 1
        return row, column
    except (ValueError, TypeError):
        return None

def change_due(payment):
    """
    Calculates change due from a 'paid/price' format string (e.g. '200/150').
    Returns string representation of change in five-coin units.
    Safely handles invalid formats, non-numeric values, underpayments, and unexpected types.
    """
    if not isinstance(payment, str):
        return "0 five-coins"
    parts = payment.split('/')
    if len(parts) != 2:
        return "0 five-coins"
    try:
        paid = int(parts[0].strip())
        price = int(parts[1].strip())
        change = paid - price
        if change <= 0:
            return "0 five-coins"
        return f"{change // 5} five-coins"
    except (ValueError, TypeError):
        return "0 five-coins"

def main():
    print("==== Running parse_coins ====")
    user_input = input("Enter coin values as CSV (e.g. 5,10,25): ")
    result = parse_coins(user_input)
    print("Coins:", result)

    print("\n==== Running slot_position ====")
    user_input = input("Enter a slot code (e.g. B7): ")
    result = slot_position(user_input)
    print("Row and Column:", result)

    print("\n==== Running change_due ====")
    user_input = input("Enter paid/price (e.g. 200/150): ")
    result = change_due(user_input)
    print("Change Due:", result)

if __name__ == "__main__":
    main()
