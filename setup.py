from setuptools import setup

setup(
    name='initialapp',
    packages=['initialapp'],
    include_package_data=True,
    install_requires=[
        'flask',
        'flask_restplus',
        'pytest'
    ],
    setup_requires=[
        'pytest-runner'
    ],
    tests_require=[
        'pytest'
    ]
)
