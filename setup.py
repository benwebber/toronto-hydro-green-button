from setuptools import setup

setup(
    name='toronto-hydro-green-button',
    version='0.1.0',
    url='https://github.com/benwebber/toronto-hydro-green-button/',
    author='Ben Webber',
    author_email='benjamin.webber@gmail.com',
    py_modules=['toronto_hydro_green_button'],
    entry_points={
        'console_scripts': [
            'toronto-hydro-green-button = toronto_hydro_green_button:main',
        ],
    },
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    install_requires=['requests', 'selenium'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3 :: Only',
    ],
)
