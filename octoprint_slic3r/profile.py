# coding=utf-8
from __future__ import absolute_import

__author__ = "Gina Häußge <osd@foosel.net>"
__license__ = 'GNU Affero General Public License http://www.gnu.org/licenses/agpl.html'
__copyright__ = "Copyright (C) 2014 The OctoPrint Project - Released under terms of the AGPLv3 License"

import logging
import re

class GcodeFlavors(object):
	REPRAP = "reprap"
	TEACUP = "teacup"
	MAKERWARE = "makerware"
	SAILFISH = "sailfish"
	MACH3 = "mach3"
	NO_EXTRUSION = "no-extrusion"

class FillPatterns(object):
	ARCHIMEDEANCHORDS = "archimedeanchords"
	RECTILINEAR = "rectilinear"
	FLOWSNAKE = "flowsnake"
	OCTAGRAMSPIRAL = "octagramspiral"
	HILBERTCURVE = "hilbertcurve"
	LINE = "line"
	CONCENTRIC = "concentric"
	HONEYCOMB = "honeycomb"
	HONEYCOMB_3D = "3dhoneycomb"

class SupportPatterns(object):
	HONEYCOMB = "honeycomb"
	RECTILINEAR = "rectilinear"
	RECTILINEAR_GRID = "rectilinear-grid"

class SeamPositions(object):
	RANDOM = "random"
	ALIGNED = "aligned"
	NEAREST = "nearest"

class Profile(object):

	regex_strip_comments = re.compile(";.*$", flags=re.MULTILINE)

	@classmethod
	def from_slic3r_ini(cls, path):
		import os
		if not os.path.exists(path) or not os.path.isfile(path):
			return None

		result = dict()
		display_name = None
		description = None
		with open(path) as f:
			for line in f:
				if "#" in line:
					if line.startswith("# Name: "):
						display_name = line[len("# Name: "):]
					elif line.startswith("# Description: "):
						description = line[len("# Description: "):]
					line = line[0:line.find("#")]
				split_line = line.split("=", 1)
				if len(split_line) != 2:
					continue
				key, v = map(str.strip, split_line)
				result[key] = cls.convert_value(key, v, None)

		# merge it with our default settings, the imported profile settings taking precedence
		return cls.merge_profile(result), display_name, description

	@classmethod
	def to_slic3r_ini(cls, profile, path, display_name=None, description=None):
		with open(path, "w") as f:
			if display_name is not None:
				f.write("# Name: " + display_name + "\n")
			if description is not None:
				f.write("# Description: " + description + "\n")
			for key in sorted(profile.keys()):
				if key.startswith("_"):
					continue

				value = profile[key]
				f.write(key + " = " + str(value) + "\n")

	@classmethod
	def convert_value(cls, key, value, default, sep=","):
		try:
                        if default is None:
                                try:
                                        return int(value)
                                except ValueError:
                                        pass
                                try:
                                        return float(value)
                                except ValueError:
                                        pass
                                return str(value)
		except:
			logging.getLogger("plugins.slic3r." + __name__).exception("Got an exception while trying to convert the value for %s from an imported profile, using default" % key)
			return default

	@classmethod
	def merge_profile(cls, profile, overrides=None):
		import copy

		result = {}
		for k in profile.keys():
			override_value = None
			profile_value = profile[k]
			if overrides and k in overrides:
				override_value = overrides[k]

			# just change the result value to the override_value if available, otherwise to the profile_value if
			# that is given, else just leave as is
			if override_value is not None:
				result[k] = override_value
			elif profile_value is not None:
				result[k] = profile_value
		return result

	def __init__(self, profile, printer_profile, posX, posY, overrides=None):
		self._profile = profile
		self._printer_profile = printer_profile
		self._pos_x = posX
		self._pos_y = posY
		self._overrides = overrides

	def get(self, key):
          if key in self._profile:
            return self._profile[key]
          else:
            return None

	def convert_to_engine(self):
		settings = dict()

		for key in self._profile:
			value = self.get(key)
			if value is None:
				continue

			if isinstance(value, bool):
				if not value:
					continue
				value = None
			elif isinstance(value, (tuple, list)):
				value = ",".join(map(str, value))

			settings[key.replace("_", "-")] = value

		return settings
