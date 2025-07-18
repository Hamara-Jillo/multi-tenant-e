# Generated by Django 3.2 on 2025-06-12 11:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('voucher', '0001_initial'),
        ('partner', '0002_initial'),
        ('communication', '0002_initial'),
        ('basket', '0004_initial'),
        ('store_meta', '0001_initial'),
        ('catalogue', '0002_initial'),
        ('sites', '0002_alter_domain_unique'),
        ('address', '0003_initial'),
        ('order', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='ordernote',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
        migrations.AddField(
            model_name='orderdiscount',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='discounts', to='order.order', verbose_name='Order'),
        ),
        migrations.AddField(
            model_name='order',
            name='basket',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='basket.basket', verbose_name='Basket'),
        ),
        migrations.AddField(
            model_name='order',
            name='billing_address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='order.billingaddress', verbose_name='Billing Address'),
        ),
        migrations.AddField(
            model_name='order',
            name='shipping_address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='order.shippingaddress', verbose_name='Shipping Address'),
        ),
        migrations.AddField(
            model_name='order',
            name='site',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sites.site', verbose_name='Site'),
        ),
        migrations.AddField(
            model_name='order',
            name='store',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='store_meta.store'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders', to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
        migrations.AddField(
            model_name='order',
            name='voucher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='voucher.voucher'),
        ),
        migrations.AddField(
            model_name='lineprice',
            name='line',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prices', to='order.line', verbose_name='Line'),
        ),
        migrations.AddField(
            model_name='lineprice',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='line_prices', to='order.order', verbose_name='Option'),
        ),
        migrations.AddField(
            model_name='lineattribute',
            name='line',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attributes', to='order.line', verbose_name='Line'),
        ),
        migrations.AddField(
            model_name='lineattribute',
            name='option',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='line_attributes', to='catalogue.option', verbose_name='Option'),
        ),
        migrations.AddField(
            model_name='line',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lines', to='order.order', verbose_name='Order'),
        ),
        migrations.AddField(
            model_name='line',
            name='partner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='order_lines', to='partner.partner', verbose_name='Partner'),
        ),
        migrations.AddField(
            model_name='line',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalogue.product', verbose_name='Product'),
        ),
        migrations.AddField(
            model_name='line',
            name='stockrecord',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_lines', to='partner.stockrecord', verbose_name='Stock record'),
        ),
        migrations.AddField(
            model_name='communicationevent',
            name='event_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='communication.communicationeventtype', verbose_name='Event Type'),
        ),
        migrations.AddField(
            model_name='communicationevent',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='communication_events', to='order.order', verbose_name='Order'),
        ),
        migrations.AddField(
            model_name='billingaddress',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='address.country', verbose_name='Country'),
        ),
        migrations.AlterUniqueTogether(
            name='shippingeventquantity',
            unique_together={('event', 'line')},
        ),
        migrations.AlterUniqueTogether(
            name='paymenteventquantity',
            unique_together={('event', 'line')},
        ),
        migrations.AlterUniqueTogether(
            name='order',
            unique_together={('store', 'number')},
        ),
    ]
