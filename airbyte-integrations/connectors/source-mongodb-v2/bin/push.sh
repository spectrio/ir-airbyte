VERSION=1


docker tag airbyte/source-mongodb-v2:dev 781895395657.dkr.ecr.us-west-2.amazonaws.com/source-mongodb-v2-ext:dev.${VERSION}


docker push 781895395657.dkr.ecr.us-west-2.amazonaws.com/source-mongodb-v2-ext:dev.${VERSION}
