from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='backutil',
      version='0.1.3',
      description='Python backup utility',
      long_description=readme(),
      url='https://github.com/heywoodlh/backutil',
      author='Spencer Heywood',
      author_email='l.spencer.heywood@gmail.com',
      license='APACHE-2.0',
      packages=['backutil'],
      scripts=['bin/backutil'],
      install_requires=[
          'requests',
      ],
      zip_safe=False)
