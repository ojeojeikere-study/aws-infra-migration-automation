"""
Author: Oje Ojeikere
Description:
Automates RDS PostgreSQL snapshot creation using boto3.
This script is safe for public upload (no credentials included).
"""

import boto3
import datetime

# Initialize RDS client (credentials pulled from AWS CLI config)
rds = boto3.client('rds', region_name='us-east-1')

def create_snapshot(db_instance_id):
    timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    snapshot_id = f"{db_instance_id}-snapshot-{timestamp}"

    print(f"Creating snapshot: {snapshot_id}")
    try:
        rds.create_db_snapshot(
            DBSnapshotIdentifier=snapshot_id,
            DBInstanceIdentifier=db_instance_id
        )
        print("✅ Snapshot creation initiated successfully.")
    except Exception as e:
        print(f"❌ Error creating snapshot: {e}")

if __name__ == "__main__":
    create_snapshot("legacydb")
