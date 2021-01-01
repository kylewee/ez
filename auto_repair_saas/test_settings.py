from .settings import *

DEBUG = True
INSTALLED_APPS.remove('django_tenants')
INSTALLED_APPS.remove('auto_repair_saas.apps.tenants')
MIDDLEWARE.remove('auto_repair_saas.apps.tenants.middleware.TenantMiddleware')
DATABASE_ROUTERS = ()
SENDGRID_SANDBOX_MODE_IN_DEBUG = True

if os.environ.get('GITHUB_WORKFLOW'):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'github_actions',
            'USER': 'postgres',
            'PASSWORD': 'postgres',
            'HOST': '127.0.0.1',
            'PORT': '5432',
        }
    }
