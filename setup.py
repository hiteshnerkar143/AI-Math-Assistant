#!/usr/bin/env python
"""
Setup script for AI Math Assistant
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="ai-math-assistant",
    version="1.0.0",
    author="AI Math Assistant Team",
    description="AI-powered Mathematics Assistant with Modern GUI",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/ai-math-assistant",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Mathematics",
        "Topic :: Education",
    ],
    python_requires=">=3.8",
    install_requires=[
        "customtkinter>=5.2.0",
        "Pillow>=10.1.0",
        "scikit-learn>=1.3.2",
        "numpy>=1.26.3",
        "sympy>=1.12",
        "scipy>=1.11.4",
        "matplotlib>=3.8.2",
        "reportlab>=4.0.7",
        "SpeechRecognition>=3.10.0",
        "pyttsx3>=2.90",
        "pandas>=2.1.4",
        "python-dateutil>=2.8.2",
    ],
    entry_points={
        "console_scripts": [
            "ai-math-assistant=main:main",
        ],
    },
)
