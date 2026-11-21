class Television:
    """
    Class to represent a Television instance and its details.
    """
    # Python equivalent of constants to be used in subsequent methods
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        """
        Initializes an instance of Television class with default values.
        """
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL

    def power(self) -> None:
        """
        Method to change the power status of the Television instance.
        """
        if self.__status:
            self.__status = False
        else:
            self.__status = True

    def mute(self) -> None:
        """
        Method to change the mute status of the Television instance.
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
            else:
                self.__muted = True

    def channel_up(self) -> None:
        """
        Method to increase the channel value of the Television instance.
        Will loop from MAX_CHANNEL around to MIN_CHANNEL.
        """
        if self.__status:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self) -> None:
        """
        Method to decrease the channel value of the Television instance.
        Will loop from MIN_CHANNEL around to MAX_CHANNEL.
        """
        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self) -> None:
        """
        Method to increase the volume value of the Television instance.
        Will not increase past MAX_VOLUME.
        """
        if self.__status:
            self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        """
        Method to decrease the volume value of the Television instance.
        Will not decrease past MIN_VOLUME.
        """
        if self.__status:
            self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        """
        Method to access the settings of the Television instance.
        :return: String containing information about the power status, channel value, and volume value.
        """
        power = self.__status
        channel = self.__channel
        if self.__muted:
            volume = Television.MIN_VOLUME
        else:
            volume = self.__volume
        return f"Power = {power}, Channel = {channel}, Volume = {volume}"
