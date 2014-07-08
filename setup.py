# Copyright 2013 Novo Nordisk Foundation Center for Biosustainability,
# Technical University of Denmark.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from setuptools import setup, find_packages
from ipython_notebook_utils import __version__

with open('requirements.txt') as fhandle:
    requirements = [line.strip() for line in fhandle]


setup(
    name='ipython_notebook_utils',
    version=__version__,
    packages=find_packages(),
    install_requires=requirements,  # from requirements.txt
    author='Joao Cardoso',
    author_email='joaca@biosustain.dtu.dk',
    description='IPython Notebook GUI utils',
    license='Apache License Version 2.0',
    keywords='ipython notebook gui utils',
    url='TBD',
    long_description="TODO",
    classifiers=[
        'Topic :: Utilities',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'License :: OSI Approved :: Apache Software License',
    ],
)
