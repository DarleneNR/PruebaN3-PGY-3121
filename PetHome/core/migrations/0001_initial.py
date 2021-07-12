# Generated by Django 3.2.3 on 2021-07-12 01:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('idCategoria', models.AutoField(primary_key=True, serialize=False, verbose_name='Identificador del Producto')),
                ('nombreCategoria', models.CharField(help_text='Introduzca el tipo de Categoría', max_length=70, verbose_name='Nombre Categoría')),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('nroRutCli', models.IntegerField(primary_key=True, serialize=False, verbose_name='Número Rut del cliente')),
                ('dvRun', models.CharField(help_text='Introduzca el dígito verificador de su rut', max_length=1, verbose_name='Dígito Verificador')),
                ('nombreCli', models.CharField(help_text='Introduzca su nombre completo', max_length=70, verbose_name='Nombre Cliente')),
                ('apellidocli', models.CharField(help_text='Introduzca su(s) apellido(s)', max_length=80, verbose_name='Apellido Cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('idProducto', models.AutoField(primary_key=True, serialize=False, verbose_name='Identificador del Producto')),
                ('nombreProducto', models.CharField(help_text='Introduzca el nombre', max_length=70, verbose_name='Nombre Producto')),
                ('precioUnidad', models.IntegerField(help_text='Introduzca el precio por prodcuto', verbose_name='Precio Producto')),
                ('cantStock', models.IntegerField(help_text='Introduzca cantidad de Stock disponible', verbose_name='Stock disponible')),
                ('idCategoria', models.ForeignKey(help_text='Selecciona la Categoría', on_delete=models.SET('CategoríaEliminada'), to='core.categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Suscrito',
            fields=[
                ('idSuscripcion', models.AutoField(primary_key=True, serialize=False, verbose_name='Identificador de la Suscripción')),
                ('nombreUser', models.CharField(help_text='Introduzca el nombre de usuario', max_length=30, unique=True, verbose_name='Nombre de usuario')),
                ('fechaSuscripcion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha en la que el usuario se suscribió')),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('nroVenta', models.AutoField(primary_key=True, serialize=False, verbose_name='Identificador de la Venta')),
                ('cantidad', models.CharField(blank=True, help_text='Introduzca el modelo', max_length=20, null=True, verbose_name='Modelo')),
                ('montoVenta', models.IntegerField(verbose_name='Monto Total a pagar')),
                ('idProducto', models.ForeignKey(help_text='Selecciona Producto', on_delete=models.SET('ProductoEliminado'), to='core.producto')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('idUser', models.AutoField(primary_key=True, serialize=False, verbose_name='Identificador del Usuario')),
                ('nombreUser', models.CharField(help_text='Introduzca el nombre de usuario', max_length=30, unique=True, verbose_name='Nombre de usuario')),
                ('passwordUser', models.CharField(help_text='Introduzca la contraseña', max_length=10, verbose_name='Contraseña')),
                ('nroRutCli', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.cliente', verbose_name='Número Rut sin dígito verificador')),
            ],
        ),
    ]
