from constructs import Construct

from aws_cdk.aws_ec2 import Vpc

from typing import Any


class Network(Construct):

    def __init__(self, scope: Construct, construct_id: str, **kwargs: Any) -> None:
        super().__init__(scope, construct_id, **kwargs)
        self.vpc = Vpc.from_lookup(
            self,
            'Vpc',
            vpc_id='vpc-087ef239aefa4a4ad'
        )
