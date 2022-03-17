FROM python:3.8-buster

## https://github.com/OpenNMT/OpenNMT-py/blob/fc3409ce08785915728dac9e9c9fb49f73027917/tools/multi-bleu-detok.perl
RUN wget https://github.com/OpenNMT/OpenNMT-py/raw/fc3409ce08785915728dac9e9c9fb49f73027917/tools/multi-bleu-detok.perl

COPY fanid_dict.py .
