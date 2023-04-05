# Generated by Django 4.1.7 on 2023-03-25 22:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_booklangage_alter_author_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookLanguage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(help_text='Informe o idioma do Livro', max_length=200)),
            ],
            options={
                'verbose_name': 'Idioma do Livro',
                'verbose_name_plural': 'Idiomas dos Livros',
                'ordering': ['language'],
            },
        ),
        migrations.DeleteModel(
            name='BookLangage',
        ),
        migrations.AddField(
            model_name='book',
            name='language',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.booklanguage'),
        ),
    ]
