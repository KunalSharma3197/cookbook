from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from utils.models import File
import os

class Command(BaseCommand):
    help = 'Creates a new file entry'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Path to the file')
        parser.add_argument('name', type=str, help='Name of the file')
        parser.add_argument('--description', type=str, default='', help='Description of the file')
        parser.add_argument('--file-type', type=str, help='MIME type of the file')
        parser.add_argument('--s3-key', type=str, help='S3 key for the file')

    def handle(self, *args, **options):
        try:
            # Get or create a system user
            user, created = User.objects.get_or_create(
                username='system_user',
                defaults={
                    'email': 'system@example.com',
                    'is_active': True
                }
            )
            if created:
                user.set_password('system_password')
                user.save()

            # Get file type if not provided
            file_type = options['file_type']
            if not file_type:
                import mimetypes
                file_type, _ = mimetypes.guess_type(options['file_path'])
                if not file_type:
                    file_type = 'application/octet-stream'

            # Get S3 key if not provided
            s3_key = options['s3_key']
            if not s3_key:
                s3_key = os.path.join('files', os.path.basename(options['file_path']))

            # Create file entry
            file_entry = File.objects.create(
                file=options['file_path'],
                name=options['name'],
                description=options['description'],
                file_type=file_type,
                s3_key=s3_key,
                created_by=user,
                updated_by=user
            )

            self.stdout.write(
                self.style.SUCCESS(
                    f'Successfully created file entry "{file_entry}" with ID {file_entry.id}'
                )
            )

        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'Error creating file entry: {str(e)}')
            ) 