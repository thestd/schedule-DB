from tornado.options import options, define, parse_config_file
import os


def load_conf(config_file=None):
    if config_file:
        parse_config_file(config_file)
    define("db_name", default="pnu_schedule", help="Database name")
    define("db_user", default="user", help="Database user")
    define("db_password", default="password", help="Database password")
    define("db_host", default="localhost", help="Database host")
    define("db_port", default="27017", help="Database port")
    define("app_port", default="8086", help="Application port")
    define("secret", default="ABCDEFG!@#$%#", help="Secret key")
    define("auth_token", default=os.getenv("AUTH_KEY", "123456"), help="Secret key")

    db_uri = "mongodb://{}:{}@{}:{}/".format(options.db_user, options.db_password,
                                             options.db_host, options.db_port)

    define("db_uri", default=db_uri)
