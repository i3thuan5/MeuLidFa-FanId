FROM pytorch/pytorch:1.9.0-cuda11.1-cudnn8-runtime
#RUN pip install OpenNMT-py==2.1.2
RUN pip install https://github.com/OpenNMT/OpenNMT-py/archive/refs/heads/master.zip # torch >= 1.6.0
RUN pip install flask


WORKDIR /onmt
COPY tin.yaml ./

ENV IP="0.0.0.0"
ENV PORT=5000
ENV URL_ROOT="/"
ENV CONFIG="./tin.json"

# Kah ENV PORT sio-kâng
EXPOSE 5000 

CMD server.py --ip $IP --port $PORT --url_root $URL_ROOT --config $CONFIG
