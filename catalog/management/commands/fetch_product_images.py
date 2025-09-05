import os
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
from django.conf import settings
import requests
from catalog.models import Product, ProductImage

IMAGE_MAP = [
    (1,  "spinning_graphiteleader.jpg", "https://images.unsplash.com/photo-1558981285-6f0c94958bb6"),
    (2,  "feeder_shimano_beastmaster.jpg", "https://images.unsplash.com/photo-1519562990207-3caef6f90d05"),
    (3,  "reel_daiwa_ninja.jpg", "https://images.unsplash.com/photo-1625591342236-2aa7e5b45fc5"),
    (4,  "reel_shimano_sienna.jpg", "https://images.unsplash.com/photo-1542367597-2261f6e1d5a6"),
    (5,  "lure_megabass_vision.jpg", "https://images.unsplash.com/photo-1594909122845-11baa439b7f3"),
    (6,  "spinner_mepps_aglia.jpg", "https://images.pexels.com/photos/6478093/pexels-photo-6478093.jpeg"),
    (7,  "softbait_keitech_swing.jpg", "https://images.pexels.com/photos/6478127/pexels-photo-6478127.jpeg"),
    (8,  "line_sunline_fc.jpg", "https://images.unsplash.com/photo-1516299023765-1c7c3e9247b1"),
    (9,  "braid_powerpro.jpg", "https://images.unsplash.com/photo-1470167290877-7d5d3446de4c"),
    (10, "hooks_owner_iseama.jpg", "https://images.pexels.com/photos/45851/pexels-photo-45851.jpeg"),
    (11, "net_foldable.jpg", "https://images.pexels.com/photos/674688/pexels-photo-674688.jpeg"),
    (12, "tacklebox_plano_3600.jpg", "https://images.pexels.com/photos/1669240/pexels-photo-1669240.jpeg"),
]

class Command(BaseCommand):
    help = "Download product images and attach to first 12 products"

    def handle(self, *args, **kwargs):
        media_dir = os.path.join(settings.MEDIA_ROOT, "products")
        os.makedirs(media_dir, exist_ok=True)
        for pk, fname, url in IMAGE_MAP:
            self.stdout.write(f"Downloading {fname}…")
            import requests
            r = requests.get(url, timeout=30)
            r.raise_for_status()
            product = Product.objects.get(pk=pk)
            ProductImage.objects.filter(product=product).delete()
            img = ProductImage(product=product, is_primary=True)
            img.image.save(fname, ContentFile(r.content), save=True)
        self.stdout.write(self.style.SUCCESS("Images downloaded and linked."))
