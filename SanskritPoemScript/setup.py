from setuptools import setup, find_packages

setup(
    name='sanskrit-poem-script',
    version='0.1.0',
    description='A unique programming language inspired by Classical Sanskrit Poetry',
    author='Your Name',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'sanskrit-poem-script=sanskrit_poem_script.cli:main'
        ]
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Software Development :: Interpreters'
    ]
)
