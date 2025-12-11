from constructs import Construct

from typing import Any


class CodeStarConnection(Construct):

    def __init__(self, scope: Construct, construct_id: str, **kwargs: Any) -> None:
        super().__init__(scope, construct_id, **kwargs)
        self.arn = (
            'arn:aws:codeconnections:'
            'us-west-2:654654139991:'
            'connection/44fed36e-6dc9-480e-a575-5a9b29a2cc20'
        )
