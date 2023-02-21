import qrcode
import os
import json
from dotenv import load_dotenv


def generate_data():
    sibel_data = {
        "EnvName": os.getenv("EnvName"),
        "ApiEndpoint": os.getenv("ApiEndpoint"),
        "UserpoolId": os.getenv("UserpoolId"),
        "ClientId": os.getenv("ClientId"),
    }
    return json.dumps(sibel_data)


if __name__ == '__main__':
    # List of .env files to load
    envs = ['demo', 'dev', 'internal', 'prod', 'rph', 'test']

    # Loop through the files and load the environment variables
    for env in envs:
        load_dotenv(f"envs/{env}.env")

        # Set default qr code & data format setting
        qr = qrcode.QRCode(
            version=1,
            box_size=10,
            border=5
        )

        # Add the JSON data to the QR code
        qr.add_data(generate_data())

        # Generate the QR code image
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")

        # Save the image to a file
        img.save("qrcode.png")
