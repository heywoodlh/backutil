from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='backutil',
      version='0.1',
      description='Python backup utility',
      long_description=readme(),
      url='https://github.com/heywoodlh/backutil',
      author='Spencer Heywood',
      author_email='l.spencer.heywood@gmail.com',
      license='APACHE-2.0',
      packages=['backutil'],
      scripts=['bin/backutil'],
      zip_safe=False)
