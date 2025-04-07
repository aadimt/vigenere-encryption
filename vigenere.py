def vigenere_encrypt(plaintext, key):
    plaintext = ''.join(filter(str.isalpha, plaintext.upper()))
    key = ''.join(filter(str.isalpha, key.upper()))
    key_repeat = (key * (len(plaintext) // len(key) + 1))[:len(plaintext)]
    
    ciphertext = ""
    for p, k in zip(plaintext, key_repeat):
        c = chr((ord(p) - ord('A') + ord(k) - ord('A')) % 26 + ord('A'))
        ciphertext += c
    return ciphertext

plaintext = """Di sebuah gedung konser, suara alat musik dipersiapkan sebelum pertunjukan dimulai. Para
musisi mengenakan pakaian resmi, memegang instrumen mereka dengan penuh keahlian.
Penonton mulai memenuhi kursi mereka, berbincang pelan sambil menunggu pertunjukan.
Lampu-lampu panggung mulai redup, menandakan konser akan segera dimulai. Sang konduktor
naik ke podium, mengangkat tongkatnya dengan penuh wibawa. Begitu tongkatnya bergerak,
suara harmoni memenuhi ruangan, menciptakan melodi indah. Setiap nada yang dimainkan
membawa emosi, menghipnotis semua yang hadir dalam pertunjukan musik klasik ini membuat
jiwa terasa tenang dan berayun."""

key = "Adi Muhamad Taufik"
ciphertext = vigenere_encrypt(plaintext, key)
print("Ciphertext:")
print(ciphertext)
