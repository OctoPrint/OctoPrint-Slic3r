# coding=utf-8
from __future__ import absolute_import

__author__ = "Javier Martínez Arrieta <martinezarrietajavier@gmail.com>, Eyal Soha <eyalsoha@gmail.com>"
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
        split_line = line.split("=", 1)
        if len(split_line) != 2:
          continue
        key, v = map(str.strip, split_line)
        # Only strip the comment if it's really a comment.
        # Sometimes the parameter's value includes a #,
        # for example, color.
        if "#" in v and str.strip(v[0:v.find("#")]):
          v = str.strip(v[0:v.find("#")])

        result[key] = v

    return result, display_name, description

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
        if isinstance(value, bool):
          value = "true" if value else "false"
        elif isinstance(value, (tuple, list)):
          value = ",".join(map(str, value))
        f.write(key + " = " + str(value) + "\n")

  def __init__(self, profile, printer_profile, posX, posY, overrides=None):
    self._profile = profile
    self._printer_profile = printer_profile
    self._pos_x = posX
    self._pos_y = posY
    self._overrides = overrides

  def get(self, key):
    if key == "print_center":
      width = self._printer_profile["volume"]["width"]
      depth = self._printer_profile["volume"]["depth"]
      circular = self._printer_profile["volume"]["formFactor"] == "circular"

      if self._pos_x:
        x = self._pos_x
      else:
        x = width / 2.0 if not circular else 0.0
      if self._pos_y:
        y = self._pos_y
      else:
        y = depth / 2.0 if not circular else 0.0

      return x, y

    elif key == "nozzle_diameter":
      return self._printer_profile["extruder"]["nozzleDiameter"]

    else:
      if key in self._profile:
        return self._profile[key]
      else:
        return None
