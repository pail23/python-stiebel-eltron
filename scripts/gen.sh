#!/bin/sh

uv run scripts/generate.py
uvx ruff format pystiebeleltron
uvx ruff check --fix pystiebeleltron
