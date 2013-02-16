from setuptools import setup, find_packages
import os

version = '0.0.1'
here = os.path.abspath(os.path.dirname(__file__))
long_description = open(os.path.join(here, 'README.rst')).read()

setup(name='pable',
      version=version,
      description="tables at terminal with python",
      long_description=long_description,
      classifiers=[
      'Environment :: Console',
      'Intended Audience :: Developers',
      'License :: OSI Approved :: MIT License',
      'Natural Language :: English',
      'Operating System :: OS Independent',
      'Topic :: Utilities',
      ],
      keywords='table row',
      author='Bernardo B. Marques',
      author_email='bernardo.fire@gmail.com',
      url='http://github.com/bernardofire/pable',
      license='MIT',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False
      )

