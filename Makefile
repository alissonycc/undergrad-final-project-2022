install:
	pip install kaggle

download:
	kaggle datasets download --force -d deadskull7/fer2013

unzip:
	unzip fer2013.zip

transform:
	jupyter nbconvert --to notebook --inplace --execute transform_data.ipynb

code:
	jupyter nbconvert --to notebook --inplace --execute code.ipynb

evaluate:
	jupyter nbconvert --to notebook --inplace --execute evaluate.ipynb

run: install download unzip transform code evaluate

cam:
	python3 facial_detection/webcam.py
