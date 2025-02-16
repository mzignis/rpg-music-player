from abc import ABC, abstractmethod


class AbstractYoutubeResult(ABC):
    @abstractmethod
    def title(self) -> str:
        pass

    @abstractmethod
    def url(self) -> str:
        pass

    @abstractmethod
    def thumbnail(self) -> str:
        pass

    @abstractmethod
    def duration(self) -> int:
        pass

    @abstractmethod
    def channel_name(self) -> str:
        pass

    @abstractmethod
    def channel_url(self) -> str:
        pass

    @abstractmethod
    def channel_thumbnail(self) -> str:
        pass

    @abstractmethod
    def description(self) -> str:
        pass

    @abstractmethod
    def tags(self) -> list:
        pass

    @abstractmethod
    def category(self) -> str:
        pass


class YoutubeResult(AbstractYoutubeResult):
    def __init__(
            self,
            title: str,
            url: str,
            thumbnail: str,
            duration: int,
            channel_name: str,
            channel_url: str,
            channel_thumbnail: str,
            description: str,
            # tags: list,
            # category: str
    ):
        self._title: str = title
        self._url: str = url
        self._thumbnail: str = thumbnail
        self._duration: int = duration
        self._channel_name: str = channel_name
        self._channel_url: str = channel_url
        self._channel_thumbnail: str = channel_thumbnail
        self._description: str = description
        # self._tags: list = tags
        # self._category: str = category

    def __str__(self):
        return f"YoutubeResult(title={self.title}, channel={self.channel_name}, url={self.url})"

    def __repr__(self):
        return f"YoutubeResult(title={self.title}, channel={self.channel_name}, url={self.url})"

    @property
    def title(self) -> str:
        return self._title

    @title.setter
    def title(self, value: str):
        self._title = value

    @property
    def url(self) -> str:
        return self._url

    @url.setter
    def url(self, value: str):
        self._url = value

    @property
    def thumbnail(self) -> str:
        return self._thumbnail

    @thumbnail.setter
    def thumbnail(self, value: str):
        self._thumbnail = value

    @property
    def duration(self) -> int:
        return self._duration

    @duration.setter
    def duration(self, value: int):
        self._duration = value

    @property
    def channel_name(self) -> str:
        return self._channel_name

    @channel_name.setter
    def channel_name(self, value: str):
        self._channel_name = value

    @property
    def channel_url(self) -> str:
        return self._channel_url

    @channel_url.setter
    def channel_url(self, value: str):
        self._channel_url = value

    @property
    def channel_thumbnail(self) -> str:
        return self._channel_thumbnail

    @channel_thumbnail.setter
    def channel_thumbnail(self, value: str):
        self._channel_thumbnail = value

    @property
    def description(self) -> str:
        return self._description

    @description.setter
    def description(self, value: str):
        self._description = value

    @property
    def tags(self) -> list:
        return self._tags

    @tags.setter
    def tags(self, value: list):
        self._tags = value

    @property
    def category(self) -> str:
        return self._category

    @category.setter
    def category(self, value: str):
        self._category = value


if __name__ == '__main__':
    pass
