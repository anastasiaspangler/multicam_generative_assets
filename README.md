# Generating 3D Assets
This program offers a bit of infrastructure to get you quickly generating 3D assets using a two-camera setup.


<img width="2535" height="1268" alt="demo" src="https://github.com/user-attachments/assets/94005bb3-9706-43a1-8426-6217eab48e4f" />

## Setup
A [Replicate](https://replicate.com/docs/reference/http#authentication) account is required. Replicate offers endpoints for community AI models. The model used here costs about $0.04 (USD) per run.

Two cameras are required. If you have an updated iPhone, you can use the Continuity Camera feature and openCV will read it. 

Bright lighting and a clean surface will achieve higher quality generations.

## Running the program
**Install requirements**
```
pip install -r requirements.txt
```

**Run the Flask App**
```
python -m flask run
```

**Open a New Terminal**

You're going to have two runs active in parallel. Don't close the terminal running the app.
```
python terminal_capture.py
```

Verify that the two camera feed windows that open are what you want. If you only see one, they might be on top of each other.

The prompts in the terminal will guide you on capture. Once the prediction is complete, the  response will appear in the terminal with a link to the viewer.

```
To begin a capture, position your item and hit the 'a' key.
This will take the first two images.
Object VgdVNtoceu: first shots saved. Adjust pose, then press 'n' for second shots.
Object VgdVNtoceu: second shots saved. Capture complete.
Sending to queue...
{'preview': 'http://127.0.0.1:5000/viewer/VgdVNtoceu', 'received': {'name': 'VgdVNtoceu', 'path_a': 'local_storage/VgdVNtoceu/img_a1.png', 'path_b': 'local_storage/VgdVNtoceu/img_b1.png', 'path_c': 'local_storage/VgdVNtoceu/img_a2.png', 'path_d': 'local_storage/VgdVNtoceu/img_b2.png', 'timestamp': '2025-08-30T15:32:09.538134', 'type': 'rep_out'}, 'status': 'pass'}
```

## Accessing Data

Each capture is assigned a random string as an object name. Under **local_storage** you can view your data.

<img width="446" height="240" alt="Screenshot 2025-08-30 at 4 08 54 PM" src="https://github.com/user-attachments/assets/bec8f8fc-6f16-438e-8cb7-7b149b8477d8" />

## My Setup

![IMG_0004](https://github.com/user-attachments/assets/62fa02c4-0009-4965-b876-ccafbfb372f2)









