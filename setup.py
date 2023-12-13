from setuptools import setup

setup(
    name='EasyRex',
    version='0.1.0',    
    description='Regular expressions made simple',
    url='https://github.com/shuds13/pyexample',#TODO
    author='Noureddine Ait Hellal',
    author_email='noureddine.ait.hellal1@gmail.com',
    license='BSD 2-clause',
    packages=['EasyRex'],
    install_requires=['mpi4py>=2.0',
                      'numpy',                     
                      ],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        'License :: OSI Approved :: BSD License',  
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)