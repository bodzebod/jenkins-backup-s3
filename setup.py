from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='bodzebod/jenkins-backup-s3',
    version='0.1.9',
    description="Fork from Backup Jenkins to S3",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="http://github.com/bodzebod/jenkins-backup-s3",
    author='Stephane Baudet',
    author_email='',
    license='MIT',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'backup-jenkins=jenkins_backup_s3.backup:main'
        ]
    },
    install_requires=(
        'boto3~=1.9',
        'click~=7.0',
        'colorama~=0.3.9',
        'python-dateutil~=2.8',
        'termcolor~=1.1'
    )
)
