=========
Piggel.in
=========

| Author: Daniel Jonsson

Setup
=====

::

    pyvenv env
    source env/bin/activate
    pip install -r requirements.txt

Update gh-pages
===============

::

    make publish
    ghp-import output
    git push origin gh-pages

