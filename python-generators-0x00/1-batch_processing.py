from seed import connect_to_prodev

def stream_users_in_batches(batch_size):
    """Yields rows in batches from user_data table"""
    connection = connect_to_prodev()
    cursor = connection.cursor(dictionary=True)
    offset = 0

    while True:
        cursor.execute("SELECT * FROM user_data LIMIT %s OFFSET %s", (batch_size, offset))
        rows = cursor.fetchall()
        if not rows:
            break
        offset += batch_size
        yield rows  # ✅ هذا هو المطلوب
    cursor.close()
    connection.close()

def batch_processing(batch_size):
    """Processes each batch and prints users over age 25"""
    for batch in stream_users_in_batches(batch_size):
        for user in batch:
            if user['age'] > 25:
                print(user)
