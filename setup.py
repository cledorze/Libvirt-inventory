#!/usr/bin/python

from setuptools import setup

setup(
    name="libvirt-inventory",
    version="0.0.1",
    description="dynamic inventory for ansible",
    long_description="dynamic inventory for ansible",
    author="Ivan Kozelskikh",
    author_email="johndemigod3318@gmail.com",
    url="https://github.com/Aded175/Libvirt-inventory",
    license="BSD 3-Clause License",
    scripts=["libvirt-inventory"],
    install_requires=["libvirt-python"],
)
