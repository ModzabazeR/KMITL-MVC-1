def read(path):
	with open(path, 'r') as f:
		return f.read().splitlines()
	
def formatOutput(tokenTypes: list) -> str:
	return "\n".join([f"{token} is {tokenType}" for token, tokenType in tokenTypes])