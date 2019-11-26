FROM python:3.7
WORKDIR /Projects/fisher

COPY package.txt ./
RUN pip install -r package.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

COPY . .

CMD ["gunicorn", "fisher:app", "-c", "./gunicorn.conf.py"]