# WARNING: template code, may need edits
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="sample_calculator_dify",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A simple, well-structured Python calculator application",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/sample_calculator_dify",
    package_dir={"calculator": "src/calculator"},
    packages=find_packages(where="src"),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    install_requires=[],
    extras_require={
        "dev": [
            "pytest>=7.4.0",
            "pytest-cov>=4.1.0",
            "black>=23.7.0",
            "flake8>=6.1.0",
            "mypy>=1.5.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "calculator=calculator.cli:main",
        ],
    },
)
