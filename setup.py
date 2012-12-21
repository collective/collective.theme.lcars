# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import os

version = open(os.path.join("collective", "theme", "lcars", "version.txt")).read().strip()

setup(name='collective.theme.lcars',
      version=version,
      description="LCARS inspired Diazo Theme for Plone",
      long_description=open('README.rst').read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Framework :: Zope2",
        "Framework :: Zope3",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Framework :: Plone :: 4.1",
        "Framework :: Plone :: 4.2",
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        ],
      keywords='web zope plone theme skin',
      author='Christian Ledermann',
      author_email='christian.ledermann@gmail.com',
      url='https://github.com/cleder/collective.theme.lcars',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective', 'collective.theme'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'plone.app.themingplugins',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      )

