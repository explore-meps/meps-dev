from django.core.management.base import BaseCommand
from meps_dev.components.scrapper import ScrapMEPSCodebook


class Command(BaseCommand):
    """ Management command to scrap data files from the MEPS site. Run in terminal.
        ex:
            python manage.py scrap_meps_codebook
            python manage.py scrap_meps_codebook --years 2016 2019 --output_dir "custom/path" --sleep 25
    """

    help = "Scraps the MEPS page variable information "

    def add_arguments(self, parser):
        parser.add_argument("--years", nargs="*", type=int, help="declare a years to scrap data for: 2019 2020")

        parser.add_argument("--output_dir", nargs="?", help="declare the path to the download directory")

        parser.add_argument("--sleep", nargs="?", type=int, help="declare how many seconds to wait between downloads")

    def handle(self, *args, **options):

        kwargs = {}
        for arg in ["years", "output_dir", "sleep"]:
            if options[arg] is not None:
                kwargs.update({arg: options[arg]})

        scrapper = ScrapMEPSCodebook(**kwargs)
        scrapper.run()
