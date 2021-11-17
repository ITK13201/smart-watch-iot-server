import ast

import fitbit
from django.conf import settings


class FitbitApiClient:
    def __init__(self):
        self.client_id = settings.FITBIT_CLIENT_ID
        self.client_secret = settings.FITBIT_CLIENT_SECRET
        self.token_file_path = settings.FITBIT_TOKEN_FILE_PATH

        with open(self.token_file_path, "r") as f:
            tokens = f.read()
        token_dict = ast.literal_eval(tokens)
        self.access_token = token_dict["access_token"]
        self.refresh_token = token_dict["refresh_token"]

    def initial(self) -> fitbit.Fitbit:
        return fitbit.Fitbit(
            client_id=self.client_id,
            client_secret=self.client_secret,
            access_token=self.access_token,
            refresh_token=self.refresh_token,
            refresh_cb=self.update_token,
        )

    def update_token(self, token):
        with open(self.token_file_path, "w") as f:
            f.write(str(token))
