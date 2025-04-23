from django.db import migrations

def copy_profiles(apps, schema_editor):
    old_profile = apps.get_model('oc_lettings_site', 'Profile')
    new_profile = apps.get_model('profiles', 'Profile')

    for old_p in old_profile.objects.all():
        new_profile.objects.create(
            user = old_p.user,
            favorite_city = old_p.favorite_city,
        )

class Migration(migrations.Migration):
    dependencies = [
        ('profiles', '0001_initial'),
        ('oc_lettings_site', '0001_initial'),
    ]
    operations = [
        migrations.RunPython(copy_profiles),
    ]