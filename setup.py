import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="rv_curve_jura",
    version="0.1",
    author="Khaled Al Moulla",
    author_email="khaled.almoulla@gmail.com",
    description="Plot all RV curves that you want!",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/almoulla/jura_workshop_khaled",
    packages=setuptools.find_packages(),
    install_requires=["numpy","matplotlib"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Indepedent",
    ]
)