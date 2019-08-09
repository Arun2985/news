import os
SECRET_KEY = '\xf5]0|\xd6\xc7Z\xf3D6\xe8\xe1\xf8\xfd\xfb\xd8/\xf6\xd1R\xddgO\xee'
SQLALCHEMY_DATABASE_URI =  'mysql+pymysql://root:root@localhost/spingig'
basedir = os.path.abspath(os.path.dirname(__file__))
UPLOADED_PHOTOS_DEST = os.path.join(basedir, 'photos')