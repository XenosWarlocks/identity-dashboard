from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, List
import uuid
from datetime import datetime

# Import your IdentityGenerator class
from identity_generator import IdentityGenerator

app = FastAPI()