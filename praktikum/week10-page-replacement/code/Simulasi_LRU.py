reference = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
frame_size = 3

def lru_simulation(reference, frame_size):
    frames = []
    page_fault = 0

    print("=== SIMULASI LRU ===")
    print("Page\tFrames\t\tStatus")

    for page in reference:
        if page in frames:
            status = "Hit"
            frames.remove(page)
            frames.append(page)
        else:
            status = "Fault"
            page_fault += 1
            if len(frames) < frame_size:
                frames.append(page)
            else:
                frames.pop(0)
                frames.append(page)

        print(f"{page}\t{frames}\t{status}")

    print("\nTotal Page Fault LRU:", page_fault)

lru_simulation(reference, frame_size)
