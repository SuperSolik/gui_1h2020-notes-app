# gui_1h2020-notes-app
##  Requirements
Python3.8, SQLite
```bash
sudo apt-get update && apt-get install python3.8 sqlite3 python3-pyqt5 python3-pyqt5.qtwebengine
```  
## Installation & start  
1. Using local machine:  

```bash
./start.sh
```  
2. Using docker:  

```bash
./start_docker.sh
```  
## Usage
Features:  
* Create and delete notes  
* Create and add labels to notes, allowing to group notes  
* Provides two modes: edit and render  
* Render mode supports Markdown, allowing user to format text in edit mode using Markdown syntax  
* Current notes list can be filtered by user input, filter is applied to notes' titles  
* Notes are stored in database, so all changes will be available after reopening application  
