#! /usr/bin/env python
from bs4 import BeautifulSoup
import requests
import json
import time
import re

session = requests.Session()

URL = "https://www.fishbase.se/identification/RegionSpeciesList.php?resultPage=1&&c_code=076"
URL2 = "https://www.fishbase.se/ComNames/CommonNamesList.php?ID=68792&GenusName=Acanthurus&SpeciesName=bahianus&StockCode=60405"
response = session.get(URL)

soup = BeautifulSoup(response.text,"html.parser")

