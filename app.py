# Created this file just to host to vercel, but it can be deleted

import os
from django.core.wsgi import get_wsgi_application

# for accessing Django modules and also kufikia settings za Project
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "AirBnB.settings")
app = get_wsgi_application()
