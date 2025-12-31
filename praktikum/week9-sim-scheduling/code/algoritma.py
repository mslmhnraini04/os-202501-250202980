import csv
import os

print("=== SIMULASI CPU SCHEDULING FCFS ===\n")

# Path otomatis (dataset.csv satu folder dengan file python)
base_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_dir, "dataset.csv")

print("Membaca file:", file_path, "\n")

# Membaca data dari CSV
processes = []
with open(file_path, "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        processes.append({
            "process": row["Process"],
            "arrival": int(row["ArrivalTime"]),
            "burst": int(row["BurstTime"])
        })

# Mengurutkan proses berdasarkan Arrival Time (FCFS)
processes.sort(key=lambda p: p["arrival"])

time = 0
total_waiting = 0
total_turnaround = 0

print("Proses | Arrival | Burst | Waiting | Turnaround")
print("------------------------------------------------")

# Perhitungan FCFS
for proc in processes:

    if time < proc["arrival"]:
        time = proc["arrival"]

    waiting_time = time - proc["arrival"]
    turnaround_time = waiting_time + proc["burst"]

    total_waiting += waiting_time
    total_turnaround += turnaround_time

    print(f"{proc['process']:>6} | {proc['arrival']:>7} | {proc['burst']:>5} | {waiting_time:>7} | {turnaround_time:>10}")

    time += proc["burst"]

# Menampilkan rata-rata
jumlah = len(processes)
print("\nRata-rata Waiting Time    :", round(total_waiting / jumlah, 2))
print("Rata-rata Turnaround Time :", round(total_turnaround / jumlah, 2))
