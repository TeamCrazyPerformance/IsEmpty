from __future__ import unicode_literals
from django.db import migrations
from django.utils import timezone


def forwards_func(apps, schema_editor):
    Room = apps.get_model("booking", "Room")
    Booking = apps.get_model("booking", "Booking")
    db_alias = schema_editor.connection.alias
    Room.objects.using(db_alias).bulk_create([
        Room(room_number="310"),
        Room(room_number="311"),
        Room(room_number="312"),
        Room(room_number="313"),
        Room(room_number="314"),
        Room(room_number="315")
    ])
    Booking.objects.using(db_alias).bulk_create([
        Booking(room_id=1, user_id=3, book_date=timezone.datetime(2017, 11, 10).date(), start_hour="18", start_min="00",
                end_hour="20", end_min="30", purpose="팀 프로젝트", participants=5),
        Booking(room_id=2, user_id=4, book_date=timezone.datetime(2017, 11, 10).date(), start_hour="18", start_min="30",
                end_hour="21", end_min="00", purpose="모르겠다", participants=5),
        Booking(room_id=3, user_id=5, book_date=timezone.datetime(2017, 11, 10).date(), start_hour="19", start_min="00",
                end_hour="22", end_min="30", purpose="시험기간 공부", participants=10),
        Booking(room_id=4, user_id=1, book_date=timezone.datetime(2017, 11, 11).date(), start_hour="16", start_min="00",
                end_hour="19", end_min="00", purpose="관리자예약", participants=4),
        Booking(room_id=4, user_id=4, book_date=timezone.datetime(2017, 11, 11).date(), start_hour="19", start_min="00",
                end_hour="21", end_min="00", purpose="11일 예약", participants=6),
        Booking(room_id=1, user_id=2, book_date=timezone.datetime(2017, 11, 11).date(), start_hour="19", start_min="00",
                end_hour="21", end_min="00", purpose="11일 예약", participants=6),
        Booking(room_id=5, user_id=2, book_date=timezone.datetime(2017, 11, 11).date(), start_hour="17", start_min="00",
                end_hour="19", end_min="00", purpose="11일 예약", participants=6),
        Booking(room_id=4, user_id=3, book_date=timezone.datetime(2017, 11, 12).date(), start_hour="18", start_min="00",
                end_hour="20", end_min="00", purpose="팀 프로젝트~", participants=6),
        Booking(room_id=4, user_id=3, book_date=timezone.datetime(2017, 11, 12).date(), start_hour="20", start_min="00",
                end_hour="22", end_min="30", purpose="팀 프로젝트해요", participants=4),
        Booking(room_id=1, user_id=4, book_date=timezone.datetime(2017, 11, 12).date(), start_hour="18", start_min="00",
                end_hour="22", end_min="00", purpose="팀 프로젝트해요", participants=10),
        Booking(room_id=6, user_id=1, book_date=timezone.datetime(2017, 11, 12).date(), start_hour="20", start_min="00",
                end_hour="22", end_min="30", purpose="팀 프로젝트해요", participants=4),
    ])


def reverse_func(apps, schema_editor):
    pass


class Migration(migrations.Migration):
    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(forwards_func, reverse_func),
    ]
