from django.core.management.base import BaseCommand
from django.utils import timezone
from traffic.models import Traffic, CongestionType


class Command(BaseCommand):
    help = 'Set all traffic records to "Free" status'

    def handle(self, *args, **options):
        try:
            free_type = CongestionType.objects.get(name='Свободно')
        except CongestionType.DoesNotExist:
            self.stdout.write(self.style.ERROR('Тип "Свободно" не найден!'))
            return

        traffics = Traffic.objects.all()
        count = traffics.count()

        if count == 0:
            self.stdout.write(self.style.WARNING('Нет записей трафика!'))
            return

        updated_count = traffics.update(congestion_type=free_type, last_updated=timezone.now())

        self.stdout.write(
            self.style.SUCCESS(f'Успешно обновлено {updated_count} записей на тип "Свободно"')
        )