import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "CuidaLA.settings")
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
from Database.models import User, Locations, Jobs, Applicants, Skills
from datetime import datetime