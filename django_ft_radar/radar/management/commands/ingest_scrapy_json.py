import os
import json
import types

from django.core.management.base import BaseCommand, CommandError

from radar.models import Lead, Company, Category, Source, LeadStatus

class Command(BaseCommand):
    help = 'Command to load JSON data from Scrapy into Radar'

    def _is_not_valid_file_name(self, options):
        file_name = "".join(options['file_name']).strip()
        return (file_name.strip() == "" 
            or not os.path.exists(file_name))

    def add_arguments(self, parser):
            parser.add_argument(
                '--file_name', '-f', type=str,
                help='JSON file from Scrapy',dest="file_name",
                action="append")

    def handle(self, *args, **options):
        if options['file_name'] is None or self._is_not_valid_file_name(options):
            raise CommandError("--file is a required argument, also ensure valid file")

        file_name = "".join(options['file_name'])
        posts = json.loads(open(file_name).read())

        for item in posts:
            source = Source.objects.get(name=item['source'])

            if Category.objects.filter(name=item['category']).exists():
                category = Category.objects.get(name=item['category'])
            else:
                category = Category.objects.get(name='others')

            status = LeadStatus.objects.get(name="Pending")

            lead = Lead()
            lead.title = item['title']
            lead.location = item['location']
            lead.category = category
            lead.source = source
            lead.source_url = item['source_url']
            lead.status = status
            lead.blurb = item['blurb']
            lead.save()

        print("Completed Loading JSON File")
