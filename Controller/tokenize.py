def isComment(text: str) -> bool:
    return text.startswith("//")

def tokenize(text: str) -> list:
    return text.split(" ")

def type_classify(tokens: list, keywordType: int) -> list:
    if keywordType == 1:
        import Model.keywordType1 as KeywordType
    elif keywordType == 2:
        import Model.keywordType2 as KeywordType
    tokenTypes = []
    for token in tokens:
        tokenTypes.append((token, KeywordType.tokenType(token)))
    return tokenTypes