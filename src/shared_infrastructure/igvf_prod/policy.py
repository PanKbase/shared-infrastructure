from constructs import Construct

from aws_cdk.aws_iam import ManagedPolicy

from typing import Any


class BucketAccessPolicies(Construct):

    def __init__(self, scope: Construct, construct_id: str, **kwargs: Any) -> None:
        super().__init__(scope, construct_id, **kwargs)
        self.download_igvf_files_policy = ManagedPolicy.from_managed_policy_arn(
            self,
            'DownloadIgvfFilesPolicy',
            'arn:aws:iam::654654139991:policy/download-pankbase-files',
        )
        self.upload_igvf_files_policy = ManagedPolicy.from_managed_policy_arn(
            self,
            'UploadIgvfFilesPolicy',
            'arn:aws:iam::654654139991:policy/upload-pankbase-files'
        )
        self.download_igvf_restricted_files_policy = ManagedPolicy.from_managed_policy_arn(
            self,
            'DownloadIgvfRestrictedFilesPolicy',
            'arn:aws:iam::654654139991:policy/download-pankbase-restricted-files',
        )
        self.upload_igvf_restricted_files_policy = ManagedPolicy.from_managed_policy_arn(
            self,
            'UploadIgvfRestrictedFilesPolicy',
            'arn:aws:iam::654654139991:policy/upload-pankbase-restricted-files',
        )
