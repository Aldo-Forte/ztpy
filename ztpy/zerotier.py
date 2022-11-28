class ZeroTier:    

    __token = "";

    @staticmethod
    def set_token(token:str):
        ZeroTier.__token = token

    @staticmethod
    def get_token() -> str:
        return ZeroTier.__token
