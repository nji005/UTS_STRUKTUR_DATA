import csv

class Paper:
    def __init__(self, sumberDatabase, fokusKataKunci, title, year, author, abstractText, conclusion, link):
        self.sumberDatabase = sumberDatabase
        self.fokusKataKunci = fokusKataKunci
        self.title = title
        self.year = year
        self.author = author
        self.abstractText = abstractText
        self.conclusion = conclusion
        self.link = link

def display_paper(p):
    print("\n===========================================================")
    print(f"Sumber Database  : {p.sumberDatabase}")
    print(f"Fokus Kata Kunci : {p.fokusKataKunci}")
    print(f"Judul Paper      : {p.title}")
    print(f"Tahun Terbit     : {p.year}")
    print(f"Nama Penulis     : {p.author}")
    print(f"Abstrak          : {p.abstractText}")
    print(f"Kesimpulan       : {p.conclusion}")
    print(f"Link Paper       : {p.link}")
    print("===========================================================")

# Linear Search
def linear_search(papers, keyword, key_func):
    return [p for p in papers if keyword in key_func(p).lower()]

# Binary Search
def binary_search(papers, keyword, key_func):
    keyword = keyword.lower()
    left, right = 0, len(papers) - 1
    result = []

    while left <= right:
        mid = (left + right) // 2
        mid_val = key_func(papers[mid]).lower()

        if keyword == mid_val:
            result.append(papers[mid])
            i = mid - 1
            while i >= 0 and key_func(papers[i]).lower() == keyword:
                result.insert(0, papers[i])
                i -= 1
            i = mid + 1
            while i < len(papers) and key_func(papers[i]).lower() == keyword:
                result.append(papers[i])
                i += 1
            break
        elif keyword < mid_val:
            right = mid - 1
        else:
            left = mid + 1

    return result

def main():
    papers = []
    try:
        with open("Struktur_Data_Dataset_Kelas_A_B_C - Sheet1.csv", "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            header = next(reader)

            for row in reader:
                if len(row) < 11:
                    continue
                row = [item.strip() for item in row]
                sumber, fokus, title, year, author, abstrak, conclusion, link = row[3:11]
                paper = Paper(sumber, fokus, title, year, author, abstrak, conclusion, link)
                papers.append(paper)
        print(f"Jumlah data yang berhasil dimuat: {len(papers)}")

    except FileNotFoundError:
        print("File tidak ditemukan.")
        return
    except Exception as e:
        print(f"Error saat membaca file: {e}")
        return

    while True:
        print("\n=== Pilih Metode Pencarian ===")
        print("1. Linear Search")
        print("2. Binary Search")
        metode = input("Pilih metode (1/2): ").strip()
        if metode in ["1", "2"]:
            break
        print("Pilihan tidak valid. Silakan coba lagi.")

    papers_sorted = {
        "title": sorted(papers, key=lambda p: p.title.lower()),
        "year": sorted(papers, key=lambda p: p.year),
        "author": sorted(papers, key=lambda p: p.author.lower()),
    }

    while True:
        print("\n=== Menu Pencarian Jurnal ===")
        print("1. Cari berdasarkan Judul Paper")
        print("2. Cari berdasarkan Tahun Terbit")
        print("3. Cari berdasarkan Nama Penulis")
        print("4. Keluar")
        pilihan = input("Pilih opsi (1-4): ").strip()
        if pilihan == "4":
            print("Program selesai.")
            break
        keyword = input("Masukkan kata kunci pencarian: ").strip().lower()
        hasil = []
        if pilihan == "1":
            key_func = lambda p: p.title
            key_name = "title"
        elif pilihan == "2":
            key_func = lambda p: p.year
            key_name = "year"
        elif pilihan == "3":
            key_func = lambda p: p.author
            key_name = "author"
        else:
            print("Pilihan tidak valid.")
            continue

        if metode == "1":
            hasil = linear_search(papers, keyword, key_func)
        else:
            hasil = binary_search(papers_sorted[key_name], keyword, key_func)

        if not hasil:
            print("\nTidak ditemukan data yang sesuai.")
        else:
            print(f"\nDitemukan {len(hasil)} hasil:")
            for paper in hasil:
                display_paper(paper)

if __name__ == "__main__":
    main()
