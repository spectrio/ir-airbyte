#
# Copyright (c) 2024 Airbyte, Inc., all rights reserved.
#


import sys

from destination_clickhouse_s3_sqs import DestinationClickhouseS3Sqs

if __name__ == "__main__":
    DestinationClickhouseS3Sqs().run(sys.argv[1:])
