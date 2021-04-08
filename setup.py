from setuptools import setup
import pypandoc


setup(name='sparsity-pattern',
      version='0.4.0',
      description=(
          "Generate different types of sparsity pattern for sparse matrices."
      ),
      long_description=pypandoc.convert('README.md', 'rst'),
      url='http://github.com/ulf1/sparsity-pattern',
      author='Ulf Hamster',
      author_email='554c46@gmail.com',
      license='Apache License 2.0',
      packages=['sparsity_pattern'],
      install_requires=[
          'setuptools>=40.0.0'],
      python_requires='>=3.6',
      zip_safe=True)
