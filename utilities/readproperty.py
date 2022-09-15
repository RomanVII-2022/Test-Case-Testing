import configparser


config = configparser.RawConfigParser()
config.read("C:\\highbridselenium\\ecommerceApp\\configurations\\config.ini")


class ReadConfig:
    @staticmethod
    def get_app_url():
        url = config.get('common info', 'base_url')
        return url


    @staticmethod
    def get_user_email():
        user_email = config.get('common info', 'email')
        return user_email


    @staticmethod
    def get_user_password():
        user_password = config.get('common info', 'password')
        return user_password