from .common_settings import *

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {
        "require_debug_false": {
            "()": "django.utils.log.RequireDebugFalse",
        },
        "require_debug_true": {
            "()": "django.utils.log.RequireDebugTrue",
        },
    },
    "formatters": {
        "django.server": {
            "()": "django.utils.log.ServerFormatter",
            "format": "[%(server_time)s] %(message)s a",
        },
        "verbose": {
            "format": "[%(levelname)s] %(asctime)s %(module)s "
            "%(process)d %(thread)d %(message)s"
        },
        "simple": {
            "format": "%(asctime)s %(name)s:%(lineno)s %(funcName)s [%(levelname)s]: %(message)s"
        },
        "myformat": {
            "format": "[%(levelname)s] %(asctime)s %(name)s:%(lineno)s %(funcName)s %(module)s %(process)d %(thread)d:  %(message)s"
        },
    },
    "handlers": {
        "console": {
            "level": "INFO",
            "class": "logging.StreamHandler",
            "formatter": "myformat",
        },
        "file_app": {
            "level": "INFO",
            "class": "logging.FileHandler",
            "formatter": "myformat",
            "filename": "/var/log/backend/app.log",
        },
        "file_sql": {
            "level": "INFO",
            "class": "logging.FileHandler",
            "formatter": "myformat",
            "filename": "/var/log/backend/sql.log",
        },
        "django.server": {
            "level": "INFO",
            "class": "logging.StreamHandler",
            "formatter": "django.server",
        },
        "mail_admins": {
            "level": "ERROR",
            "filters": ["require_debug_false"],
            "class": "django.utils.log.AdminEmailHandler",
        },
    },
    "loggers": {
        "django": {
            "handlers": ["console", "mail_admins"],
            "level": "INFO",
        },
        "django.server": {
            "handlers": ["django.server"],
            "level": "INFO",
            "propagate": False,
        },
        "": {
            "handlers": ["console", "file_app"],
            "level": "INFO",
            "propagate": False,
        },
    },
}

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SECURE_SSL_REDIRECT = True
