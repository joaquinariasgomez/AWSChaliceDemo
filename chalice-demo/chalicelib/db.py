import logging
import boto3

logger = logging.getLogger("chalice-demo")

_DB = None
TABLE_NAME = "chalice-demo-table-dev"


def get_app_db():
    global _DB

    if _DB is None:
        _DB = UserSignupDB(
            table=boto3.resource("dynamodb").Table(TABLE_NAME), logger=logger
        )

    return _DB


class UserSignupDB:
    def __init__(self, table, logger):
        self._table = table
        self._logger = logger

    def user_signup(self, user_dict):
        try:
            self._table.put_item(
                Item={
                    "first_name": user_dict.get("first_name"),
                    "age": user_dict.get("age"),
                    "email": user_dict.get("email")
                }
            )
            self._logger.debug(
                f"Inserted user '{user_dict.get('first_name')}' into DynamoDB table '{self._table}'"
            )

            return True

        except Exception as exc:
            self._logger.exception(exc)
