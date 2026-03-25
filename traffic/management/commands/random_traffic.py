import random
import time
from django.core.management.base import BaseCommand
from django.utils import timezone
from traffic.models import Traffic, CongestionType


class Command(BaseCommand):
    help = 'Randomly updates traffic'

    def handle(self, *args, **options):
        types = list(CongestionType.objects.all())

        if not types:
            self.stdout.write(self.style.ERROR('Нет типов загруженности!'))
            return

        self.stdout.write('Запуск рандомизатора трафика...')

        while True:
            try:
                traffics = list(Traffic.objects.all())

                if traffics:
                    traffic = random.choice(traffics)
                    old = traffic.congestion_type

                    new = random.choice(types)

                    traffic.congestion_type = new
                    traffic.last_updated = timezone.now()
                    traffic.save()

                    self.stdout.write(f'{traffic.road_segment}: {old.name} -> {new.name}')
                else:
                    self.stdout.write('Нет записей трафика')

                wait = random.randint(2, 5)
                time.sleep(wait)

            except KeyboardInterrupt:
                self.stdout.write(self.style.SUCCESS('\nОстановлено'))
                break