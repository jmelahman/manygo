from __future__ import annotations

import unittest

from src.manygo import get_platform_tag


class TestManyGo(unittest.TestCase):
    def test_get_platform_tag_darwin(self) -> None:
        assert get_platform_tag('darwin', 'amd64') == 'macosx_10_12_x86_64'
        assert get_platform_tag('darwin', 'arm64') == 'macosx_11_0_arm64'
        with self.assertRaises(ValueError):
            get_platform_tag('darwin', '386')

    def test_get_platform_tag_linux(self) -> None:
        assert get_platform_tag('linux', 'amd64') == 'manylinux_2_17_x86_64'
        assert get_platform_tag('linux', 'arm64') == 'manylinux_2_17_aarch64'
        assert get_platform_tag('linux', '386') == 'manylinux_2_17_i686'
        assert get_platform_tag('linux', 'arm') == 'manylinux_2_17_armv7l'

    def test_get_platform_tag_windows(self) -> None:
        assert get_platform_tag('windows', 'amd64') == 'win_amd64'
        assert get_platform_tag('windows', 'arm64') == 'win_arm64'
        assert get_platform_tag('windows', '386') == 'win32'

if __name__ == "__main__":
    unittest.main()