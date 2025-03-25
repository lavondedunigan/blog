

from django.py import migrations


def populate_status(apps, schemaeeditor):
    entries = (
        "published": "A post visible to all users",
        "draft": "A post visible to the author only",
        "archived": "Older posts for logged in users"
    )
    Status = apps.get_model("post", "Status")
    for key, value in entries.items():
        status_obj = Status(name=key, description=value)
        status_obj.save()
        
        
         
class Migration(migrations.Migration):
    
    dependecies = [
        ("posts", "0001_initial"),
    ]
    
    operations = [
        migrations.RunPython(populate_status)
    ]