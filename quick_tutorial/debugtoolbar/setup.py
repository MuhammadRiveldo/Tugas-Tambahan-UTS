from setuptools import setup

# Dependencies utama
requires = [
    'pyramid',
    'waitress',
]

# Dependencies tambahan khusus development
dev_requires = [
    'pyramid_debugtoolbar',
]

setup(
    name='tutorial',
    install_requires=requires,
    extras_require={
        'dev': dev_requires,
    },
    entry_points={
        'paste.app_factory': [
            'main = tutorial:main'
        ],
    },
)
