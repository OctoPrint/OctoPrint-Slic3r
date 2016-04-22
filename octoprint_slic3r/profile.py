# coding=utf-8
from __future__ import absolute_import

__author__ = "Gina Häußge <osd@foosel.net>, Javier Martínez Arrieta <martinezarrietajavier@gmail.com>"
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

defaults = dict(
    nozzle_diameter = 0.5,
    print_center = (100, 100), # TODO
    z_offset = 0,
    gcode_flavor = GcodeFlavors.REPRAP,
    use_relative_e_distances = 0, 			# 0 (unchecked) or 1 (checked)
    use_firmware_retraction = 0, 			# 0 (unchecked) or 1 (checked)
    gcode_arcs = 0, 					# 0 (unchecked) or 1 (checked)
    gcode_comments = 0, 				# 0 (unchecked) or 1 (checked)
    vibration_limit = 0,

    filament_diameter = 3,
    extrusion_multiplier = 1,
    temperature = 200,
    first_layer_temperature = 200,
    bed_temperature = 0,

    travel_speed = 130,
    perimeter_speed = 30,
    small_perimeter_speed = 30,
    external_perimeter_speed = "70%",
    infill_speed = 60,
    solid_infill_speed = 60,
    top_solid_infill_speed = 50,
    support_material_speed = 60,
    support_material_interface_speed = "100%",
    bridge_speed = 60,
    gap_fill_speed = 20,
    first_layer_speed = "30%",

    perimeter_acceleration = 0,
    infill_acceleration = 0,
    bridge_acceleration = 0,
    first_layer_acceleration = 0,
    default_acceleration = 0,

    layer_height = 0.3,
    first_layer_height = 0.35,
    infill_every_layers = 1,
    solid_infill_every_layers = 0,

    perimeters = 3,
    top_solid_layers = 3,
    bottom_solid_layers = 3,
    fill_density = "40%",
    fill_angle = 45,
    fill_pattern = FillPatterns.HONEYCOMB,
    start_gcode = None,
    end_gcode = None,
    layer_gcode = None,
    toolchange_gcode = None,
    seam_position = SeamPositions.ALIGNED,
    external_perimeters_first = 0, 			# 0 (unchecked) or 1 (checked)
    spiral_vase = 0, 					# 0 (unchecked) or 1 (checked)
    only_retract_when_crossing_perimeters = 0,		# 0 (unchecked) or 1 (checked)
    solid_infill_below_area = 70,
    infill_only_where_needed = 0, 			# 0 (unchecked) or 1 (checked)
    infill_first = 0, 					# 0 (unchecked) or 1 (checked)

    extra_perimeters = 1, 				# 0 (unchecked) or 1 (checked)
    avoid_crossing_perimeters = 0, 			# 0 (unchecked) or 1 (checked)
    thin_walls = 1, 					# 0 (unchecked) or 1 (checked)
    overhangs = 0,

    support_material = 0, 				# 0 (unchecked) or 1 (checked)
    support_material_threshold = 0,
    support_material_pattern = SupportPatterns.HONEYCOMB,
    support_material_spacing = 2.5,
    support_material_angle = 0,
    support_material_interface_layers = 3,
    support_material_interface_spacing = 0,
    raft_layers = 0,
    support_material_enforce_layers = 0,
    dont_support_bridges = 0, 				# 0 (unchecked) or 1 (checked)

    retract_length = 1,
    retract_speed = 30,
    retract_restart_extra = 0,
    retract_before_travel = 2,
    retract_lift = 0,
    retract_layer_change = 1,
    wipe = 0,

    retract_length_toolchange = 1,
    retract_restart_extra_toolchange = 1,

    cooling = 0, 					# 0 (unchecked) or 1 (checked)
    min_fan_speed = "35",
    max_fan_speed = "100",
    bridge_fan_speed = "100",
    fan_below_layer_time = 60,
    slowdown_below_layer_time = 30,
    min_print_speed = 10,
    disable_fan_first_layers = 1,
    fan_always_on = 0,					# 0 (unchecked) or 1 (checked)

    skirts = 1,
    skirt_distance = 6,
    skirt_height = 1,
    min_skirt_length = 0,
    brim_width = 0,

    duplicate_distance = 6,
    xy_size_compensation = 0,

    complete_objects = 0,
    extruder_clearance_radius = 20,
    extruder_clearance_height = 20,

    notes = "",
    resolution = 0,

    extrusion_width = "100%",
    first_layer_extrusion_width = "100%",
    perimeter_extrusion_width = "100%",
    external_perimeter_extrusion_width = "100%",
    infill_extrusion_width = "100%",
    solid_infill_extrusion_width = "100%",
    top_infill_extrusion_width = "100%",
    support_material_extrusion_width = "100%",
    bridge_flow_ratio = 1,

    extruder_offset = "0x0",
    perimeter_extruder = 1,
    infill_extruder = 1,
    support_material_extruder = 1,
    support_material_interface_extruder = 1,
    ooze_prevention = 0, 				# 0 (unchecked) or 1 (checked)
    standby_temperature_delta = -5,

    #Parameters that weren't in the list that have been added
    extrusion_axis = "E",
    bed_shape = "0x0,100x0,100x100,0x100",
    bed_size = (200,200),
    before_layer_gcode = None,
    external_fill_pattern = FillPatterns.RECTILINEAR,
    filament_colour = "#FFFFFF",
    infill_overlap = "15%",
    max_print_speed = 80,
    max_volumetric_speed = 0,
    pressure_advance = 0,
    solid_infill_extruder = 1,
    support_material_contact_distance = 0.2,
    use_volumetric_e = 0,  				# 0 (unchecked) or 1 (checked)
    threads = 2,
    first_layer_bed_temperature = 90,
    interface_shells = 0, 				# 0 (unchecked) or 1 (checked)
    post_processing = None,
    solid_fill_pattern = FillPatterns.RECTILINEAR,
    g0 = 0,						# 0 (unchecked) or 1 (checked)
    duplicate = 1,
    duplicate_grid = (1,1),
    randomize_start = 0,				# 0 (unchecked) or 1 (checked)
    rotate = 0,
    scale = 1,
    start_perimeters_at_concave_points = 0,		# 0 (unchecked) or 1 (checked)
    start_perimeters_at_non_overhang = 0		# 0 (unchecked) or 1 (checked)
)


float_or_int_or_percentage = (
    "small_perimeter_speed", "external_perimeter_speed", "solid_infill_speed", "top_solid_infill_speed", "support_material_interface_speed",
    "first_layer_speed", "first_layer_height", "extrusion_width", "first_layer_extrusion_width", "external_perimeter_extrusion_width",
    "perimeter_extrusion_width", "infill_extrusion_width", "solid_infill_extrusion_width", "top_infill_extrusion_width",
    "support_material_extrusion_width", "infill_overlap"
)


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

				if not key in defaults.keys():
					# unknown profile settings, we'll ignore that
					continue

				result[key] = cls.convert_value(key, v, defaults[key])

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
				if isinstance(value, bool):
					value = "true" if value else "false"
				elif isinstance(value, (tuple, list)):
					value = ",".join(map(str, value))
				f.write(key + " = " + str(value) + "\n")

	@classmethod
	def convert_value(cls, key, value, default, sep=","):
		try:
			'''Some defaults can be instances of int whereas its values are instances of float. 
			If that happens, change default to float so as to override default value without getting errors'''
			if isinstance(default,int) and value.count('.')==1:
				default=float(default)

			if key in float_or_int_or_percentage:
				if value.endswith("%"):
					return str(value)
				elif value.count('.')==1:
					return float(value)
				else:
					return int(value)
			elif isinstance(default, bool):
				return bool(value)
			elif isinstance(default, int):
				return int(value)
			elif isinstance(default, float):
				return float(value)
			elif isinstance(default, (list, tuple)):
				result = []

				parts = value.split(sep)
				if len(parts) > len(default):
					parts = parts[:len(default)]

				for i, d in enumerate(default):
					if i >= len(parts):
						result.append(d)
					else:
						result.append(cls.convert_value(key, parts[i], d))

				return result
			else:
				return str(value)
		except:
			logging.getLogger("plugins.slic3r." + __name__).exception("Got an exception while trying to convert the value for %s from an imported profile, using default" % key)
			return default

	@classmethod
	def merge_profile(cls, profile, overrides=None):
		import copy

		result = copy.deepcopy(defaults)
		for k in result.keys():
			profile_value = None
			override_value = None

			if k in profile:
				profile_value = profile[k]
			if overrides and k in overrides:
				override_value = overrides[k]

			if profile_value is None and override_value is None:
				# neither override nor profile, no need to handle this key further
				continue

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
			elif key in defaults:
				return defaults[key]
			else:
				return None

	def convert_to_engine(self):
		settings = dict()

		for key in defaults:
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
