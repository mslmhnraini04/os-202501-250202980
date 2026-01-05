reference = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
frame_size = 3

def fifo_simulation(reference, frame_size):
    frames = []
    page_fault = 0

    print("=== SIMULASI FIFO ===")
    print("Page\tFrames\t\tStatus")

    for page in reference:
        if page in frames:
            status = "Hit"
        else:
            status = "Fault"
            page_fault += 1
            if len(frames) < frame_size:
                frames.append(page)
            else:
                frames.pop(0)
                frames.append(page)

        print(f"{page}\t{frames}\t{status}")

    print("\nTotal Page Fault FIFO:", page_fault)

fifo_simulation(reference, frame_size)
