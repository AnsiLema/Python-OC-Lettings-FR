from django.db import migrations

def copy_lettings(apps, schema_editor):
    old_address = apps.get_model('oc_lettings_site', 'Address')
    old_letting = apps.get_model('oc_lettings_site', 'Letting')
    new_address = apps.get_model('lettings', 'Address')
    new_letting = apps.get_model('lettings', 'Letting')

    addr_map = {}
    for old_addr in old_address.objects.all():
        new_addr = new_address.objects.create(
            number = old_addr.number,
            street = old_addr.street,
            city = old_addr.city,
            state = old_addr.state,
            zip_code = old_addr.zip_code,
            country_iso_code = old_addr.country_iso_code,
        )
        addr_map[old_addr.pk] = new_addr

    for old_let in old_letting.objects.all():
        new_letting.objects.create(
            title = old_let.title,
            address = addr_map[old_let.address_id],
        )

class Migration(migrations.Migration):
    dependencies = [
        ('lettings', '0001_initial'),
        ('oc_lettings_site', '0001_initial'),
    ]
    operations = [
        migrations.RunPython(copy_lettings),
    ]