import time
import json
import os
from models.system import System


def main():
    # Reads the config JSON
    config_file = os.getenv("CONFIG_FILE")
    json_file = open(config_file)
    config_dict = json.load(json_file)
    json_file.close()
    # Runs the program
    s = System.from_json(config_dict)
    s.single_pl_dispatch()
    # s.setup_post_study()
    # s.pddd_dispatch(0)


if __name__ == "__main__":
    ti = time.time()
    main()
    tf = time.time()
    print("Tempo de execução: {}".format(tf - ti))
