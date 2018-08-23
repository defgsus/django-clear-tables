## django-clear-tables v0.1.2

This is a simple django-app, registering a task called `django_clear_tables`.

It will delete the contents of django's **Permission** and **ContentTypes** models 
so you can load data from a fixture without problems. Normally, an initial `migrate` will 
create permission and content-type data. If you want to clone data from another instance,
to a fresh database, this data will clash with the `loaddata` command.  

**Be careful** because it can also easily mess up your existing database. 

Install it with:

```bash
pip install django-clear-tables
```

Usage is as follows:

Add `django_clear_tables` to `INSTALLED_APPS` in your django `settings.py`, then:

```bash
# initially setup the database
rm db.sqlite3  # or using mysql, pg, ...
./manage.py migrate
# wipe the initially created data
./manage.py django_clear_tables
# load a fixture from somewhere else
./manage.py loaddata dumpdata-from-another-instance.json
```
