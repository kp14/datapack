from setuptools import setup


# def readme():
#     with open('README.rst') as f:
#         return f.read()


setup(name='ansi_files',
      version='0.3',
      description='Some ancillary files',
      long_description="blah blah blah",
      # long_description=readme(),
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
        'Topic :: Text Processing :: Linguistic',
      ],
      keywords='ZCS skip syn',
      url='http://some/url/here',
      author='Ann Sillary',
      author_email='ann@sillary.com',
      license='MIT',
      packages=['ansi_files'],
      install_requires=[
          # 'markdown',
      ],
      # test_suite='nose.collector',
      # tests_require=['nose', 'nose-cover3'],
      # entry_points={
      #     'console_scripts': ['funniest-joke=funniest.command_line:main'],
      # },
      include_package_data=True,
      zip_safe=False)