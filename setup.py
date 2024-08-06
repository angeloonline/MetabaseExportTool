from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))
# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(name='MetabaseExportTool',
      version='0.0.1',
      description='Metabase Export Tool',
      long_description=long_description,
      long_description_content_type="text/markdown",
      # The project's main homepage.
      url='https://github.com/angeloonline/MetabaseExportTool.git',
      # Author details
      author='Angeloonline',
      author_email='angeloonline@inwind.it',
      license='MIT',
      # What does your project relate to?
      keywords='metabase export database',
      packages=find_packages(),
      package_data={'MetabaseExportTool': ['config_db.yml']},
      include_package_data=True,
      # List run-time dependencies here.  These will be installed by pip when
      # your project is installed.
      install_requires=[
          'importlib_resources;python_version<"3.7"',
          'peewee', 'PyQt5', 'PyYAML', 'PyMySQL'
      ],
      # List required Python versions
      python_requires='>=3.6',
      zip_safe=False,
      entry_points={
          'console_scripts':['metabase-export = MetabaseExportTool.MainWindow:runMetabaseExportToolGUI']
                    }
      )