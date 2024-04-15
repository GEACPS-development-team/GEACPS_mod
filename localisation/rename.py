import os
import glob

before_word = "l_japanese"
after_word = "l_english"

files = glob.glob("localisation/english/*/*{}.yml".format(before_word))

for before_file in files:
	# テキスト内編集
	with open(before_file, encoding="utf_8_sig") as f:
		text_lines = f.read()
	text_lines = text_lines.replace(before_word + ":\n", after_word + ":\n")
	with open(before_file, mode = "w", encoding = "utf_8_sig") as f:
		f.write(text_lines)
	
	# ファイル名変更
	after_file = before_file.replace(before_word, after_word)
	os.rename(before_file, after_file)