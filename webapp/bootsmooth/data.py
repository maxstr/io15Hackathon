# bootsmooth
# data.py module

import simplejson

def json_error(p_message, p_state_code=400):
	return simplejson.dumps({'error': p_err, 'status_code': p_status_code})

def json_success(p_message):
	return simplejson.dumps({'success': p_err, 'status_code': 200})

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
			# ignore key and '_' properties
			if n == "key":
				continue
			if n == "_key":
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
	
	