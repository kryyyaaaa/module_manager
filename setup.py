import setuptools
with open('README.md', 'r', encoding='utf-8') as fh:
	long_description = fh.read()

setuptools.setup(
	name='module_manager',
	version='0.1.0',
	author='kryyaa_sigma',
	author_email='kryyaaofficial@gmail.com',
	description='useful module',
	long_description=long_description,
	long_description_content_type='text/markdown',
	url='https://github.com/kryyyaaaa/module_manager',
	project_urls={
		'Documentation': 'https://github.com/kryyyaaaa/module_manager',
	},
	packages=['module_manager'],
	include_package_data=True,
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
	python_requires='>=3.7',
)