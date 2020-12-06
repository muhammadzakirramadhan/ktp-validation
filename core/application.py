import cv2
import numpy as np
import pytesseract
import matplotlib.pyplot as plt
from PIL import Image
import requests
from flask import request
from werkzeug.utils import secure_filename
import re

def allowed_image(filename):
	allow = ["JPEG", "JPG", "PNG"]

	if not "." in filename:
		return False

	ext = filename.rsplit(".", 1)[1]
	if ext.upper() in allow:
		return True
	else:
		return False

def word_to_number_converter(word):
	word_dict = {
		"L" : "1",
		'l' : "1",
		'O' : "0",
		'o' : "0",
		'?' : "7"
	}

	res = ''
	for letter in word:
		if letter in word_dict:
			res += word_dict[letter]
		else:
			res += letter
	return res

def match_ktp_nik():
	if request.method == "POST":
		image = request.files["ktp"]
		noktp = request.form['nik']

		if image.filename == "":
			return {
				'success':False,
				'message':'Empty Fields!'
			}

		if noktp == "":
			return {
				'success':False,
				'message':'Empty Fields!'
			}

		if allowed_image(image.filename):
			img = cv2.imdecode(np.fromstring(request.files['ktp'].read(), np.uint8), cv2.IMREAD_UNCHANGED)  
			gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
			th, threshed = cv2.threshold(gray, 127, 255, cv2.THRESH_TRUNC)
			result = pytesseract.image_to_string((threshed), lang="ind")
			result.replace('\n', ' ')
			match = False

			if 'NIK' in result:

				for word in result.split("\n"):
					if "NIK" in word:
						word = word.split(':')
						nik = word_to_number_converter(word[-1].replace(" ", ""))
						
						if noktp == nik:
							match = True
						else:
							match = False

						return {
							'success':True,
							'result': {
								'match':match,
								'nik':noktp
							}
						}	
			else:
				return {
					'success':False,
					'message':'KTP Tidak Terdeteksi'
						}			
		else: 
			return {
				'success':False,
				'message':'Extension Not Allowed!'
			}			
	else:
		return {
			'success':False,
			'message':'Method Not Allowed!'
		}

def valid_ktp():
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
			result.replace('\n', ' ')
			valid = False

			if 'NIK' in result:
				valid = True
			else:
				valid = False

			return {
				'success':True,
				'result':{
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
			'message':'Method Not Allowed!'
		}

def extract_ktp():
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
			result.replace('\n', ' ')

			if 'NIK' in result and 'Nama' in result and 'Lahir' in result and 'Jenis kelamin' in result and 'Alamat' in result:
				for word in result.split("\n"):
					if "NIK" in word:
						word = word.split(':')
						nik = word_to_number_converter(word[-1].replace(" ", ""))
						continue

					if "Nama" in word:
						word = word.split(':')
						nama = word[-1]

					if "Lahir" in word:
						word = word.split(':')
						tgl_lahir = re.search("([0-9]{2}\-[0-9]{2}\-[0-9]{4})", word[-1])[0]
						tmp_lahir = word[-1].replace(tgl_lahir, '')     
						continue

					if 'Darah' in word:
						jenis_kelamin = re.search("(LAKI-LAKI|LAKI|LELAKI|PEREMPUAN)", word)[0]
						word = word.split(':')

				return {
					'success':True,
					'message':'Valid KTP',
					'data': {
						'nik':nik,
						'nama':nama,
						'tanggal_lahir': tgl_lahir,
						'tempat_lahir':tmp_lahir,
						'jenis_kelamin':jenis_kelamin
					}
				}

			elif 'NIK' in result:
				return {
					'success':True,
					'message':'Foto KTP BLur/Rusak/Low Resolution'
				}   
			else:
				return {
					'success':False,
					'message':'KTP Tidak Terdeteksi'
				}
		else:   
			return {
				'success':False,
				'message':'Extension Not Allowed!'
			}
	else:
		return {
			'success':False,
			'message':'mMthod Not Allowed!'
		}