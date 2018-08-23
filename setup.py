from setuptools import setup

setup(
    name='django-clear-tables',
    version='0.1.2',
    description='django manage.py task that clears the content of the django Permission and ContentTypes tables, '
                'after an initial migration, to make manage.py loaddata work.',
    long_description=open("./README.md").read(),
    long_description_content_type="text/markdown",
    url='https://github.com/defgsus/django-clear-tables',
    author='Stefan Berke',
    author_email='s.berke@netzkolchose.de',
    license='MIT',
    packages=[
        'django_clear_tables',
        'django_clear_tables.management',
        'django_clear_tables.management.commands'
    ],
    zip_safe=False,
)