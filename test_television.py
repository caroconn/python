import pytest
from television import *

class Test:
    def setup_method(self):
        self.tv1 = Television()

    def teardown_method(self):
        del self.tv1

    def test_init(self):
        assert self.tv1.__str__() == "Power = False, Channel = 0, Volume = 0"

    def test_power(self):
        self.tv1.power()
        assert self.tv1.__str__() == "Power = True, Channel = 0, Volume = 0"

        self.tv1.power()
        assert self.tv1.__str__() == "Power = False, Channel = 0, Volume = 0"

    def test_mute(self):
        # test turning tv on and volume up, confirm starting volume at 1 before
        # testing mute function
        self.tv1.power()
        self.tv1.volume_up()
        assert self.tv1.__str__() == "Power = True, Channel = 0, Volume = 1"

        # mute function
        self.tv1.mute()
        assert self.tv1.__str__() == "Power = True, Channel = 0, Volume = 0"

        # stays muted when tv is turned off
        self.tv1.power()
        assert self.tv1.__str__() == "Power = False, Channel = 0, Volume = 0"

        # turns on and unmutes tv
        self.tv1.power()
        self.tv1.mute()
        assert self.tv1.__str__() == "Power = True, Channel = 0, Volume = 1"

        # stays unmuted when tv is turned off
        self.tv1.power()
        assert self.tv1.__str__() == "Power = False, Channel = 0, Volume = 1"

    def test_channel_up(self):
        # channel up does not change channel when tv is off
        self.tv1.channel_up()
        assert self.tv1.__str__() == "Power = False, Channel = 0, Volume = 0"

        # channel up changes channel when tv is on
        self.tv1.power()
        self.tv1.channel_up()
        assert self.tv1.__str__() == "Power = True, Channel = 1, Volume = 0"

        self.tv1.channel_up()
        assert self.tv1.__str__() == "Power = True, Channel = 2, Volume = 0"
        self.tv1.channel_up()
        assert self.tv1.__str__() == "Power = True, Channel = 3, Volume = 0"

        # channel up loops back to first channel
        self.tv1.channel_up()
        assert self.tv1.__str__() == "Power = True, Channel = 0, Volume = 0"

    def test_channel_down(self):
        # channel up does not change channel when tv is off
        self.tv1.channel_down()
        assert self.tv1.__str__() == "Power = False, Channel = 0, Volume = 0"

        # channel down changes channel when tv is on and loops from 0 to 3
        self.tv1.power()
        self.tv1.channel_down()
        assert self.tv1.__str__() == "Power = True, Channel = 3, Volume = 0"

    def test_volume_up(self):
        # volume_up doesn't work when tv is off
        self.tv1.volume_up()
        assert self.tv1.__str__() == "Power = False, Channel = 0, Volume = 0"

        # volume up works when tv is on
        self.tv1.power()
        self.tv1.volume_up()
        assert self.tv1.__str__() == "Power = True, Channel = 0, Volume = 1"

        # volume up unmutes and increases volume
        self.tv1.mute()
        assert self.tv1.__str__() == "Power = True, Channel = 0, Volume = 0"
        self.tv1.volume_up()
        assert self.tv1.__str__() == "Power = True, Channel = 0, Volume = 2"

        # volume up cannot go past max volume
        self.tv1.volume_up()
        self.tv1.volume_up()
        self.tv1.volume_up()
        assert self.tv1.__str__() == "Power = True, Channel = 0, Volume = 2"

    def test_volume_down(self):
        # set tv to on and max volume
        self.tv1.power()
        self.tv1.volume_up()
        self.tv1.volume_up()
        self.tv1.volume_up()
        assert self.tv1.__str__() == "Power = True, Channel = 0, Volume = 2"

        # mute tv then decrease volume
        self.tv1.mute()
        self.tv1.volume_down()
        assert self.tv1.__str__() == "Power = True, Channel = 0, Volume = 1"

        # decrease volume
        self.tv1.volume_down()
        assert self.tv1.__str__() == "Power = True, Channel = 0, Volume = 0"

        # cannot decrease past 0
        self.tv1.volume_down()
        assert self.tv1.__str__() == "Power = True, Channel = 0, Volume = 0"

        # increase to max for test
        self.tv1.volume_up()
        self.tv1.volume_up()

        # volume down does not work when tv is off
        self.tv1.power()
        self.tv1.volume_down()
        assert self.tv1.__str__() == "Power = False, Channel = 0, Volume = 2"