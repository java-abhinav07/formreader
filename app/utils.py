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
