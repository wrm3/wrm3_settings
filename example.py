#<=====>#
# Description
#<=====>#


#<=====>#
# Known To Do List
#<=====>#


#<=====>#
# Imports - Common Modules
#<=====>#

#<=====>#
# Imports - Download Modules
#<=====>#


#<=====>#
# Imports - Shared Library
#<=====>#

from wrm3_settings import Settings
from pprint import pprint

#<=====>#
# Imports - Local Library
#<=====>#


#<=====>#
# Variables
#<=====>#


#<=====>#
# Assignments Pre
#<=====>#

settings_template_json = {
	"edited_yn": "N",
	"some_setting_name_1": "some_setting_value_1",
	"some_setting_name_2": "some_setting_value_2",
	"some_setting_thats_an_int": 15,
	"some_setting_thats_a_float": 15.51,
	"some_setting_thats_a_list": ["DAI","GUSD","PAX","PYUSD","USD","USDC","USDT"],
	"some_setting_thats_a_str": "I wish I remember why I tied this string around my finger",
	"some_setting_thats_a_dict": {
		"trade_yn": "Y",
		"trade_live_yn": "Y",
		},
	"some_settings_thats_a_list": {
				"***": -1,
				"BTC": 42,
				"ETH": 123,
				"SOL": 57,
				"USDC": 99
				}
	}

buy_tmplt_json = {
	"edited_yn": "N",
	"buying_on_tf": False
	}


sell_tmplt_json = {
	"edited_yn": "N",
	"selling_on_tf": False
	}

log_tmplt_json = {
	"edited_yn": "N",
	"logging_tf": True
	}


#<=====>#
# Classes
#<=====>#



#<=====>#
# Functions
#<=====>#

def test_main():

	print('')
	print('#0 defining ')
	print("st = Settings('settings/settings.json', settings_template_json)")
	settings = Settings('settings/settings.json', settings_template_json)

	print('')
	print('# 1 if this is the first time trying this it will stop and create the missing folder and file.  the new file will be populated with the default templace json.')
	print('Any modifications from the default template will be accepted.')
	print('For example flipping the edited_yn flag to Y')
	print('once edited run the file again')

	print('# 2 to reload the settings... for example in a loop script where you might need to hot edit the scip without restarting.. ')
	print('You can use either of these commands... both perform the same action')

	print('st = st.settings_load()')
	st = settings.settings_load()
	print('st = st.reload()')
	st = settings.reload()
	pprint(st)

	print('')
	print('if this is the second or later trying this will print some keys from the entire structure.')
	print('# 3 printing everything - will contain the functions also...fyi')
	pprint(st)

	print('# 4 printing several different keys with different value types')
	print('st.edited_yn')
	print(st.edited_yn)

	print('')
	print('st.some_setting_name_2')
	print(st.some_setting_name_2)

	print('')
	print('st.some_setting_thats_an_int')
	print(st.some_setting_thats_an_int)

	print('')
	print('st.some_setting_thats_a_float')
	print(st.some_setting_thats_a_float)

	print('')
	print('st.some_setting_thats_a_list')
	print(st.some_setting_thats_a_list)

	print('')
	print('st.some_setting_thats_a_str')
	print(st.some_setting_thats_a_str)

	print('')
	print('st.some_setting_thats_a_dict')
	print(st.some_setting_thats_a_dict)

	print('# 5 Note you can access the settings structure using the key names like a dictionary or using .keyname like an object interchangeably')
	print('You can event mix and match, if needed.  ie assigning keys from a list you would use []')
	print("st['edited_yn']")
	print(st.edited_yn)

	print('')
	print('st.some_setting_thats_a_dict.trade_yn')
	print(st.some_setting_thats_a_dict.trade_yn)

	print('')
	print("st['some_setting_thats_a_dict'].trade_yn")
	print(st['some_setting_thats_a_dict'].trade_yn)

	print('')
	print("st['some_setting_thats_a_dict']['trade_yn']")
	print(st['some_setting_thats_a_dict']['trade_yn'])


	print('')
	print('# 6 You can even add default overides')
	print("st.some_settings_thats_a_list")
	print(st.some_settings_thats_a_list)

	print('')
	print("lets get the value for BTC")
	print("st.get_ovrd(in_dict=st.some_settings_thats_a_list, in_key='BTC')")
	print(settings.get_ovrd(in_dict=st.some_settings_thats_a_list, in_key='BTC'))

	print('')
	print("lets get the value for something not specifically in the list to check the default value...")
	print("st.get_ovrd(in_dict=st.some_settings_thats_a_list, in_key='XXX')")
	print(settings.get_ovrd(in_dict=st.some_settings_thats_a_list, in_key='XXX'))

	print('')
	print('# 7 I cannot easily demonstrate this via code... ')
	print("if you edit the file and it no longer is valid json, the script used to replace your file with the default template")
	print("After having lost a bunch of data this way, it now creates a dated file backup before replacing your json file with a blank template.")

	print('')
	print('# 8 You can even have multiple settings objects running at the same time... ')
	print("")
	print("buy_settings = Settings('some_folder/buy_settings.json', buy_tmplt_json)")
	print("sell_settings = Settings('some_folder/sell_settings.json', sell_tmplt_json)")
	print("log_settings = Settings('log_settings.json', log_tmplt_json)")

	print("")
	buy_settings = Settings('some_folder/buy_settings.json', buy_tmplt_json)
	sell_settings = Settings('some_folder/sell_settings.json', sell_tmplt_json)
	log_settings = Settings('log_settings.json', log_tmplt_json)

	print("")
	print("buy_st = buy_settings.reload()")
	print("sell_st = sell_settings.reload()")
	print("log_st = log_settings.reload()")

	print("")
	buy_st = buy_settings.reload()
	sell_st = sell_settings.reload()
	log_st = log_settings.reload()

	print("")
	pprint("buy_st...")
	pprint(buy_st)

	print("")
	pprint("sell_st...")
	pprint(sell_st)

	print("")
	pprint("log_st...")
	pprint(log_st)

	print()


#<=====>#
# Post Variables
#<=====>#


#<=====>#
# Default Run
#<=====>#

if __name__ == "__main__":
	test_main()

#<=====>#

