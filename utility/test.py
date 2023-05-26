import base64
from PIL import Image
from io import BytesIO

# Base64 encoded image string
encoded_image = "/9j/4QAiRXhpZgAATU0AKgAAAAgAAQESAAMAAAABAAEAAAAAAAD/7QA4UGhvdG9zaG9wIDMuMAA4QklNBAQAAAAAAAA4QklNBCUAAAAAABDUHYzZjwCyBOmACZjs\u002BEJ\u002B/\u002BICKElDQ19QUk9GSUxFAAEBAAACGGFwcGwEAAAAbW50clJHQiBYWVogB\u002BYAAQABAAAAAAAAYWNzcEFQUEwAAAAAQVBQTAAAAAAAAAAAAAAAAAAAAAAAAPbWAAEAAAAA0y1hcHBs7P2jjjiFR8NttL1PetoYLwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKZGVzYwAAAPwAAAAwY3BydAAAASwAAABQd3RwdAAAAXwAAAAUclhZWgAAAZAAAAAUZ1hZWgAAAaQAAAAUYlhZWgAAAbgAAAAUclRSQwAAAcwAAAAgY2hhZAAAAewAAAAsYlRSQwAAAcwAAAAgZ1RSQwAAAcwAAAAgbWx1YwAAAAAAAAABAAAADGVuVVM"

try:
    padding = "=" * (4 - (len(encoded_image) % 4))
    padded_encoded_image = encoded_image + padding

    image_bytes = base64.b64decode(padded_encoded_image)

    image = Image.open(BytesIO(image_bytes))

    image.save("image.jpg")

    print("Image saved successfully!")
except OSError as e:
    if str(e) == "Truncated File Read":
        print("Error: Truncated file read. The image data might be incomplete or corrupted.")
    else:
        print(f"Error: {str(e)}")
except Exception as e:
    print(f"Error: {str(e)}")
