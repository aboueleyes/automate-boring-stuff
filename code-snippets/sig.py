#!/usr/bin/env python3 

from signal import signal, SIGINT
from tqdm import trange
import time 

def handler(signum, time):
  print('\n signal detected. not stopping')

signal(SIGINT,handler)
for _ in trange(10000):
  time.sleep(0.001)