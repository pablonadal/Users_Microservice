from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os
from pathlib import Path

basedir = os.path.abspath(Path(__file__).parents[2])
load_dotenv(os.path.join(basedir,'.env'))

db = SQLAlchemy()

USER_DB = os.getenv('USER_DB')
PASS_DB = os.getenv('PASS_DB')
URL_DB = os.getenv('URL_DB')
NAME_DB = os.getenv('NAME_DB')

FULL_URL_DB = f'postgresql://{USER_DB}:{PASS_DB}@{URL_DB}/{NAME_DB}'