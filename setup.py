from pathlib import Path

import setuptools

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setuptools.setup(
    name="streamlit_copilot",
    version="0.0.1",
    author="Anastasiia Sobkevych",
    author_email="sobkevich.anastasia@gmail.com",
    description="Streamlit component: Copilot text autocomplete",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sobkevich/streamlit-copilot",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[],
    python_requires=">=3.6",
    install_requires=[
        # By definition, a Custom Component depends on Streamlit.
        # If your component has other Python dependencies, list
        # them here.
        "streamlit >= 0.63",
    ],
)
