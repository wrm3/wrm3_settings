import unittest
import os
import json
from wrm3_settings import Settings

class TestWRM3Settings(unittest.TestCase):
    def setUp(self):
        self.test_file = 'test_settings.json'
        self.template = {
            "edited_yn": "N",
            "some_setting_name": "some_setting_value",
            "some_setting_thats_an_int": 15,
            "some_setting_thats_a_float": 15.51,
            "some_setting_thats_a_list": ["DAI", "GUSD", "PAX", "PYUSD", "USD", "USDC", "USDT"],
            "some_setting_thats_a_dict": {
                "trade_yn": "Y",
                "trade_live_yn": "Y",
            }
        }
        self.settings = Settings(self.test_file, self.template)

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_settings_creation(self):
        self.assertTrue(os.path.exists(self.test_file))
        with open(self.test_file, 'r') as f:
            saved_settings = json.load(f)
        self.assertEqual(saved_settings, self.template)

    def test_settings_load(self):
        st = self.settings.reload()
        self.assertEqual(st.edited_yn, "N")
        self.assertEqual(st.some_setting_name, "some_setting_value")
        self.assertEqual(st.some_setting_thats_an_int, 15)
        self.assertAlmostEqual(st.some_setting_thats_a_float, 15.51)
        self.assertEqual(st.some_setting_thats_a_list, ["DAI", "GUSD", "PAX", "PYUSD", "USD", "USDC", "USDT"])
        self.assertEqual(st.some_setting_thats_a_dict.trade_yn, "Y")
        self.assertEqual(st.some_setting_thats_a_dict.trade_live_yn, "Y")

    def test_settings_access(self):
        st = self.settings.reload()
        self.assertEqual(st['edited_yn'], "N")
        self.assertEqual(st['some_setting_thats_a_dict']['trade_yn'], "Y")

    def test_settings_update(self):
        st = self.settings.reload()
        st.edited_yn = "Y"
        st.some_setting_thats_an_int = 20
        self.settings.file_write(st)

        st = self.settings.reload()
        self.assertEqual(st.edited_yn, "Y")
        self.assertEqual(st.some_setting_thats_an_int, 20)

    def test_get_ovrd(self):
        settings_with_override = {
            "***": -1,
            "BTC": 42,
            "ETH": 123,
            "SOL": 57,
            "USDC": 99
        }
        self.assertEqual(self.settings.get_ovrd(settings_with_override, 'BTC'), 42)
        self.assertEqual(self.settings.get_ovrd(settings_with_override, 'XXX'), -1)

    def test_multiple_settings(self):
        buy_settings = Settings('buy_settings.json', {"buying_on": True})
        sell_settings = Settings('sell_settings.json', {"selling_on": False})

        self.assertTrue(buy_settings.reload().buying_on)
        self.assertFalse(sell_settings.reload().selling_on)

        os.remove('buy_settings.json')
        os.remove('sell_settings.json')

if __name__ == '__main__':
    unittest.main()
