import qrcode 


#Taking UPI ID As a input 

upi_id = input("Enter your UPI ID = ")

#upi://pay?pa=UPI_ID&pn=NAME&am=Amount&Cu=CURRENCY&tn=MESSAGE

#Defining the payment URL based on the UPI ID and the payment app
#You can modify these URLs based on the payment apps you want to support 

phonepe_url = f'upi://pay?pa{upi_id}&pn=Recipient%20Name&mc=1234'
paytm_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
google_ulr = f'upi://pay?pa={upi_id}&pn=REcipient%20NAme&mc=1234'

#Create QR codes for each payment app
phonepe_qr = qrcode.make(phonepe_url)
paytm_qr = qrcode.make(paytm_url)
google_qr = qrcode.make(google_ulr)

#Save the QR code ot image file(optional)
phonepe_qr.save('phonepe.png')
paytm_url.save('paytm.png')
google_qr.save('gpay.png')

#Display the QR codes (you may to install PIL/Pillow Library)

phonepe_qr.show()
paytm_qr.show()
google_qr.show()

# /abhi kaam baaaki h kyuki pip ki mkc 
