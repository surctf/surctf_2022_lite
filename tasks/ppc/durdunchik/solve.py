from pyzbar import pyzbar
import numpy as np
import pwn, cv2, sys

r = pwn.remote("localhost", 5000)

def lines_to_code(lines, BOX_SIZE=4):

    img = np.ndarray((29*BOX_SIZE, 29*BOX_SIZE), dtype="uint8")
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            for k in range(BOX_SIZE):
                img[i*BOX_SIZE + k][j*BOX_SIZE:(j+1)*BOX_SIZE] = 255 if c == "▩" else 0 if c == " " else None

    return img

try:
    while True:
        resp = r.recvuntil(b"Decoded:").decode('utf-8')
        resp = resp.replace("▩▩", "▩").replace("  ", " ")
        lines = resp.split("\n")[:-1]

        img = lines_to_code(lines)

        text = pyzbar.decode(img)[0].data
        print(text.decode("utf-8"), end="")
        r.sendline(text)
except EOFError as e:
    pass
finally:
    r.close()


