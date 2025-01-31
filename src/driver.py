import os
import sys
import time
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.action import demo  # nopep8


def run_action(clk, cycle):
    action = demo.Demo(clk)
    while True:
        start = time.time()
        action.execute()

        time.sleep(max(0.0, cycle - (time.time() - start)))


def run_clock(clk, cycle):
    while True:
        start = time.time()
        clk.execute()

        time.sleep(max(0.0, cycle - (time.time() - start)))
