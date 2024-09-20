from fastapi import HTTPException, status


class ResourcesExist(HTTPException):
    def __init__(self, message: str = "Resource with ID, Email, UUID doesn't exist"):
        super().__init__(status_code=status.HTTP_409_CONFLICT, detail=message)


class InvalidRequest(HTTPException):
    def __init__(self, message: str = "Invalid Request"):
        super().__init__(status_code=status.HTTP_403_FORBIDDEN, detail=message)
