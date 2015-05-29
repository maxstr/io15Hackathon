# bootsmooth
# data.py module

import logging

# simple wrapper for simpljson

from django.utils import simplejson

def json_error(p_err):
	return simplejson.dumps({'error': p_err})

def json_success(p_err):
	return simplejson.dumps({'success': p_err})

def json_dump(p_obj):
	return simplejson.dumps(p_obj)
	

def fromEntity(ent):
	obj = {}
	for i in ent.keys():
		obj[i] = ent[i]
	return obj

# Convert dictionary to model object
def fromDict(obj, data):
	for name, value in data.iteritems():
		n = name
		try:
			# ignore key
			if n == "key":
				logging.warning('skipping key')
				continue
			if n == "_key":
				logging.warning('skipping key')
				continue
			if n[:1] == '_':
				n = n[1:]
		except:
			pass
		setattr(obj, n, value)

# Returns Dictionary of data
def toJSON(obj):
	try:
		objData = fromEntity(obj._entity)
		objData['key'] = str(obj.key())
		return json_dump(objData)
	except:
		return 0
			
# Returns Dictionary of data
def toDict(obj):
	try:
		objData = fromEntity(obj._entity)
		objData['key'] = str(obj.key())
		return objData
	except Exception as e:
		logging.warning('error: ' + str(e))
		return 0	

# Convert list of Objects to Dictionary 		
def listToDict(l):
	try:
		list = []
		for i in l:
			objData = fromEntity(i._entity)
			objData['key'] = str(i.key())
			list.append(objData)
		return list
	except:
		return 0
	
# Convert list of Objects to JSON
def listToJSON(l):
	try:
		list = []
		for i in l:
			objData = fromEntity(i._entity)
			objData['key'] = str(i.key())
			list.append(objData)
		return json_dump(list)
	except:
		return 0
	
	