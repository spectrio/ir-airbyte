jq -c . sample_files/records.json | poetry run destination-clickhouse-s3-sqs write --config secrets/config.json --catalog sample_files/configured_catalog.json