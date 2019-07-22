## Introduction

Click-by-Mouse Annotator
    A simple single-label annotator
    Only one operation(Click by Mouse) needed to annotate an image 

## Dependence

- `Python3.7`
- `PyQt5`

## Usage

install PyQt5
```bash
pip install PyQt5
```

# Step1

Run the script
```bash
python label_tool_button.py
```
# Step2

open the directory under the pictures whichs you want to label 

![Image text](./README_img/step2.png)

# Step3

move your mouse on the reference picture which you want to choice or move sliber to change value of specified label while the reference picture will change under the sliber value. 
![Image text](./README_img/load_img.png)

# Step4
click your mouse on the reference picture which you want to choice and then it is automatical save the value ,output the json under same directory on the pictures with the same filename.
![Image text](./README_img/step4.png)

## Function

- annotate images,  and save annotation file(`.json`) in the same directory of image
- click the reference picture, to annotate an image and switch to next image

|   HotKey   |   Description  |
| ---------- | -------------- |
| `Ctrl + O` | Open Image Directory |
| `Ctrl + Q` | Exit |
| `A or 4` | Switch to the previous image |
| `D or 6` | Switch to the next image     |
| `W or 8` | discard this image within -1 invalid value |




