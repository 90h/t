from setuptools import setup, find_packages


setup(
    name='khahux_t',
    version='0.1.0',
    author='90h',
    author_email='195022586@qq.com',
    packages = find_packages(),
    zip_safe=False,
    platforms='Mac',
    install_requires=['docopt'],
    entry_points = {
        'console_scripts': [
            'khahux_t = bin.khahux_t:main'
        ]
    },
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
    ]
)
