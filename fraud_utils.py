def calculate_risk_score(transaction):
    """
    Calculate the risk score based on transaction amount and flags.

    Parameters:
    transaction (dict): A dictionary containing 'amount' and 'flags'.

    Returns:
    int: A risk score between 0 and 100.
    """
    score = 0
    amount = transaction.get('amount', 0)
    flags = transaction.get('flags', [])

    # Apply amount rules
    if amount > 10000:
        score += 25
    elif amount > 5000:
        score += 15
    elif amount > 1000:
        score += 5

    # Apply flag penalties
    penalties = {'dup': 20, 'time': 10, 'split': 10, 'round': 5, 'vendor': 5}
    for flag in flags:
        score += penalties.get(flag, 0)

    return min(max(score, 0), 100)  # Ensure score is within 0-100

def classify_risk(score):
    """
    Classify the risk based on the risk score.

    Parameters:
    score (int): The risk score.

    Returns:
    str: 'High', 'Medium', or 'Low' based on the score range.
    """
    if score >= 70:
        return 'High'
    elif score >= 35:
        return 'Medium'
    else:
        return 'Low'

def parse_date(date_string):
    """
    Parse a date string into a datetime object.

    Parameters:
    date_string (str): The date string to parse.

    Returns:
    datetime: Parsed datetime object.
    """
    from datetime import datetime
    return datetime.strptime(date_string, '%Y-%m-%d')

def format_date(date):
    """
    Format a datetime object into a string.

    Parameters:
    date (datetime): The datetime object to format.

    Returns:
    str: Formatted date string in 'YYYY-MM-DD' format.
    """
    return date.strftime('%Y-%m-%d')

def generate_fake_transaction(user_id):
    """
    Generate a sample transaction.

    Parameters:
    user_id (str): The user ID for the transaction.

    Returns:
    dict: A sample transaction dictionary.
    """
    import random
    return {
        'id': random.randint(1000, 9999),
        'userId': user_id,
        'name': 'Sample Transaction',
        'amount': random.randint(100, 15000),
        'flags': random.sample(['dup', 'time', 'split', 'round', 'vendor'], k=random.randint(0, 3)),
        'date': format_date(datetime.now()),
        'score': 0,
        'risk': 'Low'
    }

def generate_batch(num_transactions, user_id):
    """
    Generate a batch of fake transactions.

    Parameters:
    num_transactions (int): The number of transactions to generate.
    user_id (str): The user ID for the transactions.

    Returns:
    list: A list of sample transaction dictionaries.
    """
    return [generate_fake_transaction(user_id) for _ in range(num_transactions)]

def filter_transactions(transactions, risk_level=None, min_amount=0, max_amount=15000):
    """
    Filter transactions based on risk level and amount range.

    Parameters:
    transactions (list): A list of transaction dictionaries.
    risk_level (str): The risk level to filter by ('High', 'Medium', 'Low').
    min_amount (int): Minimum amount for filtering.
    max_amount (int): Maximum amount for filtering.

    Returns:
    list: Filtered list of transactions.
    """
    filtered = []
    for transaction in transactions:
        if (risk_level is None or classify_risk(transaction['score']) == risk_level) and min_amount <= transaction['amount'] <= max_amount:
            filtered.append(transaction)
    return filtered