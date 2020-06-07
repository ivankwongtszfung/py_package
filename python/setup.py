from setuptools import setup, find_packages
print(__file__)
setup(
    name="HelloWorld",
    version="0.1",
    packages=find_packages(),
    data_files=[('.',['../text.txt'])],
    include_package_data=True,
    use_scm_version = {
        "root": "..",
        "relative_to": __file__,
        "local_scheme": "node-and-timestamp"
    },
    setup_requires=['setuptools_scm'],
)
