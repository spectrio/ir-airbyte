#
# Copyright (c) 2024 Airbyte, Inc., all rights reserved.
#


import sys

from airbyte_cdk.entrypoint import launch
from .destination import DestinationClickhouseS3Sqs

def run():
    destination = DestinationClickhouseS3Sqs()
    destination.run(sys.argv[1:])
