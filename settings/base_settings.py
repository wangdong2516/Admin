"""
Django settings for Admin project.

Generated by 'django-admin startproject' using Django 3.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
from datetime import timedelta
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
from celery.schedules import crontab

BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '@7i!i1rxvwlko%_h098$ew!_^6vn6p4(_fhe5(7=33hxcw9#wi'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # app
    'user.apps.UserConfig',
    'rest_framework',
    # command,添加自定义命令之前需要先执行迁移
    'utils',
    'task.apps.TaskConfig',
    'django_mysql',
    'django_filters',
    'django_celery_beat',
    # 'haystack',
    'channels',
    'bots',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.cache.UpdateCacheMiddleware',  # 对Django项目使用整站缓存
    'django.middleware.common.CommonMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',  # 对Django项目使用整站缓存
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 自定义的中间件
    'utils.middleware.ConvertGetMiddleware',
    'utils.middleware.ValidationErrorMiddleware',
    'utils.middleware.PVMiddleware',
]

ROOT_URLCONF = 'Admin.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [str(BASE_DIR / 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'Admin.wsgi.application'
ASGI_APPLICATION = "Admin.asgi.application"

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

# 日志配置
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    # 格式化
    'formatters': {
            'standard': {
                'format': '%(levelname)s %(asctime)s %(pathname)s %(funcName)s %(lineno)d: %(message)s'
            },
        },
    'handlers': {
        'django_request': {
            'class': 'logging.FileHandler',
            'formatter': 'standard',
            'filename': str(BASE_DIR / 'logs/request.log'),
            'level': 'DEBUG'
        },
        'signal_log': {
            'class': 'logging.FileHandler',
            'formatter': 'standard',
            'filename': str(BASE_DIR / 'logs/signal.log'),
            'level': 'INFO'
        }
    },
    'loggers': {
        # 默认django.request不会记录请求成功的日志，只会记录400和500的报错
        'django.request': {
            'handlers': ['django_request'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'signal': {
            'handlers': ['signal_log'],
            'level': 'INFO',
            'propagate': False
        }
    },
}


# --------Celery配置------
CELERY_TIMEZONE = "Asia/Shanghai"
# Broker配置，使用Redis作为消息中间件
CELERY_BROKER_URL = 'redis://127.0.0.1:6379/0'
# BACKEND配置，这里使用redis
CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/0'
# 结果序列化方案
CELERY_RESULT_SERIALIZER = 'json'

# CELERYBEAT_SCHEDULER = 'celery.schedulers.DatabaseScheduler'  # 使用了django-celery默认的数据库调度模型,任务执行周期都被存在你指定的orm数据库中

CELERY_TASK_RESULT_EXPIRES = 1200  # celery任务执行结果的超时时间，我的任务都不需要返回结果,只需要正确执行就行

CELERYD_CONCURRENCY = 10  # celery worker的并发数 也是命令行-c指定的数目,事实上实践发现并不是worker也多越好,保证任务不堆积,加上一定新增任务的预留就可以

CELERYD_PREFETCH_MULTIPLIER = 4  # celery worker 每次去rabbitmq取任务的数量，我这里预取了4个慢慢执行,因为任务有长有短没有预取太多

CELERYD_MAX_TASKS_PER_CHILD = 200  # 每个worker执行了多少任务就会死掉

CELERY_DEFAULT_QUEUE = "default_wj"  # 默认的队列，如果一个消息不符合其他的队列就会放在默认队列里面

CELERY_ACCEPT_CONTENT = ['application/json']

CELERY_TASK_SERIALIZER = 'json'

# 定时任务调度
CELERY_BEAT_SCHEDULE = {
    'to_database': {
        "task": "utils.celery_tasks.to_database",
        "schedule": timedelta(days=1)
    }
}

# celery队列
CELERY_QUEUES = {
    "default": {
        "exchange": "default",
        "exchange_type": "direct",
        "routing_key": "default"  # 路由key
    },
}

# -------RestFrameWork框架配置---------
# jwt-token签名的时候使用的密钥
JWT_TOKEN_SECRET_KEY = 'fequ_(pa*bj!!3y_n=*mo1to3sue)!yocd+^0jvslwmad9_74!'
REST_FRAMEWORK = {
    #  认证配置
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    #  限流配置，需要注意的是，限流和Django框架的缓存存在冲突，启用全栈缓存将会导致限流失效
    # https://q1mi.github.io/Django-REST-framework-documentation/api-guide/throttling_zh/
    'DEFAULT_THROTTLE_CLASSES': (
        # 'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle',
    ),
    'DEFAULT_THROTTLE_RATES': {
        'user': '5/min'
    },
    # 默认的过滤器后端
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
    )
}


# ------缓存配置(仅限本地，开发环境需要添加密码)--------------------
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/2",
        "TIMEOUT": 600,  # 缓存的默认超时时间，默认是300秒
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "MAX_ENTRIES": 300,  # 删除旧值之前默认缓存的最大条目，默认是300
            "CULL_FREQUENCY": 3,  # 当缓存的条目数达到MAX_ENTRIES指定的条目数之后，被淘汰数据占比
        },
        "KEY_PREFIX": 'Admin',  # 所有缓存键的前缀
        'VERSION': '1.00',  # 缓存的版本号
        'KEY_FUNCTION': None,   # 一个指定如何生成缓存key的函数路径
    }
}

# 每个页面缓存的时效,单位为秒
CACHE_MIDDLEWARE_SECONDS = 600

# -----------django haystack配置---------------
# 搜索引擎后端，注意这里haystack目前最高支持5.x版本的ES
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.elasticsearch5_backend.Elasticsearch5SearchEngine',
        'URL': 'http://127.0.0.1:9200/',
        'INDEX_NAME': 'haystack',
    },
}

# 在数据库发生更改的时候自动更新索引
HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'

# ----------------django-channels配置---------------
import environ

ROOT_DIR = environ.Path(__file__) - 2
env = environ.Env()
environ.Env.read_env(str(ROOT_DIR.path('.env')))

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [env.str('REDIS_URL', 'redis://127.0.0.1:6379/2')],
        },
    },
}
