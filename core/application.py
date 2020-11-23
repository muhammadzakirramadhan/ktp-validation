import cv2
import numpy as np
import pytesseract
import matplotlib.pyplot as plt
from PIL import Image
import requests
from flask import request
from werkzeug.utils import secure_filename

def allowed_image(filename):
	allow = ["JPEG", "JPG", "PNG"]

	if not "." in filename:
		return False

	ext = filename.rsplit(".", 1)[1]
	if ext.upper() in allow:
		return True
	else:
		return False

def ocr_ktp():
	if request.method == "POST":
		image = request.files["ktp"]

		if image.filename == "":
			return {
				'success':False,
				'message':'Empty Fields!'
			}

		if allowed_image(image.filename):
			img = cv2.imdecode(np.fromstring(request.files['ktp'].read(), np.uint8), cv2.IMREAD_UNCHANGED)	
			gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
			th, threshed = cv2.threshold(gray, 127, 255, cv2.THRESH_TRUNC)
			result = pytesseract.image_to_string((threshed), lang="ind")
			valid = False

			if 'NIK' in result:
				valid = True
			else:
				valid = False

			return {
				'success':True,
				'results':{
					'valid':valid
				}
			}
		else:	
			return {
				'success':False,
				'message':'Extension Not Allowed!'
			}
	else:
		return {
			'success':False,
			'message':'method Not Allowed!'
		}