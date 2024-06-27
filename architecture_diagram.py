from diagrams import Diagram, Cluster
from diagrams.aws.compute import EC2, ElasticBeanstalk
from diagrams.aws.database import RDS
from diagrams.aws.storage import S3
from diagrams.aws.security import SecretsManager

# Create a diagram
with Diagram("Cross Region Architecture", show=False):
    # Create clusters for regions
    with Cluster("Region 1"):
        s3_bucket1 = S3("S3 Bucket")
        rds = RDS("RDS")
        ec2 = EC2("EC2 Instance")
        elastic_beanstalk = ElasticBeanstalk("Elastic Beanstalk")
        secret_manager = SecretsManager("Secrets Manager")

    with Cluster("Region 2"):
        s3_bucket2 = S3("Replicated S3 Bucket")

    # Define the architecture
    s3_bucket1 >> s3_bucket2  # S3 bucket replication
    ec2 >> rds  # EC2 connects to RDS
    elastic_beanstalk >> ec2  # Elastic Beanstalk manages EC2
    ec2 >> secret_manager  # EC2 accesses Secrets Manager
    rds >> secret_manager  # RDS accesses Secrets Manager
