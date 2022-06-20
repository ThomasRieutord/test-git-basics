#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""test-git-basics
===================

Intro to Git and Github for helpless colleagues ;)


Memo git commandes
------------------
Liste rapide des commandes:
  * `git clone`		Cloner le dépôt sur son ordinateur local
  * `git status`	Voir quels fichiers sont modifiés, suivis, « commités ».
  * `git add`		Ajouter des fichiers à suivre/partager
  * `git commit`	Valider des modifications
  * `git push`		Envoyer les modifications validées sur le serveur
  * `git pull`		Mettre à jour ses codes (récupérer ceux du serveur)
  * `git log`		Voir derniers commits
  * `git branch`	Voir les branches existantes
  * `git checkout`	Basculer sur une branche ou un commit


Ressources
----------
Cours en ligne Openclassroom : https://openclassrooms.com/fr/courses/7162856-gerez-du-code-avec-git-et-github
"""

import os

pckgname = "mypackage"
version = "0.0.1"
setupcontent = f"""import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="{pckgname}",
    version="{version}",
    author="",
    author_email="",
    description="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    classifiers=(
        "Environment :: Console"
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Development Status :: 2 - Pre-Alpha",
    ),
)
"""

dirs = [pckgname,"tests","examples","local","tmp"]

for dirname in dirs:
    os.mkdir(dirname)

with open(".gitignore","w") as f:
    f.write("*.pyc\n")
    f.write("*.egg-info/\n")
    f.write("*__pycache__/\n")
    f.write("tmp/\n")
    f.write("local/\n")

with open("README.md","w") as f:
    f.write(__doc__)

with open("setup.py","w") as f:
    f.write(setupcontent)

with open(os.path.join(pckgname,"__init__.py"), "w") as f:
    f.write(f"__version__='{version}'")

for dirname in dirs:
    with open(os.path.join(dirname,"dummy.txt"), "w") as f:
        f.write("dummy")

print(
    f"""Package {pckgname} initiated.
    Created repositories:
        {pckgname} -> contains only classes and functions of the package
        examples -> contains only executable programs using the package
        tests -> contains unitary tests
        tmp -> contains temporary files
        local -> contains local files, not meant be shared
    
    To install the package:
        `pip install -e .`
    """
)
