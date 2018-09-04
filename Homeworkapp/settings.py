


class Config:
    DEBUG = True
    Testing = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True


def get_databases_uri(dbinfo):
    host = dbinfo.get("HOST") or "localhost"
    port = dbinfo.get("PORT") or "3306"
    user = dbinfo.get("USER") or "root"
    password = dbinfo.get("PASSWORD") or "123456"
    db = dbinfo.get("DB") or "mydb"
    type = dbinfo.get("TYPE") or "mysql"
    driver = dbinfo.get("DRIVER") or "pymysql"
    encoding = dbinfo.get("ENCODING") or "utf8"
    return '{}+{}://{}:{}@{}:{}/{}?charset={}'.format(type, driver, user, password, host, port, db, encoding)


class DevolopConfig(Config):
    Testing = False
    
    DATABASES = {
        "HOST": "localhost",
        "PORT": "3306",
        "USER": "root",
        "PASSWORD": "1111",
        "DB": "mydb",
        "DRIVER": "pymysql",
        "TYPE": "mysql",
        "ENCODING": "utf8",
    }
    SQLALCHEM_DATABASE_URI = get_databases_uri(DATABASES)