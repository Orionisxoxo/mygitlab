from setuptools import setup, find_packages
from mygitlab.dataservice import __version__


setup(name='mygitlab-data',
      version=__version__,
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      entry_points="""
      [console_scripts]
      mygitlab-dataservice = mygitlab.dataservice.run:main
      """)
