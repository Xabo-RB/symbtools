

[![PyPI Package Link](https://badge.fury.io/py/symbtools.svg "PyPI Package Link")](https://badge.fury.io/py/symbtools)
[![Build Status](https://cloud.drone.io/api/badges/TUD-RST/symbtools/status.svg?ref=refs/heads/main)](https://cloud.drone.io/TUD-RST/symbtools) [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.275073.svg)](https://doi.org/10.5281/zenodo.275073)
<!-- currently travis does not work -->
<!-- [![Travis CI Unit Test Result badge](https://travis-ci.org/TUD-RST/symbtools.svg?branch=master "Travis CI Unit Test Result badge")](https://travis-ci.org/TUD-RST/symbtools) --> 


(English version below)

Allgemeines
===========
Das Paket `symbtools` enthält eine Sammlung von Funktionen für
symbolischen Rechnungen, die bei der Untersuchung nichtlineare dynamischer
Systeme im Rahmen der Regelungs- und Steuerungstheorie auftreten.

Speziell ist im Modul `modeltools` Funktionalität gebündelt, die zur Herleitung,
Analyse und Numerischen Lösung (Simulation) von Bewegungsgleichungen mechanischer Systeme mit
und ohne algebraische Nebenbedingungen mit Hilfe der Lagrange-Gleichungen 1. bzw. 2. Art dient.

Eine klassische Dokumentation des Paketes ist in Vorbereitung. Vorerst wird auf die, die
[Demo-Notebooks](https://nbviewer.jupyter.org/github/TUD-RST/symbtools/tree/master/docs/demo_notebooks/),
auf die [Unit-Tests](https://github.com/TUD-RST/symbtools/blob/master/symbtools/test/test_modeltools.py)
und auf die Docstrings im Quellcode verwiesen.
Für Fragen und Anregungen stehen die Github-Issue-Funktion sowie der [Paketbereuer](https://tu-dresden.de/ing/elektrotechnik/rst/das-institut/beschaeftigte/carsten-knoll)
per Mail zur Verfügung.


Der Programmcode hat insgesamt den Status von "Forschungscode",
d.h. das Paket befindet sich nach wie vor in Entwicklung.
Obwohl wesentliche Teile durch Unit-Tests abgedeckt sind, enthält der Code
mit einer gewissen Wahrscheinlichkeit Fehler.


General Information
===================
The package symbtools contains collection of functions for symbolic
calculations, which occur along with the investigation of nonlinear
dynamical systems in the field of control theory.

Especially the module `modeltools` contains functionality wich serves for generating, analizing
and simulating the equations of motion of mechanical systems based on the Lagrange-Equations of
1st and 2nd kind.

Classical docs for this package are still in preparation. Meanwhile we refer to the
[Demo Notebooks](https://nbviewer.jupyter.org/github/TUD-RST/symbtools/tree/master/docs/demo_notebooks/),
to the [unit tests](https://github.com/TUD-RST/symbtools/blob/master/symbtools/test/test_modeltools.py)
and finally to the docstrings im in the sources. If you have any question feel, free to open an
issue or to email the [maintainer](https://tu-dresden.de/ing/elektrotechnik/rst/das-institut/beschaeftigte/carsten-knoll).

Note that the package is in development state. Despite that a substantial
part is covered by unit test, the code will contain bugs with some probability.


Installation
============
Make sure you have the following dependencies installed (see also requirements.txt):

- sympy
- numpy
- scipy
- ipython
- ipydex
- matplotlib (for visualization)

Get symbtools using PyPI::

    $ pip install symbtools

or the latest git version::

    $ git clone https://github.com/TUD-RST/symbtools.git

Página donde lo encontré:
https://groups.google.com/g/sympy/c/eWcKd1j3RdA/m/5muBTmkUCgAJ?pli=1

Guías:
https://nbviewer.org/github/TUD-RST/symbtools/tree/master/docs/demo_notebooks/

Software online:
https://zenodo.org/record/275073#.YhvLl-jMJPY
https://bitbucket.org/cvk/pycontroltools/src/master/

https://pypi.org/project/symbtools/#files

Línea donde se calcula el rango:
https://github.com/Xabo-RB/symbtools/blob/main/symbtools/core.py#L3224

https://github.com/cknoll/rst_symbtools/blob/7a2a4dc9eec617d41f9db3591931615272a80af9/symb_tools.py#L2636

En sympy: 
https://github.com/sympy/sympy/blob/00d6469eafdd4aac346a0b598184c15f2560dbe5/sympy/matrices/reductions.py#L178
