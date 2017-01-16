# coding=utf-8
import setuptools

def package_data_dirs(source, sub_folders):
	import os
	dirs = []

	for d in sub_folders:
		for dirname, _, files in os.walk(os.path.join(source, d)):
			dirname = os.path.relpath(dirname, source)
			for f in files:
				dirs.append(os.path.join(dirname, f))

	return dirs

def params():
	name = "OctoPrint-Slic3r"
	version = "0.2"

	description = "Adds support for slicing via Slic3r from within OctoPrint"
	author = "Eyal Soha"
	author_email = "eyal0@github.com"
	url = "http://github.com/eyal0/OctoPrint-Slic3r"
	license = "AGPLv3"

	packages = ["octoprint_slic3r"]
	package_data = {"octoprint_slic3r": package_data_dirs('octoprint_slic3r', ['static', 'templates', 'profiles'])}

	include_package_data = True
	zip_safe = False
	install_requires = open("requirements.txt").read().split("\n")

	entry_points = {
		"octoprint.plugin": [
			"slic3r = octoprint_slic3r"
		]
	}

	return locals()

setuptools.setup(**params())
