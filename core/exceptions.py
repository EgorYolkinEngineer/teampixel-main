class TokenException(Exception):
    pass


class ValidationError(Exception):
    pass


class DBError(Exception):
    pass


class AlreadyExistError(DBError):
    pass


class MultipleRowsFoundError(DBError):
    pass


class NoRowsFoundError(DBError):
    pass
