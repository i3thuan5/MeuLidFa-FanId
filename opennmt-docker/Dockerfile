FROM pytorch/pytorch:1.9.0-cuda11.1-cudnn8-runtime
#RUN pip install OpenNMT-py==2.1.2
RUN pip install https://github.com/OpenNMT/OpenNMT-py/archive/refs/heads/master.zip # torch >= 1.6.0

WORKDIR /fanid
COPY tin.yaml .
