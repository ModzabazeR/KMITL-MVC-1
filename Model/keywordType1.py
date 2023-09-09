typesName = ["Keyword", "Symbol", "Literal", "Identifier"]

types = {
	"Keyword": ["declare"],
	"Symbol": ["+", "="]
}

def isKeyword(token: str) -> bool:
	return token in types["Keyword"]

def isSymbol(token: str) -> bool:
	return token in types["Symbol"]

def isLiteral(token: str) -> bool:
	return token.isdigit()

def tokenType(token: str) -> str:
	if isKeyword(token):
		return typesName[0]
	elif isSymbol(token):
		return typesName[1]
	elif isLiteral(token):
		return typesName[2]
	else:
		return typesName[3]