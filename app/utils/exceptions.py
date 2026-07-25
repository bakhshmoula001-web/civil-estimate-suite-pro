class ValidationError(Exception):
    """Raised when validation fails."""
    pass

class DatabaseError(Exception):
    """Raised when a database operation fails."""
    pass
