# jenkins-backup-s3

This is a fork from https://github.com/artsy/jenkins-backup-s3 (v0.1.9).

A collection of scripts to backup Jenkins configuration to S3, as well as manage and restore those backups. By default
runs silently (no output) with proper exit codes. Log Level option enables output.

I needed to specify the AWS CLI argument "-sse" when uploading a backup to an encrypted bucket. So, this fork adds an argument "--sse" with a default value "aws:kms".

## Setup

`sudo pip install git+https://github.com/bodzebod/jenkins-backup-s3`

### Configure S3 and IAM

- Create an S3 bucket to store backups.

- Create an IAM role with STS:AssumeRole and a trust Service ec2.amazonaws.com.  The IAM role must have the `GetObject`, `DeleteObject`, `PutObject` and `ListBucket` S3 permissions for that bucket.

## Usage

Setup with cron for ideal usage.

`backup-jenkins {OPTIONS} {COMMAND} {COMMAND_OPTIONS}`

Options can be set directly or via and environment variable.

The only required option is your S3 bucket:
  - `backup-jenkins --bucket={BUCKET_NAME}`

Other available options are:

Bucket prefix (defaults to "jenkins-backups"):
  - `backup-jenkins --bucket-prefix={BUCKET_PREFIX}`

Bucket region (defaults to "us-east-1"):
  - `backup-jenkins --bucket-region={BUCKET_REGION}`

Available commands:
  - `create`
  - `restore`
  - `list`
  - `delete`
  - `prune`

Run `backup-jenkins {COMMAND} --help` for command-specific options.

## Running a daily backup on Jenkins

Create a new item in Jenkins and configure a build of this repository.

Set the shell / virtualenv builder (if you have it installed) to run `backup-jenkins create`.

Set the build on a daily CRON schedule.
