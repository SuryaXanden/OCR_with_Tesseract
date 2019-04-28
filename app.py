import cv2, pytesseract, re, json, sys
try:
    input_image = sys.argv[1]
    if input_image:
        # Read the input image
        image = cv2.imread(input_image)

        OCR_extraction = pytesseract.image_to_string(image)
        cleaned_characters = []
        for char in OCR_extraction:
            # Replace funky characters
            test = re.sub(r"[^a-zA-Z0-9~`!@#\$%\^&\*\(\)_\-\+={\[\}\]\|\\:;\"'<,>\.\?\/\s\n\t]+", '' , char , re.MULTILINE)
        
            cleaned_characters.append(test)
        
            # Debugging purpose only
            # Comment in production
            # --------------------------------------------------------
            if char != test:
                print("'{}' is cleaned_characters as '{}'".format( char, test ))
            # --------------------------------------------------------
        
        cleaned_characters = "".join(cleaned_characters)

        print( json.dumps({"Output": cleaned_characters}) )
        
except Exception as e:
    print(e)