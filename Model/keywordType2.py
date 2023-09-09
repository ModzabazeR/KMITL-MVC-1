typesName = ["Keyword and Sign", "Assignment", "Integer", "Variable"]

types = {
	"Keyword and Sign": ["declare", "+"],
	"Assignment": ["="]
}

def isKeywordAndSign(token: str) -> bool:
	return token in types["Keyword and Sign"]

def isAssignment(token: str) -> bool:
	return token in types["Assignment"]

def isInteger(token: str) -> bool:
	return token.isdigit()

def tokenType(token: str) -> str:
	if isKeywordAndSign(token):
		return typesName[0]
	elif isAssignment(token):
		return typesName[1]
	elif isInteger(token):
		return typesName[2]
	else:
		return typesName[3]