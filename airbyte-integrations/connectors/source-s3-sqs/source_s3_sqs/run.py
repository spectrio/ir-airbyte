#
# Copyright (c) 2024 Airbyte, Inc., all rights reserved.
#


import sys

from airbyte_cdk.entrypoint import launch
from .source import SourceS3Sqs

def run():
    source = SourceS3Sqs()
    launch(source, sys.argv[1:])
