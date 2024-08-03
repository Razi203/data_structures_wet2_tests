from util import StatusType, output_t, run_file


class Fleet:
    def __init__(self, id):
        self.ship_count = 1
        self.id = id
        self.pirates = []
        self.live = True

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    def add_pirate(self, pirate):
        self.pirates.append(pirate)
        pirate.fleetId = self.id
        pirate.rank = len(self.pirates)
        return StatusType.SUCCESS


class Pirate:
    def __init__(self, id):
        self.id = id
        self.money = 0
        self.fleetId = 0
        self.rank = 0

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def money(self):
        return self._money

    @money.setter
    def money(self, value):
        self._money = value

    @property
    def rank(self):
        return self._rank

    @rank.setter
    def rank(self, value):
        self._rank = value


def find_pirate(pirates, id):
    for pirate in pirates:
        if pirate.id == id:
            return pirate
    return StatusType.FAILURE


def find_fleet(fleets, id):
    for fleet in fleets:
        if fleet.id == id:
            return fleet
    return StatusType.FAILURE


def find_pirate_in_ocean(ocean, id):
    if id not in ocean.pirate_ids:
        return StatusType.FAILURE
    for fleet in ocean.fleets:
        for pirate in fleet.pirates:
            if pirate.id == id:
                return pirate
    return StatusType.FAILURE


class Ocean:
    def __init__(self):
        self.fleets = []
        self.fleet_ids = []
        self.pirate_ids = []

    def add_fleet(self, id):
        if id <= 0:
            return StatusType.INVALID_INPUT
        if id in self.fleet_ids:
            return StatusType.FAILURE
        self.fleets.append(Fleet(id))
        self.fleet_ids.append(id)
        return StatusType.SUCCESS

    def add_pirate(self, pirateId, fleetId):
        if pirateId <= 0 or fleetId <= 0:
            return StatusType.INVALID_INPUT
        if pirateId in self.pirate_ids or fleetId not in self.fleet_ids:
            return StatusType.FAILURE

        fleet = find_fleet(self.fleets, fleetId)
        if fleet == StatusType.FAILURE or not fleet.live:
            return StatusType.FAILURE
        pirate = Pirate(pirateId)
        fleet.add_pirate(pirate)
        self.pirate_ids.append(pirateId)
        return StatusType.SUCCESS

    def num_ships_for_fleet(self, fleetId):
        if fleetId <= 0:
            return output_t(StatusType.INVALID_INPUT)
        fleet = find_fleet(self.fleets, fleetId)
        if fleet == StatusType.FAILURE or not fleet.live:
            return output_t(StatusType.FAILURE)
        return output_t(StatusType.SUCCESS, fleet.ship_count)

    def pay_pirate(self, pirateId, money):
        if pirateId <= 0 or money <= 0:
            return StatusType.INVALID_INPUT
        pirate = find_pirate_in_ocean(self, pirateId)
        if pirate == StatusType.FAILURE:
            return StatusType.FAILURE
        pirate.money += money
        return StatusType.SUCCESS

    def get_pirate_money(self, pirateId):
        if pirateId <= 0:
            return output_t(StatusType.INVALID_INPUT)
        pirate = find_pirate_in_ocean(self, pirateId)
        if pirate == StatusType.FAILURE:
            return output_t(StatusType.FAILURE)
        return output_t(StatusType.SUCCESS, pirate.money)

    def unite_fleets(self, fleetId1, fleetId2):
        if fleetId1 <= 0 or fleetId2 <= 0 or fleetId1 == fleetId2:
            return StatusType.INVALID_INPUT
        fleet1 = find_fleet(self.fleets, fleetId1)
        fleet2 = find_fleet(self.fleets, fleetId2)
        if fleet1 == StatusType.FAILURE or fleet2 == StatusType.FAILURE:
            return StatusType.FAILURE
        if not fleet1.live or not fleet2.live:
            return StatusType.FAILURE

        if len(fleet1.pirates) >= len(fleet2.pirates):
            fleet1.ship_count += fleet2.ship_count
            fleet2.live = False
            change = len(fleet1.pirates)
            for pirate in fleet2.pirates:
                pirate.fleetId = fleetId1
                pirate.rank += change
                fleet1.pirates.append(pirate)
            return StatusType.SUCCESS

        else:
            fleet2.ship_count += fleet1.ship_count
            fleet1.live = False
            change = len(fleet2.pirates)
            for pirate in fleet1.pirates:
                pirate.fleetId = fleetId2
                pirate.rank += change
                fleet2.pirates.append(pirate)
            return StatusType.SUCCESS

    def pirate_argument(self, pirateId1, pirateId2):
        if pirateId1 <= 0 or pirateId2 <= 0 or pirateId1 == pirateId2:
            return StatusType.INVALID_INPUT
        pirate1 = find_pirate_in_ocean(self, pirateId1)
        pirate2 = find_pirate_in_ocean(self, pirateId2)
        if pirate1 == StatusType.FAILURE or pirate2 == StatusType.FAILURE:
            return StatusType.FAILURE
        if pirate1.fleetId != pirate2.fleetId:
            return StatusType.FAILURE

        diff = pirate1.rank - pirate2.rank
        pirate1.money -= diff
        pirate2.money += diff

        return StatusType.SUCCESS


def main(input_file, output_file):
    ocean = Ocean()
    run_file(input_file, output_file, ocean)
