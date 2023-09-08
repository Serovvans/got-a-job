class ParsingError(Exception):
    """Ошибка прарсинга"""
    def __init__(self, message):
        super().__init__(message)
