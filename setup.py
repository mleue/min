from setuptools import setup, find_packages

setup(
    name='min',
    version='0.0.1',
    description='minimal manpages.',
    url='',
    author='Michael Leue',
    author_email='michael@mleue.com',
    license='',
    classifiers=[
        'Development Status :: 2 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Documentation',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
    entry_points={
      'console_scripts': ['min=min.cli.cli:min_cli'],
    },
    keywords='manpage minimal man',
    packages=find_packages(exclude=['docs']),
)
