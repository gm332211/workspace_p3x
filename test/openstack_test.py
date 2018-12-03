from openstack import connection
conn = connection.Connection(
    # region_name='xiandian',
    auth=dict(
        auth_url='http://172.16.30.50:35357',
        username='admin',
        password='5BaCZHVLAFfYPEAm3mGw',
        project_name='admin',
        user_domain_name='domain',
        project_domain_name='domain',
    ),
    compute_api_version='2',
    identity_interface='admin')
print(conn.auth_token)
projects = conn.identity.projects()
for project in projects:
    print(project.name)
