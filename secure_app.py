!/usr/bin/env python3
"""
SECURE APPLICATION - Security Best Practices
"""

import sqlite3
import subprocess
import re

def login_user_secure(username, password):
    """SECURE: Uses parameterized queries"""
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    # GOOD: Parameterized query prevents SQL injection
    cursor.execute(
        "SELECT * FROM users WHERE username = ? AND password = ?",
        (username, password)
    )
    result = cursor.fetchone()
    conn.close()
    return result

def ping_host_secure(hostname):
    """SECURE: Validates input and uses subprocess list"""
    # GOOD: Validate input
    if not re.match(r'^[a-zA-Z0-9\-\.]+$', hostname):
        print("❌ Invalid hostname")
        return
    
    # GOOD: Using list form of subprocess
    try:
        result = subprocess.run(
            ['ping', '-c', '1', hostname],
            capture_output=True,
            timeout=5
        )
        print(result.stdout.decode())
    except Exception as e:
        print(f"Error: {e}")

def main():
    print("\n" + "="*50)
    print("SECURE APPLICATION - DEMO")
  print("="*50)
    print("\n✅ This application uses security best practices")
    
    # Create database
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)")
    cursor.execute("INSERT OR IGNORE INTO users (id, username, password) VALUES (1, 'admin', 'admin123')")
    cursor.execute("INSERT OR IGNORE INTO users (id, username, password) VALUES (2, 'user', 'password')")
    conn.commit()
    conn.close()
    
    print("\n" + "="*50)
    print("TEST 1: SECURE LOGIN")
    print("="*50)
    print("💡 Try SQL Injection: admin' OR '1'='1")
    
    username = input("\nEnter username: ")
    password = input("Enter password: ")
    
    result = login_user_secure(username, password)
    if result:
        print(f"\n✅ LOGIN SUCCESSFUL! User: {result[1]}")
    else:
        print("\n❌ Login failed")
    
    print("\n" + "="*50)
    print("TEST 2: SECURE PING")
    print("="*50)
    print("💡 Try command injection: 8.8.8.8; whoami")
    
    host = input("\nEnter hostname: ")
    ping_host_secure(host)

if __name__ == "__main__":
    main()


