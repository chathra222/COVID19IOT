from boto3 import Session
from botocore.exceptions import BotoCoreError, ClientError
from contextlib import closing
import os
import sys
import subprocess
from tempfile import gettempdir
import json

def text2speech(message):
    session = Session(profile_name="default")
    polly = session.client("polly")
    #subscribe to mqtt topic and fetch announcement
    announcement = json.dumps(message).replace('\\n','')


    try:
        print(announcement)
        response = polly.synthesize_speech(Text=announcement, OutputFormat="mp3",VoiceId="Joanna")
    except (BotoCoreError, ClientError) as error:
        print(error)
        sys.exit(-1)

    if "AudioStream" in response:
        with closing(response["AudioStream"]) as stream:
            output = os.path.join(gettempdir(), "speech.mp3")

            try:
                with open(output, "wb") as file:
                    file.write(stream.read())
            except IOError as error:
                    print(error)
                    sys.exit(-1)

    else:
        print("Could not stream audio")
        sys.exit(-1)

    # Play the audio using the platform's default player
    if sys.platform == "win32":
        os.startfile(output)
    else:
        # The following works on macOS and Linux. (Darwin = mac, xdg-open = linux).
        opener = "open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([opener, output])