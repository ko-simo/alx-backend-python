import sqlite3
import functools

# ✅ decorator function
def log_queries():
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # نفترض أن أول argument هو الاستعلام
            query = kwargs.get('query') or (args[0] if args else None)
            print(f"[LOG] Executing SQL query: {query}")
            return func(*args, **kwargs)
        return wrapper
    return decorator

# ✅ Example usage
@log_queries()
def fetch_all_users(query):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

# ✅ Test the decorator
users = fetch_all_users(query="SELECT * FROM users")
print(users)
