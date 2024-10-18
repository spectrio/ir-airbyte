#
# Copyright (c) 2024 Airbyte, Inc., all rights reserved.
#

import logging
from typing import Any, Iterable, Mapping
import json
import boto3

from airbyte_cdk.destinations import Destination
from airbyte_cdk.models import AirbyteConnectionStatus, AirbyteMessage, ConfiguredAirbyteCatalog, Status, Type

logger = logging.getLogger("airbyte")

class DestinationClickhouseS3Sqs(Destination):

    def write(self, config: Mapping[str, Any], configured_catalog: ConfiguredAirbyteCatalog, input_messages: Iterable[AirbyteMessage]) -> Iterable[AirbyteMessage]:
        logger.info("Begin writing to the destination...")
        # logger.info("Config contents:")
        # logger.info(json.dumps(config, indent=2))

        for message in input_messages:
            logger.info(f"Message Type: {message.type}")

            if message.type == Type.RECORD:
                record = message.record.data  
                # logger.info(f"Writing record: {record['_airbyte_data']}")
                logger.info(json.dumps(message.record.data, indent=2))

            if message.type == Type.STATE:
                yield message

        
        logger.info("Finished writing all records.")
        final_state = {"status": "completed", "recordsSynced": 1000}
        yield AirbyteMessage(type="STATE", state=final_state)

       


    def check(self, logger: logging.Logger, config: Mapping[str, Any]) -> AirbyteConnectionStatus:
        """
        Tests if the input configuration can be used to successfully connect to the destination with the needed permissions
            e.g: if a provided API token or password can be used to connect and write to the destination.

        :param logger: Logging object to display debug/info/error to the logs
            (logs will not be accessible via airbyte UI if they are not passed to this logger)
        :param config: Json object containing the configuration of this destination, content of this json is as specified in
        the properties of the spec.json file

        :return: AirbyteConnectionStatus indicating a Success or Failure
        """
        try:
            # TODO

            return AirbyteConnectionStatus(status=Status.SUCCEEDED)
        except Exception as e:
            return AirbyteConnectionStatus(status=Status.FAILED, message=f"An exception occurred: {repr(e)}")
