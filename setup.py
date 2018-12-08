from distutils.core import setup

setup(
    name='flickrpub',
    version='0.0.1',
    url='https://github.com/al4/flickrpub',
    license='MIT',
    author='al4',
    author_email='',
    description='',
    entry_points={
        'console_scripts':
            [
                'flickrpub = flickrpub.__main__:main'
            ]
    }
)
