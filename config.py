import os
import json

# mirrors listed here
MIRRORS = [
    ('http', 'mirrors.163.com/pypi'),
    ('https', 'mirror-ord.pypi.io'),
    ('https', 'pypi.doubanio.com'),
    ('https', 'pypi.fcio.net'),
    ('https', 'pypi.tuna.tsinghua.edu.cn'),
    ('http', 'mirror.picosecond.org/pypi'),
    ('http', 'mirrors.aliyun.com/pypi'),
    ('http', 'pypi.pubyun.com'),
    ('http', 'mirrors-uk.go-parts.com/python'),
    ('http', 'mirrors-ru.go-parts.com/python'),
    ('http', 'mirrors-au.go-parts.com/python'),
    ('https', 'pypi.mirrors.ustc.edu.cn'),
]

EMAIL_OVERRIDE = None  # None or "blah@example.com"


def load_config():
    envvars = '/etc/pypi-mirrors-environment.json'
    if os.path.exists(envvars):
        env = json.load(open(envvars))
        env.update(os.environ)
    else:
        env = os.environ
    return {
        'host': env.get('CACHE_REDIS_HOST', 'localhost'),
        'port': env.get('CACHE_REDIS_PORT', 6379),
        'password': env.get('CACHE_REDIS_PASSWORD'),
        'db': 1,
        'ip_api_key': env.get('IPLOC_API_KEY', None),
        'twitter_consumer_key': env.get('TWITTER_CONSUMER_KEY', None),
        'twitter_consumer_secret': env.get('TWITTER_CONSUMER_SECRET', None),
        'twitter_access_key': env.get('TWITTER_ACCESS_KEY', None),
        'twitter_access_secret': env.get('TWITTER_ACCESS_SECRET', None),
        'email_host': env.get('EMAIL_HOST', None),
        'email_port': env.get('EMAIL_PORT', None),
        'email_user': env.get('EMAIL_USER', None),
        'email_password': env.get('EMAIL_PASSWORD', None),
        'email_from': env.get('EMAIL_FROM', None),
        'email_to': env.get('EMAIL_TO', None),
        'email_bcc': env.get('EMAIL_BCC', None),
        'email_to_admin': env.get('EMAIL_TO_ADMIN', None),
        'sentry_dsn': env.get('SENTRY_DSN', None),
    }
