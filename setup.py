

# from setuptools import find_packages
from setuptools import setup


setup(
  author="GaelicGrime",
  author_email="will.angus.blaylock@gmail.com",
  license="GPLv3",
  name="SDLMasher",
  url="https://github.com/ComfortableSoftware/SDLMasher",
  version="0.1.0",
  package_dir={"SDLMasher": "SDLMasher"},
  package_data={
      "SDLMasher": [
          "../doc/*",
      ]
  },
  packages=["SDLMasher"],
  install_requires=[
      "CF",
      "PySimpleGUI",
  ],
  extras_require={
  },
#  scripts=["scripts/SDLMasher"],
)
