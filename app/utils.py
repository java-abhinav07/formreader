import numpy as np
import uuid
import os
import time
import uuid
import requests
import shutil
import traceback

asset_dir = os.path.dirname(os.path.realpath(__file__)) + "/tmp/"


def create_error_result(error_code):
    result = {}
    result["error"] = {}
    result["error"]["code"] = error_code
    return result


def generate_final_response(result, public_id, version):
    response = {}
    response["public_id"] = public_id
    response["version"] = version
    if isinstance(result, dict) and "error" in result:
        response["error"] = result["error"]
        response["status"] = "invalid_request"
    else:
        response["status"] = "completed"
        if version == "v1":
            response["result"] = result

    print(public_id, "Response = ", response)
    # print(public_id, "Total app time taken = " + str(time.time() - start_time))
    return response


def delete_image(image_path):
    if image_path is not None and os.path.exists(image_path):
        os.remove(image_path)


def download_image(image_url, public_id):
    name = str(uuid.uuid1()) + ".jpg"
    image_path = asset_dir + name
    if not os.path.isdir(asset_dir):
        os.mkdir(asset_dir)
    try:
        response = requests.get(image_url, stream=True, allow_redirects=True)
    except:
        print(public_id + " Failed while downloading image", traceback.format_exc())
        return image_path, create_error_result("PE_DOWNLOAD_IMAGE_FAILED")
    if response.status_code == 200:
        try:
            try:
                with open(image_path, "wb") as out_file:
                    for chunk in response.iter_content(chunk_size=1024):
                        out_file.write(chunk)
                return image_path, None
            except:
                if os.path.exists(image_path):
                    os.remove(image_path)
                with open(image_path, "wb") as out_file:
                    shutil.copyfileobj(response.raw, out_file)
                return image_path, None
        except:
            return image_path, create_error_result("PE_FILE_WRITE_ERROR")
    else:
        return image_path, create_error_result("PE_DOWNLOAD_IMAGE_FAILED")
