import os
import json
import uuid
import time
import requests
from flask import jsonify
from flask import Flask, request, jsonify

from utils import *
from aocr.__main__ import FormNet
from aocr.defaults import Config

formnet = FormNet()

formreader = Flask(__name__)

# {public_id: "827293842diwu323", version: "v1", image_url: "sample"}


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
    formreader.run(host="localhost", port=8001)
    # formreader.run()
