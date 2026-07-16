!/usr/bin/env python3
"""
VULNERABLE WEB APPLICATION - Security Testing Only
"""

import sqlite3
import os

def login_user(username, password):
    """VULNERABLE: SQL Injection"""
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    # BAD: This allows SQL injection
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    print(f"\n🔍 Executing query: {query}")
    
    cursor.execute(query)
    result = cursor.fetchone()
    conn.close()
    return result

def ping_host(hostname):
    """VULNERABLE: Command Injection"""
    # BAD: Directly using user input in system command
    command = f"ping -c 1 {hostname}"
    print(f"\n💻 Executing: {command}")
    os.system(command)

def main():
    print("\n" + "="*50)
    print("VULNERABLE APPLICATION - DEMO")
    print("="*50)
    print("\n⚠️  This application contains security vulnerabilities")
    
    # Create database
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)")
    cursor.execute("INSERT OR IGNORE INTO users (id, username, password) VALUES (1, 'admin', 'admin123')")
    cursor.execute("INSERT OR IGNORE INTO users (id, username, password) VALUES (2, 'user', 'password')")
    conn.commit()
    conn.close()
print("\n" + "="*50)
    print("TEST 1: SQL INJECTION DEMO")
    print("="*50)
    print("💡 Try entering: admin' OR '1'='1")
    print("💡 Or try: admin' --")
    
    username = input("\nEnter username: ")
    password = input("Enter password: ")
    
    result = login_user(username, password)
    if result:
        print(f"\n✅ LOGIN SUCCESSFUL! User found: {result}")
        print("⚠️  VULNERABILITY: SQL Injection successful!")
    else:
        print("\n❌ Login failed")
    
    print("\n" + "="*50)
    print("TEST 2: COMMAND INJECTION DEMO")
    print("="*50)
    print("💡 Try entering: 8.8.8.8; whoami")
    print("💡 Or try: 8.8.8.8; ls -la")
    
    host = input("\nEnter hostname to ping: ")
    ping_host(host)

if __name__ == "__main__":
    main()


