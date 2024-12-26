from t import check_and_install, start_modules_instalation

packages = [
	{"name": "colorama", "version": "0.4.6"},
	{"name": "rich", "version": "13.9.4"}
]

start_modules_instalation(packages)