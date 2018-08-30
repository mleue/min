from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as fh:
  long_description = fh.read()

setup(
  name='miniman',
  version='0.0.4',
  description='minimal manpages.',
  long_description=long_description,
  long_description_content_type='text/markdown',
  url='',
  author='Michael Leue',
  author_email='michael@mleue.com',
  license='',
  classifiers=[
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Documentation',
    'Programming Language :: Python :: 3',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
  ],
  entry_points={
    'console_scripts': ['min=min.cli.cli:min_cli'],
  },
  keywords='manpage minimal man',
  packages=find_packages(),
  package_data={'min': ['docs/*/*']},
)
