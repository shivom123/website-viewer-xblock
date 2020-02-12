"""Setup for xblock_website_viewer XBlock."""

import os
from setuptools import setup


def package_data(pkg, roots):
    """Generic function to find package_data.

    All of the files under each of the `roots` will be declared as package
    data for package `pkg`.

    """
    data = []
    for root in roots:
        for dirname, _, files in os.walk(os.path.join(pkg, root)):
            for fname in files:
                data.append(os.path.relpath(os.path.join(dirname, fname), pkg))

    return {pkg: data}


setup(
    name='xblock_website_viewer',
    version='1.0.0',
    description='View any website in your XBlock',
    license='UNKNOWN',          
    packages=[
        'xblock_website_viewer',
    ],
    install_requires=[
        'XBlock',
        'requests'
    ],
    entry_points={
        'xblock.v1': [
            'xblock_website_viewer = xblock_website_viewer:WebsiteViewerXBlock',
        ]
    },
    package_data=package_data("xblock_website_viewer", ["static", "public", "rest"]),
)
