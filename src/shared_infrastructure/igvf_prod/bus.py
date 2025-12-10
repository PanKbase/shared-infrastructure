from constructs import Construct

from aws_cdk.aws_events import EventBus

from typing import Any


class Bus(Construct):

    def __init__(self, scope: Construct, construct_id: str, **kwargs: Any) -> None:
        super().__init__(scope, construct_id, **kwargs)
        self.default = EventBus.from_event_bus_arn(
            self,
            'DefaultBus',
            'arn:aws:events:us-west-2:654654139991:event-bus/default',
        )
