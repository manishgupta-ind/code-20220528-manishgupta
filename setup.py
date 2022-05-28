from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='BMI_Calculator',
        version='0.1',
        description='BMI, BMI Category, Health Risk calculation',
        long_description=long_description,
        long_description_content_type="text/markdown",
        url='#',
        author='Manish Gupta',
        author_email='mgupta.power@gmail.com',
        license='MIT',
        python_requires='>=3.6',
        packages=['BMI_Calculator'],
        install_requires=['BMI_Calculator'],
        zip_safe=False)