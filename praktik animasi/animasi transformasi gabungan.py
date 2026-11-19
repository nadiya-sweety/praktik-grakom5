
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from matplotlib.patches import Polygon

# ==================================
# 1. MEMBUAT AREA ANIMASI
# ==================================
fig, ax = plt.subplots(figsize=(9, 6))

ax.set_xlim(-1, 7)
ax.set_ylim(-1, 5)
ax.set_aspect('equal')
ax.grid(True, alpha=0.3)
ax.set_title(
    "Animasi Transformasi Gabungan",
    fontsize=14,
    fontweight='bold'
)

# ==================================
# 2. MEMBUAT OBJEK RUMAH
# ==================================

# Dinding rumah
dinding = np.array([
    [0, 0],
    [2, 0],
    [2, 1.2],
    [0, 1.2]
])

# Atap rumah
atap = np.array([
    [-0.15, 1.2],
    [1, 2.2],
    [2.15, 1.2]
])

# Pintu rumah
pintu = np.array([
    [0.8, 0],
    [1.2, 0],
    [1.2, 0.8],
    [0.8, 0.8]
])

# Jendela kiri
jendela1 = np.array([
    [0.2, 0.6],
    [0.65, 0.6],
    [0.65, 1],
    [0.2, 1]
])

# Jendela kanan
jendela2 = np.array([
    [1.35, 0.6],
    [1.8, 0.6],
    [1.8, 1],
    [1.35, 1]
])

# Menggabungkan bagian-bagian rumah
bagian_rumah = [
    dinding, atap, pintu, jendela1, jendela2
]

# ==================================
# 3. MEMBUAT GAMBAR RUMAH
# ==================================

warna = [
    'pink', 'red', 'blue',
    'yellow', 'yellow'
]

objek = []

for titik, warna_objek in zip(bagian_rumah, warna):
    gambar = Polygon(
        titik,
        closed=True,
        facecolor=warna_objek,
        edgecolor='black',
        linewidth=2
    )
    ax.add_patch(gambar)
    objek.append(gambar)

# ==================================
# 4. FUNGSI TRANSFORMASI GABUNGAN
# ==================================


def transform(points, s, theta, dx, dy):

    # Matriks Scaling
    S = np.array([
        [s, 0, 0],
        [0, s, 0],
        [0, 0, 1]
    ])

    # Matriks Rotasi
    R = np.array([
        [np.cos(theta), -np.sin(theta), 0],
        [np.sin(theta), np.cos(theta), 0],
        [0, 0, 1]
    ])

    # Matriks Translasi
    T = np.array([
        [1, 0, dx],
        [0, 1, dy],
        [0, 0, 1]
    ])

    # Mengubah koordinat menjadi homogen
    P_h = np.hstack((
        points,
        np.ones((points.shape[0], 1))
    ))

    # Urutan transformasi: Rotasi, Translasi, Scaling
    P_new = (S @ T @ R @ P_h.T).T

    return P_new[:, :2]


# ==================================
# 5. FUNGSI UPDATE ANIMASI
# ==================================

def update(frame):

    # Tahap 1: Scaling (frame 0-20)
    s = 1 - 0.2 * min(frame, 20) / 20

    # Tahap 2: Rotasi 30 derajat (frame 20-40)
    theta = np.deg2rad(
        30 * max(0, min(frame - 20, 20)) / 20
    )

    # Tahap 3: Translasi (+3, +1) (frame 40-60)
    dx = 3 * max(0, min(frame - 40, 20)) / 20
    dy = 1 * max(0, min(frame - 40, 20)) / 20

    # Memperbarui setiap bagian rumah
    for gambar, titik_awal in zip(objek, bagian_rumah):

        titik_baru = transform(
            titik_awal, s, theta, dx, dy
        )

        gambar.set_xy(titik_baru)

    return objek

# ==================================
# 6. MENJALANKAN ANIMASI
# ==================================

ani = animation.FuncAnimation(
    fig,
    update,
    frames=61,
    interval=50,
    blit=True,
    repeat=True
)

plt.show()
