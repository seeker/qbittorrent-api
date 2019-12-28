#!/bin/sh

coverage run --branch -m unittest
coverage report --omit='/**/.virtualenvs/**/'
coverage html --omit='/**/.virtualenvs/**/'

