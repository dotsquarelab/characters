from setuptools import find_packages, setup

install_requires = [
    "openai",
    "langchain",
    "faiss-cpu",
    "tiktoken",
    "python-dotenv",
    "streamlit",
    "streamlit-chat",
    "wheel",
]


test_requires = [
    "flake8",
    "pylint",
    "pytest",
    "pytest-cov",
    "pytest-env",
    "pytest-sugar",
]

dev_requires = test_requires + [
    "pre-commit",
    "ipdb",
    "jupyterlab",
]


setup(
    name="characters",
    version="0.0.1",
    description="",
    python_requires=">=3.10",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=install_requires,
    extras_require={
        "test": test_requires,
        "dev": dev_requires,
    },
)
