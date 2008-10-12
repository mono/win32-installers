import os
import uuid
import re
from os.path import join, basename, split
from optparse import OptionParser
from xml.dom import minidom
from sets import Set

parser = OptionParser(usage='usage: %prog [options] SOURCE_DIR')
parser.add_option("-g", dest="gen_guid",
		  help="generate guids for component objects")

(options, args) = parser.parse_args()

if len(args) != 1:
	parser.error ('incorrect number of arguments')

source_dir = args[0]

unique_ids = {}

def sanitizeId(id):
	# For some reason, we get ICE30 validation errors if we have Ids longer
	# than about 30 characters.  This seems to have nothing to do with the
	# MSI s? column limit that the validation error describes (255
	# characters including the 36 character GUID).
	if len(id) > 30:
		id = id[0:30]

	# Ids can't start with a number
	if re.match('^\d(.*)$', id):
		id = "_" + id

	# Only alphanumerics and underscores (periods are allowed, but not in
	# Module Ids, so we drop them)
	id = re.sub('[^\d\w_]', '_', id)
	
	# Ids must be unique
	if not unique_ids.has_key(id):
		unique_ids[id] = 1
		return id

	num = unique_ids[id]
	new_id = id + "_" + str(num)
	unique_ids[id] = num + 1

	return new_id
		

def generateGuid():
	return str(uuid.uuid1())

doc = minidom.Document()

wix = doc.createElement("Wix")
wix.setAttribute("xmlns", "http://schemas.microsoft.com/wix/2006/wi")
doc.appendChild(wix)

mod = doc.createElement("Module")
mod.setAttribute("Id", "ID-NAME-HERE")
mod.setAttribute("Language", "1033")
mod.setAttribute("Version", "VERSION-HERE")
wix.appendChild(mod)

pkg = doc.createElement("Package")
pkg.setAttribute("Id", generateGuid())
pkg.setAttribute("Manufacturer", "MANUFACTURER-HERE")
pkg.setAttribute("InstallerVersion", "200")
mod.appendChild(pkg)

tar = doc.createElement("Directory")
tar.setAttribute("Id", "TARGETDIR")
tar.setAttribute("Name", "SourceDir")
mod.appendChild(tar)

top = doc.createElement("Directory")
top.setAttribute("Id", "MergeRedirectFolder")
tar.appendChild(top)

parent_dirs = {}

for root, dirs, files in os.walk(source_dir):
	if root == source_dir:
		continue

	parent = top

	(head, tail) = split(root)
	if parent_dirs.has_key(head):
		parent = parent_dirs[head]

	elm = doc.createElement("Directory")
	elm.setAttribute("Id", sanitizeId(basename(root)))
	elm.setAttribute("Name", basename(root))
	parent.appendChild(elm)

	parent_dirs[root] = elm
	
	if len(files) > 0:
		cmp = doc.createElement("Component")
		cmp.setAttribute("Id", sanitizeId(basename(root) + "_component"))
		cmp.setAttribute("Guid", generateGuid())
		elm.appendChild (cmp)

	for file in files:
		chi = doc.createElement("File")
		chi.setAttribute("Id", sanitizeId(file))
		chi.setAttribute("Name", file)
		chi.setAttribute("Source", join(root, file))
		chi.setAttribute("Vital", "yes")
		cmp.appendChild(chi)

print doc.toprettyxml('  ')

