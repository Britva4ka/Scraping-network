from functools import wraps


def social_login_required(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        # Check if user is already logged in
        if self.is_registered:
            if self.is_logged_in:
                return func(self, *args, **kwargs)
            self.social_network_login()
            return func(self, *args, **kwargs)
        self.social_network_register()
        # If not logged in, perform social login
        self.social_network_login()

        # Call the original function
        return func(self, *args, **kwargs)
    return wrapper
