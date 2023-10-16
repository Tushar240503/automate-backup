import boto3
import schedule

ec2_client = boto3.client('ec2')

snapshots = ec2_client.describe_snapshots(OwnerIds=['self'])
sorted_by_date = sorted(snapshots['Snapshots'], key=lambda x: x['StartTime'], reverse=True)

for snap in sorted_by_date[2:]:
    response = ec2_client.delete_snapshot(
        SnapshotId=snap['SnapshotId']
    )
    print(response)
