from setuptools import find_packages, setup

# Read the requirements from requirements.txt
with open('requirements.txt', 'r', encoding='utf-8') as f:
    required = f.read().splitlines()

# Read the contents of your README file
with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="mlops_modular_project",
    version="0.1.0",
    author="Md. Nafiz Imam Zilani",
    author_email="nafiz_zilani@outlook.com",
    description="A modular MLOps project structure",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nafizzilani/mlops_modular_project",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
    ],
    python_requires='>=3.12',
    install_requires=required,
    extras_require={
        'dev': [
           'pytest>=7.1.1',
           'pytest-cov>=2.12.1',
           'flake8>=3.9.0',
           'black>=22.3.0',
           'isort>=5.10.1',
           'mypy>=0.942',
        ],
    }

)