from setuptools import setup

requires = [
    'pyramid==1.9.1',
    'waitress==1.1.0',
    'pyramid-debugtoolbar',
    'kafka-python==1.4.2',
    'pyramid-chameleon==0.3',
    'cornice==3.1',
    'sqlalchemy==1.2',
    'pyramid-tm==2.2',
    'zope.sqlalchemy==1.0',
    'psycopg2-binary',
    'gunicorn',
    'eventlet',
    "pycryptodomex",
    "requests",
    "six",
    "future"
]

setup(
    name='resefex',
    version='0.1',
    packages=['resefex'],
    url='',
    license='GPLv3',
    author='Nejc Gašper',
    author_email='nejc.gasper@gmail.com',
    description='',
    install_requires=requires,
    entry_points="""\
    [paste.app_factory]
    main = resefex:main
    [console_scripts]
    initialize_db = resefex.db.initialize:main
    processor = resefex.engine.processor:main
    store_balance = resefex.storage.store_balance:main
    store_orderbookdata = resefex.storage.store_orderbookdata:main
    """
)
