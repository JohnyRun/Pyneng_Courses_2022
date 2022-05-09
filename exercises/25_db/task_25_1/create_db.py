import os
import sqlite3

def create_database(db_name):
    db_exists = os.path.exists(db_name)
    if not db_exists:
        print('Creating database...')
        connection = sqlite3.connect(db_name)
        with open('dhcp_snooping_schema.sql', 'r') as f:
            schema = f.read()
        connection.executescript(schema)
        return connection
    else:
        print('Database exists, assume dhcp table does, too.')

if __name__ == '__main__':
    create_database('dhcp_snooping.db')
