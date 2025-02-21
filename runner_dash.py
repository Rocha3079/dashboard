import sys
from streamlit.web import cli as stcli

sys.argv = ["streamlit", "run", r"C:\\Users\\lucas.fachi\\Desktop\\NICOLAS - GC\\PYTHON\\dashboard.py"]
sys.exit(stcli.main())