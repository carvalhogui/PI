import environ
from bo.settings.base import *

env=environ.Env()

DEBUG= env.bool("DEBUG", False)

SECRET_KEY = env("SECRECT_KEY")

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")

DATABASES = {
	"default": env.db(),
}