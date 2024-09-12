from setuptools import setup

setup(
    name="jupyterhub-ldapauthenticator",
    version="2.0.0.dev",
    description="LDAP Authenticator for JupyterHub",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/jupyterhub/ldapauthenticator",
    author="Yuvi Panda",
    author_email="yuvipanda@riseup.net",
    license="3 Clause BSD",
    packages=["ldapauthenticator"],
    python_requires=">=3.8",
    install_requires=[
        "jupyterhub>=2.3.1",
        "ldap3",
        "tornado",
        "traitlets",
    ],
    extras_require={
        "test": [
            "pytest",
            "pytest-asyncio",
            "pytest-cov",
        ],
    },
)
