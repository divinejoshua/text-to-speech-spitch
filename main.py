import os
from spitch import Spitch


os.environ["SPITCH_API_KEY"] = os.getenv("SPITCH_API_KEY")
client = Spitch()

with open("new.mp3", "wb") as f:
    response = client.speech.generate(
        text="Movies, oh my gosh, I just just absolutely love them. They are like time machines taking you to different worlds and landscapes, and um, and I just cant get enough of it.",
        language="en",
        voice="lucy",
    )
    f.write(response.read())