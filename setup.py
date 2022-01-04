import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="CNVMatrixGenerator", # Replace with your own username
    version="0.0.1",
    author="Azhar Khandekar",
    author_email="akhandek@eng.ucsd.edu",
    license='UCSD',
    description="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    install_requires =[
                        "matplotlib>=2.2.2",
                        "sigProfilerPlotting>=1.0.1",
                        "numpy>=1.18.5",
                        "pandas>=0.23.4"],

    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
    zip_safe=False
)
