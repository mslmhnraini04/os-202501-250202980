# ============================
# DEADLOCK DETECTION PROGRAM
# ============================

# Data proses dan resource
processes = ["P1", "P2", "P3"]

allocation = {
    "P1": "R1",
    "P2": "R2",
    "P3": "R3"
}

request = {
    "P1": "R2",
    "P2": "R3",
    "P3": "R1"
}

# Semua resource sedang dipakai (tidak ada yang available)
available = []

# Status proses
deadlock_status = {p: True for p in processes}

# Cek apakah ada proses yang bisa jalan
for p in processes:
    if request[p] in available:
        deadlock_status[p] = False

# Tampilkan hasil per proses
print("Proses Deadlock yang Terdeteksi :")
for p in processes:
    if deadlock_status[p]:
        print(f"{p} : Deadlock")
    else:
        print(f"{p} : Tidak Deadlock")

# Kesimpulan sistem
if all(deadlock_status.values()):
    print("\nSystem is in DEADLOCK condition")
else:
    print("\nSystem is SAFE")
