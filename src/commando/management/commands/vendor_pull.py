import helpers

from typing import Any
from django.core.management.base import BaseCommand
from django.conf import settings

STATICFILES_VENDOR_DIR = getattr(settings, 'STATICFILES_VENDOR_DIR')


VENDOR_STATICFILES = {
    "saas-theme.min.css": "https://raw.githubusercontent.com/codingforentrepreneurs/SaaS-Foundations/main/src/staticfiles/theme/saas-theme.min.css",
    "flowbite.min.css": "https://cdnjs.cloudflare.com/ajax/libs/flowbite/2.3.0/flowbite.min.css",
    "flowbite.min.js": "https://cdnjs.cloudflare.com/ajax/libs/flowbite/2.3.0/flowbite.min.js",
    "flowbite.min.js.map": "https://cdnjs.cloudflare.com/ajax/libs/flowbite/2.3.0/flowbite.min.js.map"
}

class Command(BaseCommand):

    def handle(self, *args: Any, **options: Any):
        self.stdout.write("Hello, world! This is a custom management command.")
        completed_urls = []
        for filename, url in VENDOR_STATICFILES.items():
            local_path = STATICFILES_VENDOR_DIR / filename
            self.stdout.write(f"Downloading {filename} from {url} to {local_path}")
            success = helpers.downloader.download_to_local(url, local_path, parent_mkdir=True)
            if success:
                self.stdout.write(f"Successfully downloaded {filename}")
                completed_urls.append(url)
            else:
                self.stdout.write(
                    self.style.ERROR(f"Failed to download {filename}")
                )
        if set(completed_urls) == set(VENDOR_STATICFILES.values()):
            self.stdout.write(self.style.SUCCESS("All vendor static files have been pulled successfully."))
        else:
            self.stdout.write(self.style.WARNING("Some vendor static files could not be pulled. Please check the logs."))