from setuptools import setup, find_packages


setup(name='mygitlab-tokendealer',
      version="0.1",
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      entry_points="""
      [console_scripts]
      mygitlab-tokendealer = mygitlab.tokendealer.run:main
      """)
