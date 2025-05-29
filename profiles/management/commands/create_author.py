from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from profiles.models import Author

class Command(BaseCommand):
    help = 'Creates a new author with a user account'

    def add_arguments(self, parser):
        parser.add_argument('username', type=str, help='Username for the new author')
        parser.add_argument('email', type=str, help='Email for the new author')
        parser.add_argument('password', type=str, help='Password for the new author')
        parser.add_argument('--first-name', type=str, default='', help='First name of the author')
        parser.add_argument('--last-name', type=str, default='', help='Last name of the author')
        parser.add_argument('--bio', type=str, default='', help='Bio of the author')
        parser.add_argument('--location', type=str, default='', help='Location of the author')
        parser.add_argument('--website', type=str, default='', help='Website of the author')

    def handle(self, *args, **options):
        try:
            # Create user
            user = User.objects.create_user(
                username=options['username'],
                email=options['email'],
                password=options['password'],
                first_name=options['first_name'],
                last_name=options['last_name']
            )

            # Create author
            author = Author.objects.create(
                user=user,
                bio=options['bio'],
                location=options['location'],
                website=options['website'],
                created_by=user,
                updated_by=user
            )

            self.stdout.write(
                self.style.SUCCESS(
                    f'Successfully created author "{author}" with username "{user.username}"'
                )
            )

        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'Error creating author: {str(e)}')
            ) 