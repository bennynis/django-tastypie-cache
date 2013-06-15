from setuptools import setup

setup(
    name='django-tastypie-cache',
    version='0.1',
    zip_safe = False,
    include_package_data=True,
    url='http://github.com/dstegelman/django-tastypie-cache',
    license='MIT',
    author='Derek Stegelman',
    author_email='email@stegelman.com',
    description='Cache mixin for Django Tastypie',
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        'Programming Language :: Python :: 2.7',
        "Framework :: Django",
        ],
    )