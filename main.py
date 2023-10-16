import boto3
import schedule

ec2_client = boto3.client('ec2')

def volume_snapshots():
    volumes = ec2_client.describe_volumes()
    for volume in volumes['Volumes']:
        new_snapshot = ec2_client.create_snapshot(
            VolumeId=volume['VolumeId']
        )

schedule.every().day.do(volume_snapshots)

while True:
    schedule.run_pending()

