from setuptools import setup, find_packages

with open('README.rst') as f:
    long_description = f.read()

setup(
    name='bounded_executor',
    version='0.0.5',
    description='Bounded ThreadPoolExecutor and ProcessPoolExecutor',
    long_description=long_description,
    long_description_content_type='text/x-rst',
    author='Yanbin',
    author_email='yabqiu@gmail.com',
    url='https://github.com/yabqiu/bounded-pool-executor',
    license='BSD License',
    packages=find_packages(),
    platforms=['all'],
    python_requires='>=3.2',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ]
)
