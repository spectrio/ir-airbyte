#docker login
#docker logout

#image: airbyte/destination-clickhouse-s3-sqs:dev

###############################################################################################################
#
# Dockerhub
#
###############################################################################################################
#docker tag airbyte/destination-clickhouse-s3-sqs:dev irllc/destination-clickhouse-s3-sqs:dev

#docker push irllc/destination-clickhouse-s3-sqs:dev

###############################################################################################################
#
# AWS ECR
#
###############################################################################################################
VERSION=7


docker tag airbyte/destination-clickhouse-s3-sqs:dev 781895395657.dkr.ecr.us-west-2.amazonaws.com/destination-clickhouse-s3-sqs:dev.${VERSION}


docker push 781895395657.dkr.ecr.us-west-2.amazonaws.com/destination-clickhouse-s3-sqs:dev.${VERSION}
