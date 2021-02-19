# %%
from OpenSSL import crypto
import tkinter
from tkinter import messagebox as tmb

CA_CRT = "cert.crt"
CA_KEY = "cert.key"


def create_self_signed_cert():
    try:
        KEY_FILE = "cert.key"
        CERT_FILE = "cert.crt"
        k = crypto.PKey()
        k.generate_key(crypto.TYPE_RSA, 1024)  # генерируем ключ

        cert = crypto.X509()  # генерируем сертификат
        cert.get_subject().C = "RU"  # указываем свои данные
        cert.get_subject().ST = "ChelReg"  # указываем свои данные
        cert.get_subject().L = "Kopeisk"  # указываем свои данные
        cert.get_subject().O = "lol"  # указываем свои данные
        cert.get_subject().OU = "kek"  # указываем свои данные
        cert.get_subject().CN = "cheburek.com"  # указываем свои данные
        cert.set_serial_number(1000)
        cert.gmtime_adj_notBefore(0)
        cert.gmtime_adj_notAfter(10 * 365 * 24 * 60 * 60)
        cert.set_issuer(cert.get_subject())
        cert.set_pubkey(k)
        cert.sign(k, "sha1")
        open(CERT_FILE, "wt").write(crypto.dump_certificate(crypto.FILETYPE_PEM, cert).decode())
        open(KEY_FILE, "wt").write(crypto.dump_privatekey(crypto.FILETYPE_PEM, k).decode())

        show_info("Self-signed certificate generated successfully")
    except:
        show_info("Something gone wrong")

def create_signed_cert():
    try:
        KEY_FILE = "cert2.key"
        CERT_FILE = "cert2.crt"
        with open(CA_CRT, "rb") as certfile:
            ca_cert = crypto.load_certificate(crypto.FILETYPE_PEM, certfile.read())
        with open(CA_KEY, "rb") as key:
            ca_key = crypto.load_privatekey(crypto.FILETYPE_PEM, key.read())
        k = crypto.PKey()
        k.generate_key(crypto.TYPE_RSA, 1024)  # генерируем ключ

        cert = crypto.X509()  # генерируем сертификат
        cert.get_subject().C = "RU"  # указываем свои данные
        cert.get_subject().ST = "ChelReg"  # указываем свои данные
        cert.get_subject().L = "Kopeisk"  # указываем свои данные
        cert.get_subject().O = "lol"  # указываем свои данные
        cert.get_subject().OU = "kek"  # указываем свои данные
        cert.get_subject().CN = "cheburek.com"  # указываем свои данные
        cert.set_serial_number(1000)
        cert.gmtime_adj_notBefore(0)
        cert.gmtime_adj_notAfter(10 * 365 * 24 * 60 * 60)
        cert.set_issuer(ca_cert.get_subject())
        cert.set_pubkey(k)
        cert.sign(ca_key, "sha1")
        open(CERT_FILE, "wt").write(crypto.dump_certificate(crypto.FILETYPE_PEM, cert).decode())
        open(KEY_FILE, "wt").write(crypto.dump_privatekey(crypto.FILETYPE_PEM, k).decode())

        show_info("Self-signed certificate generated successfully")
    except:
        show_info("Something gone wrong")

def show_info(message):
    tmb.showinfo("Info", message)


root = tkinter.Tk()
root.title("SSL generator")
root.geometry("300x125")
x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
root.wm_geometry("+%d+%d" % (x, y))
root.minsize(300, 125)
root.maxsize(300, 125)


button = tkinter.Button(text="Generate signed SSL certificate", command=create_signed_cert)
button.pack(expand=1, padx=10, pady=10)

button = tkinter.Button(text="Generate self signed SSL certificate", command=create_self_signed_cert)
button.pack(expand=1, padx=10, pady=10)

root.mainloop()