# Created this file just to host to vercel, but it can be deleted

import os
from django.core.wsgi import get_wsgi_application

# Replace "your_project_name" with your actual project name
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "your_project_name.settings")
app = get_wsgi_application()
