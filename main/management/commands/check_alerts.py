from django.core.management.base import BaseCommand

from main.models import Alert


class Command(BaseCommand):
    help = 'Updates all Teachable data using API.'

    def handle(self, *args, **options):
        for alert in Alert.objects.all():
            if alert.expired:
                print("Alert {} for product {} has been already activated {} days ago.".format(alert.id,
                                                                                               alert.product.name,
                                                                                               alert.days_since_activation))
            else:
                print("Alert {} for product {} will be activated in {} days.".format(alert.id,
                                                                                     alert.product.name,
                                                                                     alert.days_until_activation))
