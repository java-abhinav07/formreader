import os
import json
import uuid
import time
import requests
from flask import jsonify
from flask import Flask, request, jsonify

import numpy as np
import uuid
import os
import time
import uuid
import requests
import shutil
import traceback

# from utils import *
from aocr.__main__ import FormNet
from aocr.defaults import Config

formnet = FormNet()

formreader = Flask(__name__)

# {public_id: "827293842diwu323", version: "v1", image_url: "sample"}

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



@formreader.route("/predict", methods=["POST"])
def handwritten_ocr_http():
    req = request.get_data()
    response = handwritten_ocr(req)
    return jsonify(response)


def handwritten_ocr(request):
    result = dict()
    version = "v1"

    try:
        # request validation
        try:
            request = json.loads(request.decode("utf-8"))
        except:
            print("[ERR] Could not load request")
            result = create_error_result("PE_BAD_REQUEST")
            return generate_final_response(result, "", "")

        public_id = request.get("public_id", None)

        if public_id is None:
            print("[ERR] Public ID not provided")
            result = create_error_result("PE_BAD_REQUEST")
            return generate_final_response(result, public_id, "")

        if version == "v1":
            image_url = request.get("data", {}).get("image_url", None)
            if image_url is None:
                print("[ERR] Could not get reference image")
                result = create_error_result("PE_BAD_REQUEST")
                return generate_final_response(result, public_id, version)

        else:
            print("[ERR] Bad version")
            result = create_error_result("PE_UNSUPPORTED_VERSION")
            return generate_final_response(result, public_id, version)

        max_width = int(request.get("max_width", None))
        if max_width is None:
            print("[ERR] Could not get reference image")
            result = create_error_result("PE_BAD_REQUEST")
            return generate_final_response(result, public_id, version)

        max_height = int(request.get("max_width", None))
        if max_height is None:
            print("[ERR] Could not get reference image")
            result = create_error_result("PE_BAD_REQUEST")
            return generate_final_response(result, public_id, version)

        # download images
        image, error = download_image(image_url, public_id)
        if error is not None:
            delete_image(image_url)
            return generate_final_response(error, public_id, version)

        print("[INFO] Successfully downloaded images...")
        # print(help(aocr))
        # get results
        text, probability = formnet.prediction(
            image
        )  # add appropriate arguments for prediction

        print("[INFO] OCR results fetched...")

        # make result dict from response
        result["prediction"] = text
        result["probability"] = probability

    except Exception as e:
        print(e)
        result = create_error_result("PE_INTERNAL_ERROR")

    delete_image(image)

    print("[INFO] Returning response...")
    return generate_final_response(result, public_id, version)


# index.html random index page
@formreader.route("/")
def index():
    return json.dumps({"success": True}), 200, {"ContentType": "application/json"}


if __name__ == "__main__":
    formreader.debug = True
    # formreader.run(host="localhost", port=8001)
    formreader.run()
