from django.core.management.base import BaseCommand
from restaurant.models import Menu, Booking
from datetime import datetime, timedelta

class Command(BaseCommand):
    help = 'Populates the database with sample data'

    def handle(self, *args, **kwargs):
        # Add menu items
        menu_items = [
            {'Title': 'Greek Salad', 'Price': 12.99, 'Inventory': 100},
            {'Title': 'Bruschetta', 'Price': 8.99, 'Inventory': 80},
            {'Title': 'Grilled Fish', 'Price': 24.99, 'Inventory': 50},
            {'Title': 'Lemon Dessert', 'Price': 7.99, 'Inventory': 60},
            {'Title': 'Pasta Carbonara', 'Price': 16.99, 'Inventory': 70},
        ]

        for item in menu_items:
            Menu.objects.create(**item)
            self.stdout.write(f'Created menu item: {item["Title"]}')

        # Add some sample bookings
        bookings = [
            {'Name': 'John Doe', 'No_of_guests': 4, 'BookingDate': datetime.now() + timedelta(days=1)},
            {'Name': 'Jane Smith', 'No_of_guests': 2, 'BookingDate': datetime.now() + timedelta(days=2)},
            {'Name': 'Mike Johnson', 'No_of_guests': 6, 'BookingDate': datetime.now() + timedelta(days=3)},
        ]

        for booking in bookings:
            Booking.objects.create(**booking)
            self.stdout.write(f'Created booking for: {booking["Name"]}')
