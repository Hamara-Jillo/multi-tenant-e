# Generated by Django 3.2 on 2025-06-12 11:05

from decimal import Decimal
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import oscar.models.fields.autoslugfield


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('address', '0002_useraddress_store'),
        ('contenttypes', '0002_remove_content_type_name'),
        ('store_meta', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShippingMethod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', oscar.models.fields.autoslugfield.AutoSlugField(blank=True, editable=False, max_length=128, populate_from='name', unique=True, verbose_name='Slug')),
                ('name', models.CharField(db_index=True, max_length=128, unique=True, verbose_name='Name')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('enabled', models.BooleanField(default=True, verbose_name='Enabled')),
                ('countries', models.ManyToManyField(blank=True, to='address.Country', verbose_name='Countries')),
                ('polymorphic_ctype', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_shipping.shippingmethod_set+', to='contenttypes.contenttype')),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shipping_methods', to='store_meta.store', verbose_name='Store')),
            ],
            options={
                'verbose_name': 'Shipping Method',
                'verbose_name_plural': 'Shipping Methods',
                'ordering': ['name'],
                'abstract': False,
                'unique_together': {('store', 'code')},
            },
        ),
        migrations.CreateModel(
            name='OrderAndItemCharges',
            fields=[
                ('shippingmethod_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='shipping.shippingmethod')),
                ('price_per_order', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=12, verbose_name='Price per order')),
                ('price_per_item', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=12, verbose_name='Price per item')),
                ('free_shipping_threshold', models.DecimalField(blank=True, decimal_places=2, help_text='Order total needed for free shipping', max_digits=12, null=True, verbose_name='Free Shipping Threshold')),
            ],
            options={
                'verbose_name': 'Order and Item Charge',
                'verbose_name_plural': 'Order and Item Charges',
                'ordering': ['name'],
                'abstract': False,
            },
            bases=('shipping.shippingmethod', models.Model),
        ),
        migrations.CreateModel(
            name='WeightBased',
            fields=[
                ('shippingmethod_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='shipping.shippingmethod')),
                ('default_weight', models.DecimalField(decimal_places=3, default=Decimal('0.000'), help_text='Default weight (kg) for products without weight attribute', max_digits=12, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))], verbose_name='Default Weight')),
            ],
            options={
                'verbose_name': 'Weight-based Shipping Method',
                'verbose_name_plural': 'Weight-based Shipping Methods',
                'ordering': ['name'],
                'abstract': False,
            },
            bases=('shipping.shippingmethod', models.Model),
        ),
        migrations.CreateModel(
            name='WeightBand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upper_limit', models.DecimalField(db_index=True, decimal_places=3, help_text='Enter upper limit of this weight band in kg. The lower limit will be determined by the other weight bands.', max_digits=12, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))], verbose_name='Upper Limit')),
                ('charge', models.DecimalField(decimal_places=2, max_digits=12, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))], verbose_name='Charge')),
                ('method', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bands', to='shipping.weightbased', verbose_name='Weight Based Method')),
            ],
            options={
                'verbose_name': 'Weight Band',
                'verbose_name_plural': 'Weight Bands',
                'ordering': ['upper_limit'],
                'abstract': False,
            },
        ),
    ]
