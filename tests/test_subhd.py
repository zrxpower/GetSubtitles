# coding: utf-8

import unittest
from getsub.downloader.subhd import SubHDDownloader


class TestSubHD(unittest.TestCase):

    def test_search(self):

        results = SubHDDownloader().get_subtitles(
            'Show.S01E01.ShowName.1080p.AMZN.WEB-DL.DDP5.1.H.264-GRP.mkv')
