import replicate
import os


def send_to_replicate(name, abs_paths):
    image_datas = []
    for abs_path in abs_paths:
        image_datas.append(open(abs_path, 'rb'))

    input = {
        "images": image_datas,
        "texture_size": 2048,
        "mesh_simplify": 0.9,
        "generate_model": True,
        "save_gaussian_ply": True,
        "ss_sampling_steps": 38
    }

    output = replicate.run(
        "firtoz/trellis:e8f6c45206993f297372f5436b90350817bd9b4a0d52d2a76df50c1c8afa2b3c",
        input=input
    )

    save_generation(output, name)
    return output

def save_generation(output, obj_name):
    prediction_dir = "local_storage/" + obj_name + "/replicate_predictions"
    os.makedirs(prediction_dir, exist_ok=True)

    color_video = output["color_video"]
    video_path = prediction_dir + "/" + obj_name + "_" + "color_video.mp4"
    with open(video_path, "wb") as f:
        f.write(color_video.read())

    model_file = output["model_file"]
    model_path = prediction_dir + "/" + obj_name + "_" + "output.glb"
    with open(model_path, "wb") as f:
        f.write(model_file.read())

    gaussian_ply = output["gaussian_ply"]
    gaussian_path = prediction_dir + "/" + obj_name + "_" + "output_gaussian.ply"
    with open(gaussian_path, "wb") as f:
        f.write(gaussian_ply.read())
