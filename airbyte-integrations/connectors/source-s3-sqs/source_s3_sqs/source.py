# Copyright (c) 2024 Airbyte, Inc., all rights reserved.

from abc import ABC
from typing import Any, Iterable, List, Mapping, MutableMapping, Optional, Tuple
import requests
from airbyte_cdk.sources import AbstractSource
from airbyte_cdk.sources.streams import Stream
from airbyte_cdk.sources.streams.http import HttpStream
from airbyte_cdk.sources.streams.http.requests_native_auth import TokenAuthenticator
from airbyte_cdk.models import AirbyteMessage, AirbyteRecordMessage, Type

import logging

logger = logging.getLogger("airbyte")

# Basic full refresh stream
class S3SqsStream(Stream):
    primary_key = "s3_object_key"
    
    def __init__(self, config: Mapping[str, Any]):
        self.config = config

    @property
    def name(self) -> str:
        """Returns the name of the stream, which should match the catalog."""
        logger.info("Getting name")
        return "S3SqsStream"  # Ensure this matches the stream name in the configured catalog.

    def process_message(self, message: Any) -> Iterable[AirbyteRecordMessage]:
        logger.info("Entry to Process Message")
        return []

    def read_records(self, stream_slice: Optional[Mapping[str, Any]] = None, **kwargs) -> Iterable[AirbyteRecordMessage]:
        logger.info("Entry to Read Records")
        yield from []

    def get_updated_state(self, current_stream_state: MutableMapping[str, Any], latest_record: Mapping[str, Any]) -> Mapping[str, Any]:
        return {}
    

# Source
class SourceS3Sqs(AbstractSource):
    """
    /***
     * The main source class for the connector. This class is responsible for 
     * handling the source setup, including checking connection status and defining available streams.
    ***/
    """

    def check_connection(self, logger, config) -> Tuple[bool, any]:
        """
        /***
         * Checks the connection to the API using the provided configuration.
         * This method should attempt a simple API request to validate the connection (e.g., a ping or a request to a lightweight endpoint).
         * @param config: The configuration for the connector (e.g., API keys, URLs).
         * @param logger: The logger object to log connection check messages.
         * @return: A tuple indicating the success of the connection check (True/False) and an error message if failed.
        ***/
        """
        logger.info("testing")
        return True, None

    def streams(self, config: Mapping[str, Any]) -> List[Stream]:
        """
        /***
         * Defines the available streams in the connector (e.g., Customers, Employees).
         * Each stream corresponds to a specific API endpoint from which data will be fetched.
         * @param config: The configuration for the connector.
         * @return: A list of stream instances for the connector.
        ***/
        """
        return [S3SqsStream(config=config)] 
