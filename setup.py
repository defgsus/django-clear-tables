from setuptools import setup

setup(
    name='django-clear-tables',
    version='0.1',
    description='manage.py task that clears the content of the django Permission and ContentTypes tables, '
                'after an initial migration, to make manage.py loaddata work.',
    url='https://github.com/defsus/django-clear-tables',
    author='Stefan Berke',
    author_email='s.berke@netzkolchose.de',
    license='MIT',
    packages=['django_clear_tables'],
    zip_safe=False,
)