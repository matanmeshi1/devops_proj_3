import boto3


def get_instance_name(instance, key='Name'):
    try:
        tags = instance.tags
        for tag in tags:
            if tag['Key'] == key:
                return tag['Value']
        return ''
    except Exception as ex:
        print('error fetching instance name {} - returning empty string'.format(ex))
        return ''


if __name__ == '__main__':
    print('Instances cleanup - Start!')
    ec2 = boto3.resource('ec2', 'eu-west-1')
    instances = ec2.instances.filter(Filters=[{'Name': 'tag:k8s.io/role/master', 'Values': ['1']},
                                              {'Name': 'instance-state-code', 'Values': ['16']}])
    for instance in instances:
        print('Instance id: {}. Instance name: {}'.format(instance.id, get_instance_name(instance)))

    print('Instances cleanup - End!')
