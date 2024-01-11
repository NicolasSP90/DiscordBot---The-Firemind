# Python Libraries
import os
from dotenv import load_dotenv


# Instancing Env Variables
load_dotenv()


class AuthFiremind:

    @staticmethod
    def auth_discord():
        # Discord Keys
        discordtoken = os.getenv('DiscordBotToken')

        # Return Key
        return discordtoken

    @staticmethod
    def auth_openai():
        # Discord Keys
        openaitoken = os.getenv('OpenAIAPISecKey')

        # Return Key
        return openaitoken
