class Extractor():
    def __init__(self,
    cookie_name,
    cookie_id,
    cookie_value,
    cookie_expiration_date,
    cookie_domain,
    cookie_secure_flag,
    cookie_http_only_flag):

        self.cookie_id = cookie_id
        self.cookie_value =cookie_value
        self.cookie_expiration_date = cookie_expiration_date
        self.cookie_domain = cookie_domain
        self.cookie_secure_flag =cookie_secure_flag
        self.cookie_http_only_flag =cookie_http_only_flag
        self.cookie_name = cookie_name