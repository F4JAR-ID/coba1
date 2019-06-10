import os, sys

runntxt(GG+"[!] Silahkan Masukkan Username & Password Anda")

runntxt(GG+"[•] Atau silahkan Hubungi Akun Fb Sampah Masyarakat")

username = 'Fajar'      

password = 'Ganteng123'



def restart():

	ngulang = sys.executable

	os.execl(ngulang, ngulang, *sys.argv)



def main():

	uname = raw_input("username : ")

	if uname == username:

		pwd = raw_input("password : ")



		if pwd == password:

			
runntxt(GL+ "Alhmdllh sudah masuk juga..")

			sys.exit()



		else:

			print GL+" Maaf Masukkan password Anda salah... "

			print RR+" Silahkan segera log-in kembali...!!"

			restart()



	else:

		print GL+" Maaf Masukkan Username Anda salah..."

		print RR+" Silahkan segera log-in kembali...!!"

		restart()



try:

	main()

except KeyboardInterrupt:

	os.system('clear')

restart()
