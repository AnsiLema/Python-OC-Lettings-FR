from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('lettings', '0003_auto_20250423_1022'),
        ('profiles', '0003_auto_20250423_1022'),
        ('oc_lettings_site', '0002_auto_20250423_1022')
    ]
    operations = [
        migrations.DeleteModel(
            name='Address',
        ),
        migrations.DeleteModel(
            name='Letting',
        ),
        migrations.DeleteModel(
            name='Profile',
        )
    ]