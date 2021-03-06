# Metabase Export Tool
#### Metabase database export tool written in Python language
This tool provides three main functionalities:
1. **Migrate**: export & import database (with related *metabase_table*, *metabase_field*, *metrics* tables) 
and Collection (with related *report_card*, *report_dashboard* and *report_dashboardcard* tables) 
from a DB source to a DB target
2. **Export**: export database (with related *metabase_table*, *metabase_field*, *metrics* tables) 
and Collection (with related *report_card*, *report_dashboard* and *report_dashboardcard* tables) 
from a DB source creating sql dump files (INSERT INTO statements)
3. **Delete**: delete a DB and a Collection (and their related tables)

Metabase Export Tool GUI was built using PyQt5 (Designer tool was used to write 
*MetabaseExportMain.ui* file)

Below a sample screenshot:

![alt text](MetabaseExportTool/images/gui.png "Metabase Export Tool GUI")

To setup program and download dependencies, run:
```shell script
pip install .
```

To start the program simply run:
```shell script
python MetabaseExportTool.py
```
It also install an executable script (.exe for Windows) in: ```YOUR_INSTALL_PATH\Scripts\metabase-exporter.exe``` 

There is also a config file (config_db.yml) for source and target database parameters configuration, located in ui folder.