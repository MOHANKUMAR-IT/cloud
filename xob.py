import dropbox
dropbox_access_token= "sl.BJhCMGP6zwBaH8kHQgkXJqKovq2OACJB5hqvO5g53roAnYQp8BDRl3qASfR3QzlPXMfCabxxOtgvJ094DUKIR1t2vNMw7s1qxUiIIfmo_2wne60XwdcWIYO0fiXlDDBCbXYpB0Bi_EbW"
dropbox_path= "/sample.txt"
computer_path=r"E:\dropbox code\sample.txt"
client = dropbox.Dropbox(dropbox_access_token)
print("[SUCCESS] dropbox account linked")
client.files_upload(open(computer_path, "rb").read(), dropbox_path)
print("[UPLOADED] {}".format(computer_path))
metadata, f = client.files_download('/sample.txt')
out = open("sample_download.txt", 'wb')
out.write(f.content)
out.close()
print("[SUCCESS] downloaded")
