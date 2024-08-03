from enum import Enum
import contextlib


class StatusType(Enum):
    ALLOCATION_ERROR = 1
    INVALID_INPUT = 2
    FAILURE = 3
    SUCCESS = 4


class output_t:
    def __init__(self, status, x=0):
        self.status = status
        self.result = x


def run(command, *args):
    result = command(*args)
    print(command.__name__, end=": ")
    if isinstance(result, StatusType):
        print(result.name)

    elif isinstance(result, output_t):
        print(result.status.name, end="")
        if result.status == StatusType.SUCCESS:
            print(",", result.result)
        else:
            print("")


def run_file(input_file, output_file, ocean):
    with open(input_file, "r") as input_file:
        with open(output_file, "w") as output_file:
            with contextlib.redirect_stdout(output_file):
                for line in input_file:
                    command = line.strip().split(" ")
                    if command[0] == "":
                        continue
                    elif command[0] == "add_fleet" and len(command) == 2:
                        run(ocean.add_fleet, int(command[1]))
                    elif command[0] == "add_pirate" and len(command) == 3:
                        run(ocean.add_pirate, int(command[1]), int(command[2]))
                    elif command[0] == "num_ships_for_fleet" and len(command) == 2:
                        run(ocean.num_ships_for_fleet, int(command[1]))
                    elif command[0] == "pay_pirate" and len(command) == 3:
                        run(ocean.pay_pirate, int(command[1]), int(command[2]))
                    elif command[0] == "get_pirate_money" and len(command) == 2:
                        run(ocean.get_pirate_money, int(command[1]))
                    elif command[0] == "unite_fleets" and len(command) == 3:
                        run(ocean.unite_fleets, int(command[1]), int(command[2]))
                    elif command[0] == "pirate_argument" and len(command) == 3:
                        run(ocean.pirate_argument, int(command[1]), int(command[2]))
                    else:
                        print("Invalid command")
