#!/usr/bin/env python
"""
A simple script to test the PostgreSQL database connection.
Run this script after configuring PostgreSQL to verify that the connection works.
"""

import os
import sys
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'socialnetworkapi.settings')
django.setup()

# Import Django models
from django.db import connections
from django.db.utils import OperationalError

def test_connection():
    """Test the database connection and print the result."""
    try:
        # Try to get a cursor from the default database connection
        db_conn = connections['default']
        db_conn.cursor()
        
        # Get database info
        db_name = db_conn.settings_dict['NAME']
        db_engine = db_conn.settings_dict['ENGINE'].split('.')[-1]
        
        print(f"✅ Successfully connected to {db_engine} database: {db_name}")
        print("Database connection is working correctly!")
        return True
    except OperationalError as e:
        print(f"❌ Failed to connect to the database: {e}")
        print("\nPossible issues:")
        print("1. PostgreSQL service is not running")
        print("2. Database credentials in settings.py are incorrect")
        print("3. Database 'socialnetworkapi' does not exist")
        print("4. PostgreSQL is not installed or not in PATH")
        return False

if __name__ == "__main__":
    print("Testing database connection...")
    success = test_connection()
    sys.exit(0 if success else 1)