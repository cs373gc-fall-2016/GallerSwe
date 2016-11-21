from temp_app import DB
from model import Style
import re

pattern = re.compile(r"\[(?P<gene>.*?)\]\((.*?)\)")
styles = DB.session.query(Style).all()
for s in styles:
    s.description = re.sub("_", "", s.description)
    DB.session.commit()
