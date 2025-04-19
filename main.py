import os
from spitch import Spitch

os.environ["SPITCH_API_KEY"] = "YOUR_API_KEY"
client = Spitch()

with open("new.mp3", "wb") as f:
    response = client.speech.generate(
        text="Bawo ni ololufe mi?",
        language="yo",
        voice="sade"
    )
    f.write(response.read())