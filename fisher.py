# -*- coding: UTF-8 -*-

# Description: 入口文件
#      Author: Mario
#    Datetime: 2019-09-22 12:34
from app import create_app

app = create_app()
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=app.config['DEBUG'])
