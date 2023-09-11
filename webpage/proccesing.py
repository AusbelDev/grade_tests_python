from PIL import Image
from pprint import pprint
import os
import pytesseract
import language_tool_python


basedir = os.path.abspath(os.path.dirname(__file__))

tool = language_tool_python.LanguageTool("en-US")

img = Image.open(
    os.path.join(
        "C:/Users/kmarx/source/repos/grade_tests_python/webpage/static/images/image.jpeg"
    )
)

img = img.convert("RGBA")

text = pytesseract.image_to_string(img, lang="eng")


filtered_text = [t for t in text.split("\n") if t.strip() != ""]

for line in filtered_text:
    matches = tool.check(line)
    print(line)
    if len(matches) > 0:
        print(matches[0].ruleId, matches[0].replacements)
        print("\n")

tool.close()
