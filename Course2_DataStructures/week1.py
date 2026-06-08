text = "X-DSPAM-Confidence:    0.8475"
ipos= text.find('0')
num=text[ipos:]
print(float(num))
