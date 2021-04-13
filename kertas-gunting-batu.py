import random
import os

main = "main"

def pilihanBot():
	return random.randint(1, 3)

def pilihan(pilihan):
	pilih = str(pilihan)

	if pilih == '1':
		return "kertas"
	elif pilih == '2':
		return "gunting"
	elif pilih == '3':
		return "batu"
	elif pilih == 'q':
		return True
	else:
		return False

def bermain(pilKamu, pilBot):
	if pilKamu == False:
		return "Maaf pilihan angka tidak ada di daftar!!!"
	elif pilKamu == True:
		print("Anda telah keluar dari permainan!!!")
		exit()

	if pilKamu == "kertas" and pilBot == "batu":
		return f"Selamat kamu menang kamu memilih {pilKamu} dan Bot memilih {pilBot}!!!"
	elif pilKamu == "gunting" and pilBot == "kertas":
		return f"Selamat kamu menang kamu memilih {pilKamu} dan Bot memilih {pilBot}!!!"
	elif pilKamu == "batu" and pilBot == "gunting":
		return f"Selamat kamu menang kamu memilih {pilKamu} dan Bot memilih {pilBot}!!!"
	elif pilKamu == pilBot:
		return f"kamu seri dengan pilihan yang sama dengan bot yaitu {pilKamu}!!!"
	else:
		return f"Maaf kamu kalah dengan pilihan {pilKamu} dan bot {pilBot}!!!"



text1 = """Selamat datang di game sederhana kertas, gunting, dan batu.

#Ketik 'p' untuk mulai bermain
#ketik 'q' untuk berhenti bermain
"""
os.system('cls')
print("="*60)
print(text1)
print("="*60)
play = input("Ketik : ")

if play == 'p':
	while main == 'main':
		text2 = """\nPilih angka sesuai pilihan:\n1. Kertas\n2. Gunting\n3. Batu
		"""
		print(text2)
		angka = input("Ketik : ")
		pilihM = pilihan(angka)
		pilBot = pilihan(pilihanBot())
		os.system('cls')
		print("="*60)
		print(bermain(pilihM, pilBot))
		print("="*60)
		print("#ketik 'q' untuk keluar dari permainan!!!")

