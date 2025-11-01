"""
migrate_data.py
Author: Oje Ojeikere
Description:
Simulates data migration from a legacy PostgreSQL database
to an AWS RDS PostgreSQL instance using psycopg2.
"""

import psycopg2

def migrate_data(source_config, target_config):
    try:
        src_conn = psycopg2.connect(**source_config)
        tgt_conn = psycopg2.connect(**target_config)
        src_cursor = src_conn.cursor()
        tgt_cursor = tgt_conn.cursor()

        src_cursor.execute("SELECT * FROM users;")
        rows = src_cursor.fetchall()
        for row in rows:
            tgt_cursor.execute(
                "INSERT INTO users (id, name, email) VALUES (%s, %s, %s)", row
            )

        tgt_conn.commit()
        print(f"✅ Migrated {len(rows)} records successfully.")

    except Exception as e:
        print(f"❌ Migration failed: {e}")
    finally:
        src_cursor.close()
        tgt_cursor.close()
        src_conn.close()
        tgt_conn.close()

if __name__ == "__main__":
    source_db = {
        "dbname": "legacydb",
        "user": "admin",
        "password": "admin1234",
        "host": "127.0.0.1",
        "port": "5432"
    }

    target_db = {
        "dbname": "awsdb",
        "user": "admin",
        "password": "admin1234",
        "host": "rds-instance.amazonaws.com",
        "port": "5432"
    }

    migrate_data(source_db, target_db)
