from json_ql import JSONQLDict, JSONQL
from datetime import datetime

data = {
    'Reservations': [
        {
            'Groups': [
                {
                    'GroupName': 'string',
                    'GroupId': 'string'
                },
            ],
            'Instances': [
                {
                    'AmiLaunchIndex': 123,
                    'ImageId': 'string',
                    'InstanceId': '1',
                    'InstanceType': 'a1.medium',
                    'KernelId': 'string',
                    'KeyName': 'string',
                    'LaunchTime': datetime(2015, 1, 1),
                    'Monitoring': {
                        'State': 'disabled'
                    },
                    'Placement': {
                        'AvailabilityZone': 'string',
                        'Affinity': 'string',
                        'GroupName': 'string',
                        'PartitionNumber': 123,
                        'HostId': 'string',
                        'Tenancy': 'default',
                        'SpreadDomain': 'string',
                        'HostResourceGroupArn': 'string'
                    },
                    'Platform': 'Windows',
                    'PrivateDnsName': 'string',
                    'PrivateIpAddress': 'string',
                    'ProductCodes': [
                        {
                            'ProductCodeId': 'string',
                            'ProductCodeType': 'devpay'
                        },
                    ],
                    'PublicDnsName': 'string',
                    'PublicIpAddress': 'string',
                    'RamdiskId': 'string',
                    'State': {
                        'Code': 123,
                        'Name': 'pending'
                    },
                    'StateTransitionReason': 'string',
                    'SubnetId': 'string',
                    'VpcId': 'string',
                    'Architecture': 'arm64',
                    'BlockDeviceMappings': [
                        {
                            'DeviceName': 'string',
                            'Ebs': {
                                'AttachTime': datetime(2015, 1, 1),
                                'DeleteOnTermination': True|False,
                                'Status': 'attaching',
                                'VolumeId': 'string'
                            }
                        },
                    ],
                    'ClientToken': 'string',
                    'EbsOptimized': True|False,
                    'EnaSupport': True|False,
                    'Hypervisor': 'ovm',
                    'IamInstanceProfile': {
                        'Arn': 'string',
                        'Id': 'string'
                    },
                    'InstanceLifecycle': 'spot',
                    'ElasticGpuAssociations': [
                        {
                            'ElasticGpuId': 'string',
                            'ElasticGpuAssociationId': 'string',
                            'ElasticGpuAssociationState': 'string',
                            'ElasticGpuAssociationTime': 'string'
                        },
                    ],
                    'ElasticInferenceAcceleratorAssociations': [
                        {
                            'ElasticInferenceAcceleratorArn': 'string',
                            'ElasticInferenceAcceleratorAssociationId': 'string',
                            'ElasticInferenceAcceleratorAssociationState': 'string',
                            'ElasticInferenceAcceleratorAssociationTime': datetime(2015, 1, 1)
                        },
                    ],
                    'NetworkInterfaces': [
                        {
                            'Association': {
                                'CarrierIp': 'string',
                                'CustomerOwnedIp': 'string',
                                'IpOwnerId': 'string',
                                'PublicDnsName': 'string',
                                'PublicIp': 'string'
                            },
                            'Attachment': {
                                'AttachTime': datetime(2015, 1, 1),
                                'AttachmentId': 'string',
                                'DeleteOnTermination': True|False,
                                'DeviceIndex': 123,
                                'Status': 'attaching',
                                'NetworkCardIndex': 123
                            },
                            'Description': 'string',
                            'Groups': [
                                {
                                    'GroupName': 'string',
                                    'GroupId': 'string'
                                },
                            ],
                            'Ipv6Addresses': [
                                {
                                    'Ipv6Address': 'string'
                                },
                            ],
                            'MacAddress': 'string',
                            'NetworkInterfaceId': 'string',
                            'OwnerId': 'string',
                            'PrivateDnsName': 'string',
                            'PrivateIpAddress': 'string',
                            'PrivateIpAddresses': [
                                {
                                    'Association': {
                                        'CarrierIp': 'string',
                                        'CustomerOwnedIp': 'string',
                                        'IpOwnerId': 'string',
                                        'PublicDnsName': 'string',
                                        'PublicIp': 'string'
                                    },
                                    'Primary': True|False,
                                    'PrivateDnsName': 'string',
                                    'PrivateIpAddress': 'string'
                                },
                            ],
                            'SourceDestCheck': True|False,
                            'Status': 'available',
                            'SubnetId': 'string',
                            'VpcId': 'string',
                            'InterfaceType': 'string',
                            'Ipv4Prefixes': [
                                {
                                    'Ipv4Prefix': 'string'
                                },
                            ],
                            'Ipv6Prefixes': [
                                {
                                    'Ipv6Prefix': 'string'
                                },
                            ]
                        },
                    ],
                    'OutpostArn': 'string',
                    'RootDeviceName': 'string',
                    'RootDeviceType': 'ebs',
                    'SecurityGroups': [
                        {
                            'GroupName': 'string',
                            'GroupId': 'string'
                        },
                    ],
                    'SourceDestCheck': True|False,
                    'SpotInstanceRequestId': 'string',
                    'SriovNetSupport': 'string',
                    'StateReason': {
                        'Code': 'string',
                        'Message': 'string'
                    },
                    'Tags': [
                        {
                            'Key': 'string',
                            'Value': 'string'
                        },
                    ],
                    'VirtualizationType': 'hvm',
                    'CpuOptions': {
                        'CoreCount': 123,
                        'ThreadsPerCore': 123
                    },
                    'CapacityReservationId': 'string',
                    'CapacityReservationSpecification': {
                        'CapacityReservationPreference': 'open',
                        'CapacityReservationTarget': {
                            'CapacityReservationId': 'string',
                            'CapacityReservationResourceGroupArn': 'string'
                        }
                    },
                    'HibernationOptions': {
                        'Configured': True|False
                    },
                    'Licenses': [
                        {
                            'LicenseConfigurationArn': 'string'
                        },
                    ],
                    'MetadataOptions': {
                        'State': 'pending',
                        'HttpTokens': 'optional',
                        'HttpPutResponseHopLimit': 123,
                        'HttpEndpoint': 'disabled',
                        'HttpProtocolIpv6': 'disabled',
                        'InstanceMetadataTags': 'disabled'
                    },
                    'EnclaveOptions': {
                        'Enabled': True|False
                    },
                    'BootMode': 'legacy-bios',
                    'PlatformDetails': 'string',
                    'UsageOperation': 'string',
                    'UsageOperationUpdateTime': datetime(2015, 1, 1),
                    'PrivateDnsNameOptions': {
                        'HostnameType': 'ip-name',
                        'EnableResourceNameDnsARecord': True|False,
                        'EnableResourceNameDnsAAAARecord': True|False
                    },
                    'Ipv6Address': 'string',
                    'TpmSupport': 'string',
                    'MaintenanceOptions': {
                        'AutoRecovery': 'disabled'
                    }
                },
                {
                    'AmiLaunchIndex': 123,
                    'ImageId': 'string',
                    'InstanceId': '2',
                    'InstanceType': 'a1.medium',
                    'KernelId': 'string',
                    'KeyName': 'string',
                    'LaunchTime': datetime(2015, 1, 1),
                    'Monitoring': {
                        'State': 'disabled'
                    },
                    'Placement': {
                        'AvailabilityZone': 'string',
                        'Affinity': 'string',
                        'GroupName': 'string',
                        'PartitionNumber': 123,
                        'HostId': 'string',
                        'Tenancy': 'default',
                        'SpreadDomain': 'string',
                        'HostResourceGroupArn': 'string'
                    },
                    'Platform': 'Windows',
                    'PrivateDnsName': 'string',
                    'PrivateIpAddress': 'string',
                    'ProductCodes': [
                        {
                            'ProductCodeId': 'string',
                            'ProductCodeType': 'devpay'
                        },
                    ],
                    'PublicDnsName': 'string',
                    'PublicIpAddress': 'string',
                    'RamdiskId': 'string',
                    'State': {
                        'Code': 123,
                        'Name': 'pending'
                    },
                    'StateTransitionReason': 'string',
                    'SubnetId': 'string',
                    'VpcId': 'string',
                    'Architecture': 'arm64',
                    'BlockDeviceMappings': [
                        {
                            'DeviceName': 'string',
                            'Ebs': {
                                'AttachTime': datetime(2015, 1, 1),
                                'DeleteOnTermination': True|False,
                                'Status': 'attaching',
                                'VolumeId': 'string'
                            }
                        },
                    ],
                    'ClientToken': 'string',
                    'EbsOptimized': True|False,
                    'EnaSupport': True|False,
                    'Hypervisor': 'ovm',
                    'IamInstanceProfile': {
                        'Arn': 'string',
                        'Id': 'string'
                    },
                    'InstanceLifecycle': 'spot',
                    'ElasticGpuAssociations': [
                        {
                            'ElasticGpuId': 'string',
                            'ElasticGpuAssociationId': 'string',
                            'ElasticGpuAssociationState': 'string',
                            'ElasticGpuAssociationTime': 'string'
                        },
                    ],
                    'ElasticInferenceAcceleratorAssociations': [
                        {
                            'ElasticInferenceAcceleratorArn': 'string',
                            'ElasticInferenceAcceleratorAssociationId': 'string',
                            'ElasticInferenceAcceleratorAssociationState': 'string',
                            'ElasticInferenceAcceleratorAssociationTime': datetime(2015, 1, 1)
                        },
                    ],
                    'NetworkInterfaces': [
                        {
                            'Association': {
                                'CarrierIp': 'string',
                                'CustomerOwnedIp': 'string',
                                'IpOwnerId': 'string',
                                'PublicDnsName': 'string',
                                'PublicIp': 'string'
                            },
                            'Attachment': {
                                'AttachTime': datetime(2015, 1, 1),
                                'AttachmentId': 'string',
                                'DeleteOnTermination': True|False,
                                'DeviceIndex': 123,
                                'Status': 'attaching',
                                'NetworkCardIndex': 123
                            },
                            'Description': 'string',
                            'Groups': [
                                {
                                    'GroupName': 'string',
                                    'GroupId': 'string'
                                },
                            ],
                            'Ipv6Addresses': [
                                {
                                    'Ipv6Address': 'string'
                                },
                            ],
                            'MacAddress': 'string',
                            'NetworkInterfaceId': 'string',
                            'OwnerId': 'string',
                            'PrivateDnsName': 'string',
                            'PrivateIpAddress': 'string',
                            'PrivateIpAddresses': [
                                {
                                    'Association': {
                                        'CarrierIp': 'string',
                                        'CustomerOwnedIp': 'string',
                                        'IpOwnerId': 'string',
                                        'PublicDnsName': 'string',
                                        'PublicIp': 'string'
                                    },
                                    'Primary': True|False,
                                    'PrivateDnsName': 'string',
                                    'PrivateIpAddress': 'string'
                                },
                            ],
                            'SourceDestCheck': True|False,
                            'Status': 'available',
                            'SubnetId': 'string',
                            'VpcId': 'string',
                            'InterfaceType': 'string',
                            'Ipv4Prefixes': [
                                {
                                    'Ipv4Prefix': 'string'
                                },
                            ],
                            'Ipv6Prefixes': [
                                {
                                    'Ipv6Prefix': 'string'
                                },
                            ]
                        },
                    ],
                    'OutpostArn': 'string',
                    'RootDeviceName': 'string',
                    'RootDeviceType': 'ebs',
                    'SecurityGroups': [
                        {
                            'GroupName': 'string',
                            'GroupId': 'string'
                        },
                    ],
                    'SourceDestCheck': True|False,
                    'SpotInstanceRequestId': 'string',
                    'SriovNetSupport': 'string',
                    'StateReason': {
                        'Code': 'string',
                        'Message': 'string'
                    },
                    'Tags': [
                        {
                            'Key': 'string',
                            'Value': 'string'
                        },
                    ],
                    'VirtualizationType': 'hvm',
                    'CpuOptions': {
                        'CoreCount': 123,
                        'ThreadsPerCore': 123
                    },
                    'CapacityReservationId': 'string',
                    'CapacityReservationSpecification': {
                        'CapacityReservationPreference': 'open',
                        'CapacityReservationTarget': {
                            'CapacityReservationId': 'string',
                            'CapacityReservationResourceGroupArn': 'string'
                        }
                    },
                    'HibernationOptions': {
                        'Configured': True|False
                    },
                    'Licenses': [
                        {
                            'LicenseConfigurationArn': 'string'
                        },
                    ],
                    'MetadataOptions': {
                        'State': 'pending',
                        'HttpTokens': 'optional',
                        'HttpPutResponseHopLimit': 123,
                        'HttpEndpoint': 'disabled',
                        'HttpProtocolIpv6': 'disabled',
                        'InstanceMetadataTags': 'disabled'
                    },
                    'EnclaveOptions': {
                        'Enabled': True|False
                    },
                    'BootMode': 'legacy-bios',
                    'PlatformDetails': 'string',
                    'UsageOperation': 'string',
                    'UsageOperationUpdateTime': datetime(2015, 1, 1),
                    'PrivateDnsNameOptions': {
                        'HostnameType': 'ip-name',
                        'EnableResourceNameDnsARecord': True|False,
                        'EnableResourceNameDnsAAAARecord': True|False
                    },
                    'Ipv6Address': 'string',
                    'TpmSupport': 'string',
                    'MaintenanceOptions': {
                        'AutoRecovery': 'disabled'
                    }
                }
            ],
            'OwnerId': 'string',
            'RequesterId': 'string',
            'ReservationId': 'string'
        },
        {
            'Groups': [
                {
                    'GroupName': 'string',
                    'GroupId': 'string'
                },
            ],
            'Instances': [
                {
                    'AmiLaunchIndex': 123,
                    'ImageId': 'string',
                    'InstanceId': '3',
                    'InstanceType': 'a1.medium',
                    'KernelId': 'string',
                    'KeyName': 'string',
                    'LaunchTime': datetime(2015, 1, 1),
                    'Monitoring': {
                        'State': 'disabled'
                    },
                    'Placement': {
                        'AvailabilityZone': 'string',
                        'Affinity': 'string',
                        'GroupName': 'string',
                        'PartitionNumber': 123,
                        'HostId': 'string',
                        'Tenancy': 'default',
                        'SpreadDomain': 'string',
                        'HostResourceGroupArn': 'string'
                    },
                    'Platform': 'Windows',
                    'PrivateDnsName': 'string',
                    'PrivateIpAddress': 'string',
                    'ProductCodes': [
                        {
                            'ProductCodeId': 'string',
                            'ProductCodeType': 'devpay'
                        },
                    ],
                    'PublicDnsName': 'string',
                    'PublicIpAddress': 'string',
                    'RamdiskId': 'string',
                    'State': {
                        'Code': 123,
                        'Name': 'pending'
                    },
                    'StateTransitionReason': 'string',
                    'SubnetId': 'string',
                    'VpcId': 'string',
                    'Architecture': 'arm64',
                    'BlockDeviceMappings': [
                        {
                            'DeviceName': 'string',
                            'Ebs': {
                                'AttachTime': datetime(2015, 1, 1),
                                'DeleteOnTermination': True|False,
                                'Status': 'attaching',
                                'VolumeId': 'string'
                            }
                        },
                    ],
                    'ClientToken': 'string',
                    'EbsOptimized': True|False,
                    'EnaSupport': True|False,
                    'Hypervisor': 'ovm',
                    'IamInstanceProfile': {
                        'Arn': 'string',
                        'Id': 'string'
                    },
                    'InstanceLifecycle': 'spot',
                    'ElasticGpuAssociations': [
                        {
                            'ElasticGpuId': 'string',
                            'ElasticGpuAssociationId': 'string',
                            'ElasticGpuAssociationState': 'string',
                            'ElasticGpuAssociationTime': 'string'
                        },
                    ],
                    'ElasticInferenceAcceleratorAssociations': [
                        {
                            'ElasticInferenceAcceleratorArn': 'string',
                            'ElasticInferenceAcceleratorAssociationId': 'string',
                            'ElasticInferenceAcceleratorAssociationState': 'string',
                            'ElasticInferenceAcceleratorAssociationTime': datetime(2015, 1, 1)
                        },
                    ],
                    'NetworkInterfaces': [
                        {
                            'Association': {
                                'CarrierIp': 'string',
                                'CustomerOwnedIp': 'string',
                                'IpOwnerId': 'string',
                                'PublicDnsName': 'string',
                                'PublicIp': 'string'
                            },
                            'Attachment': {
                                'AttachTime': datetime(2015, 1, 1),
                                'AttachmentId': 'string',
                                'DeleteOnTermination': True|False,
                                'DeviceIndex': 123,
                                'Status': 'attaching',
                                'NetworkCardIndex': 123
                            },
                            'Description': 'string',
                            'Groups': [
                                {
                                    'GroupName': 'string',
                                    'GroupId': 'string'
                                },
                            ],
                            'Ipv6Addresses': [
                                {
                                    'Ipv6Address': 'string'
                                },
                            ],
                            'MacAddress': 'string',
                            'NetworkInterfaceId': 'string',
                            'OwnerId': 'string',
                            'PrivateDnsName': 'string',
                            'PrivateIpAddress': 'string',
                            'PrivateIpAddresses': [
                                {
                                    'Association': {
                                        'CarrierIp': 'string',
                                        'CustomerOwnedIp': 'string',
                                        'IpOwnerId': 'string',
                                        'PublicDnsName': 'string',
                                        'PublicIp': 'string'
                                    },
                                    'Primary': True|False,
                                    'PrivateDnsName': 'string',
                                    'PrivateIpAddress': 'string'
                                },
                            ],
                            'SourceDestCheck': True|False,
                            'Status': 'available',
                            'SubnetId': 'string',
                            'VpcId': 'string',
                            'InterfaceType': 'string',
                            'Ipv4Prefixes': [
                                {
                                    'Ipv4Prefix': 'string'
                                },
                            ],
                            'Ipv6Prefixes': [
                                {
                                    'Ipv6Prefix': 'string'
                                },
                            ]
                        },
                    ],
                    'OutpostArn': 'string',
                    'RootDeviceName': 'string',
                    'RootDeviceType': 'ebs',
                    'SecurityGroups': [
                        {
                            'GroupName': 'string',
                            'GroupId': 'string'
                        },
                    ],
                    'SourceDestCheck': True|False,
                    'SpotInstanceRequestId': 'string',
                    'SriovNetSupport': 'string',
                    'StateReason': {
                        'Code': 'string',
                        'Message': 'string'
                    },
                    'Tags': [
                        {
                            'Key': 'string',
                            'Value': 'string'
                        },
                    ],
                    'VirtualizationType': 'hvm',
                    'CpuOptions': {
                        'CoreCount': 123,
                        'ThreadsPerCore': 123
                    },
                    'CapacityReservationId': 'string',
                    'CapacityReservationSpecification': {
                        'CapacityReservationPreference': 'open',
                        'CapacityReservationTarget': {
                            'CapacityReservationId': 'string',
                            'CapacityReservationResourceGroupArn': 'string'
                        }
                    },
                    'HibernationOptions': {
                        'Configured': True|False
                    },
                    'Licenses': [
                        {
                            'LicenseConfigurationArn': 'string'
                        },
                    ],
                    'MetadataOptions': {
                        'State': 'pending',
                        'HttpTokens': 'optional',
                        'HttpPutResponseHopLimit': 123,
                        'HttpEndpoint': 'disabled',
                        'HttpProtocolIpv6': 'disabled',
                        'InstanceMetadataTags': 'disabled'
                    },
                    'EnclaveOptions': {
                        'Enabled': True|False
                    },
                    'BootMode': 'legacy-bios',
                    'PlatformDetails': 'string',
                    'UsageOperation': 'string',
                    'UsageOperationUpdateTime': datetime(2015, 1, 1),
                    'PrivateDnsNameOptions': {
                        'HostnameType': 'ip-name',
                        'EnableResourceNameDnsARecord': True|False,
                        'EnableResourceNameDnsAAAARecord': True|False
                    },
                    'Ipv6Address': 'string',
                    'TpmSupport': 'string',
                    'MaintenanceOptions': {
                        'AutoRecovery': 'disabled'
                    }
                },
                {
                    'AmiLaunchIndex': 123,
                    'ImageId': 'string',
                    'InstanceId': '4',
                    'InstanceType': 'a1.medium',
                    'KernelId': 'string',
                    'KeyName': 'string',
                    'LaunchTime': datetime(2015, 1, 1),
                    'Monitoring': {
                        'State': 'disabled'
                    },
                    'Placement': {
                        'AvailabilityZone': 'string',
                        'Affinity': 'string',
                        'GroupName': 'string',
                        'PartitionNumber': 123,
                        'HostId': 'string',
                        'Tenancy': 'default',
                        'SpreadDomain': 'string',
                        'HostResourceGroupArn': 'string'
                    },
                    'Platform': 'Windows',
                    'PrivateDnsName': 'string',
                    'PrivateIpAddress': 'string',
                    'ProductCodes': [
                        {
                            'ProductCodeId': 'string',
                            'ProductCodeType': 'devpay'
                        },
                    ],
                    'PublicDnsName': 'string',
                    'PublicIpAddress': 'string',
                    'RamdiskId': 'string',
                    'State': {
                        'Code': 123,
                        'Name': 'pending'
                    },
                    'StateTransitionReason': 'string',
                    'SubnetId': 'string',
                    'VpcId': 'string',
                    'Architecture': 'arm64',
                    'BlockDeviceMappings': [
                        {
                            'DeviceName': 'string',
                            'Ebs': {
                                'AttachTime': datetime(2015, 1, 1),
                                'DeleteOnTermination': True|False,
                                'Status': 'attaching',
                                'VolumeId': 'string'
                            }
                        },
                    ],
                    'ClientToken': 'string',
                    'EbsOptimized': True|False,
                    'EnaSupport': True|False,
                    'Hypervisor': 'ovm',
                    'IamInstanceProfile': {
                        'Arn': 'string',
                        'Id': 'string'
                    },
                    'InstanceLifecycle': 'spot',
                    'ElasticGpuAssociations': [
                        {
                            'ElasticGpuId': 'string',
                            'ElasticGpuAssociationId': 'string',
                            'ElasticGpuAssociationState': 'string',
                            'ElasticGpuAssociationTime': 'string'
                        },
                    ],
                    'ElasticInferenceAcceleratorAssociations': [
                        {
                            'ElasticInferenceAcceleratorArn': 'string',
                            'ElasticInferenceAcceleratorAssociationId': 'string',
                            'ElasticInferenceAcceleratorAssociationState': 'string',
                            'ElasticInferenceAcceleratorAssociationTime': datetime(2015, 1, 1)
                        },
                    ],
                    'NetworkInterfaces': [
                        {
                            'Association': {
                                'CarrierIp': 'string',
                                'CustomerOwnedIp': 'string',
                                'IpOwnerId': 'string',
                                'PublicDnsName': 'string',
                                'PublicIp': 'string'
                            },
                            'Attachment': {
                                'AttachTime': datetime(2015, 1, 1),
                                'AttachmentId': 'string',
                                'DeleteOnTermination': True|False,
                                'DeviceIndex': 123,
                                'Status': 'attaching',
                                'NetworkCardIndex': 123
                            },
                            'Description': 'string',
                            'Groups': [
                                {
                                    'GroupName': 'string',
                                    'GroupId': 'string'
                                },
                            ],
                            'Ipv6Addresses': [
                                {
                                    'Ipv6Address': 'string'
                                },
                            ],
                            'MacAddress': 'string',
                            'NetworkInterfaceId': 'string',
                            'OwnerId': 'string',
                            'PrivateDnsName': 'string',
                            'PrivateIpAddress': 'string',
                            'PrivateIpAddresses': [
                                {
                                    'Association': {
                                        'CarrierIp': 'string',
                                        'CustomerOwnedIp': 'string',
                                        'IpOwnerId': 'string',
                                        'PublicDnsName': 'string',
                                        'PublicIp': 'string'
                                    },
                                    'Primary': True|False,
                                    'PrivateDnsName': 'string',
                                    'PrivateIpAddress': 'string'
                                },
                            ],
                            'SourceDestCheck': True|False,
                            'Status': 'available',
                            'SubnetId': 'string',
                            'VpcId': 'string',
                            'InterfaceType': 'string',
                            'Ipv4Prefixes': [
                                {
                                    'Ipv4Prefix': 'string'
                                },
                            ],
                            'Ipv6Prefixes': [
                                {
                                    'Ipv6Prefix': 'string'
                                },
                            ]
                        },
                    ],
                    'OutpostArn': 'string',
                    'RootDeviceName': 'string',
                    'RootDeviceType': 'ebs',
                    'SecurityGroups': [
                        {
                            'GroupName': 'string',
                            'GroupId': 'string'
                        },
                    ],
                    'SourceDestCheck': True|False,
                    'SpotInstanceRequestId': 'string',
                    'SriovNetSupport': 'string',
                    'StateReason': {
                        'Code': 'string',
                        'Message': 'string'
                    },
                    'Tags': [
                        {
                            'Key': 'string',
                            'Value': 'string'
                        },
                    ],
                    'VirtualizationType': 'hvm',
                    'CpuOptions': {
                        'CoreCount': 123,
                        'ThreadsPerCore': 123
                    },
                    'CapacityReservationId': 'string',
                    'CapacityReservationSpecification': {
                        'CapacityReservationPreference': 'open',
                        'CapacityReservationTarget': {
                            'CapacityReservationId': 'string',
                            'CapacityReservationResourceGroupArn': 'string'
                        }
                    },
                    'HibernationOptions': {
                        'Configured': True|False
                    },
                    'Licenses': [
                        {
                            'LicenseConfigurationArn': 'string'
                        },
                    ],
                    'MetadataOptions': {
                        'State': 'pending',
                        'HttpTokens': 'optional',
                        'HttpPutResponseHopLimit': 123,
                        'HttpEndpoint': 'disabled',
                        'HttpProtocolIpv6': 'disabled',
                        'InstanceMetadataTags': 'disabled'
                    },
                    'EnclaveOptions': {
                        'Enabled': True|False
                    },
                    'BootMode': 'legacy-bios',
                    'PlatformDetails': 'string',
                    'UsageOperation': 'string',
                    'UsageOperationUpdateTime': datetime(2015, 1, 1),
                    'PrivateDnsNameOptions': {
                        'HostnameType': 'ip-name',
                        'EnableResourceNameDnsARecord': True|False,
                        'EnableResourceNameDnsAAAARecord': True|False
                    },
                    'Ipv6Address': 'string',
                    'TpmSupport': 'string',
                    'MaintenanceOptions': {
                        'AutoRecovery': 'disabled'
                    }
                }
            ],
            'OwnerId': 'string',
            'RequesterId': 'string',
            'ReservationId': 'string'
        }
    ],
    'NextToken': 'string'
}

if __name__ == "__main__":
    # a = JSONQLDict({"name": "bharat sinha", "details": {"age": 23}}, key_delimiter="/")
    # a = JSONQLDict(data, key_delimiter="/")
    a = JSONQLDict({"data": [[[{"a":"1"}],[{"b": "2"}]]]}, key_delimiter="/")
    d = 1
    # print("answer", a[f'Reservations/Instances/[[{{InstanceId={d}}}]]/Tags/[{{Key=string}}]/Value'])
    print("answer", a[f'data/[[[{{b=2}}]]]'])
    # a["new"] = 2
    # print(len(a))
    # printa["age"] = 23
    # for i in a:
    #     print(i)

    # print(a)