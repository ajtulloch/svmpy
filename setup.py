from setuptools import setup

setup(name='svmpy',
      version='0.1',
      description='Naive SVM library in Python',
      url='http://github.com/ajtulloch/svmpy',
      author='Andrew Tulloch',
      author_email='andrew@tullo.ch',
      license='MIT',
      packages=['svmpy'],
      install_requires=[
          'argh',
          'numpy',
          'matplotlib',
          'cvxopt'
      ],
      zip_safe=False)
