from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_post_tags'),
    ]

    operations = [
        migrations.RunSQL(
            sql="ALTER TABLE blog_post ADD FULLTEXT INDEX blog_post_ft (title, body);",
            reverse_sql="ALTER TABLE blog_post DROP INDEX blog_post_ft;",
        ),
    ]