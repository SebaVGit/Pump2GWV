# Pump2GWV
This is a python script that creates a properly formatted .csv file for pumps in Groundwater Vistas
## Required packages
**pandas version:** `1.2.3 or later`\
**tqdm version:** `4.49.0 or later`\
**openpyxl version:** `3.0.7 or later`
## Running Example
In the **Example folder** you can find an CaudalToGWV.xlsx file, wich is the excel format that you must to use for now.\
You can run the script in windows by using the batch file `Executable.bat`\
and then change it as you like. This is how it look like:
```bash
@echo on
call activate base
python ..\Read_Binary_CLN_v1_git.py
pause
```
I use `call activate base` in order to activate the conda environment where I have those libraries.\
Finally you can run the script with your favorite text editor like VSCode or Spyder if you like.
## Capabilities
You can easily create `.csv file` that can be read by Groundwater Vistas as an input for the pumps.\
## Disclaimer
This version only creates outputs with the fields (like Numtrans, Layer_Top, etc)  that exist in the script.\
You can change that if you like and easely adapt it.\
This is the first version and I will improve the capabilities of it in order to make it easy to control it.
## Contact
Please if you want to improve the code feel free to contact me or make a pull request.\
email: `sebastian.vazquez@ug.uchile.cl`\
[Linkedin](https://www.linkedin.com/in/sebasti%C3%A1n-v%C3%A1zquez-gasty-952121181/)
