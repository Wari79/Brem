import discord
from discord.ext import commands
from replit import db
import requests
import random
import json
import asyncio
from keep_alive import keep_alive
import os
from discord.utils import find
import datetime
from datetime import datetime
from discord.ext import tasks
from googletrans import Translator
import traceback
import sys

class instructions(commands.Cog):
    def __init__(self, client):
        self.client = client



def setup(client):
  client.add_cog(instructions(client))