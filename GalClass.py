import re

class chooseindex(object):
	def __init__(self):
		self.return_index = None
		self.num = None
	def chooseBG(self):
		if self.num != None:
			pat = r'\[background=\'(.+?)\'\]'
			result = re.compile(pat,re.M)
			findall_result = result.findall(self.return_index[self.num])
			str_result = "".join(findall_result)
			return str_result
		else:
			pass
	def chooseText(self):
		if self.num != None:
			pat = r'\<(.+?)\>'
			result = re.compile(pat,re.M)
			findall_result = result.findall(self.return_index[self.num])
			str_result = "".join(findall_result)
			return str_result
		else:
			pass
	def chooseBGM(self):
		if self.num != None:
			pat = r'\[BGM = \'(.+?)\'\]'
			result = re.compile(pat,re.M)
			findall_result = result.findall(self.return_index[self.num])
			str_result = "".join(findall_result)
			return str_result
		else:
			pass
	def chooseButton(self):
		pat = r'(.+?)->(\d+)'
		result = re.compile(pat,re.M)
		findall_result = result.findall(self.return_index[self.num])
		if findall_result != []:
			t = []
			for i in (0,1):
				for a in (0,1):
					c = findall_result[i][a]
					t.append(str(c))
			a,b = t[0],t[2]
			c,d = t[1],t[3]
			return a,b,c,d
		else:
			return []


	def set(self,return_index=None,num=None):
		self.return_index = return_index
		self.num = num