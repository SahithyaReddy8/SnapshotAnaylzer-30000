from setuptools import setup

setup(
    name= "SnanpshotAnaylzer-30000",
    version='0.1',
    author="Sahithya Reddy",
    author_email="sahithyaveeramreddy@gmail.com",
    description="SnapshotAnaylzer-30000 is a tool to manage AWS EC2 Snapshots",
    lincense="GPLv3+",
    packages=['shotty'],
    url="https://github.com/SahithyaReddy8/SnapshotAnaylzer-30000",
    install_requires=[
           'click',
           'boto3'
    ],
    entry_points='''
      [console_scripts]
      shotty=shotty.shotty:cli
    ''',
)