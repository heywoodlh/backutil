from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='pybackup',
      version='0.1',
      description='Python backup utility',
      long_description=readme(),
      url='https://github.com/heywoodlh/pybackup',
      author='Spencer Heywood',
      author_email='l.spencer.heywood@gmail.com',
      license='APACHE-2.0',
      packages=['pybackup'],
      scripts=['bin/pybackup'],
      zip_safe=False)
