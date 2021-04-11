import os.path as osp
from setuptools import setup, find_packages


# read the contents of your README file
rep_folder = osp.abspath(osp.dirname(__file__))
with open(osp.join(rep_folder, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="deep_hedge_rl",
    version="0.0.1",
    url="https://github.com/RoetGer/deep-hedge-rl",
    packages=find_packages(include=["deep_hedge_rl"]),
    long_description=long_description, 
    long_description_content_type="text/markdown"
)