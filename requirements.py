import os



path_to_archieve= os.path.dirname(__file__) + "/test_images"
path_to_excel = os.path.dirname(__file__) +"./dataset.xlsx"
days_of_archieve=1/32 #in order to set a condition to stop the program if the maximum possible combinations of the images was reached.

dtstart = '2020-09-01T00_00_00'
dtend = '2020-09-01T00_30_00'

# Commandes pour execution:
# .venv\Scripts\Activate.ps1
# streamlit run app.py / python -m streamlit run app.py
# deactivate