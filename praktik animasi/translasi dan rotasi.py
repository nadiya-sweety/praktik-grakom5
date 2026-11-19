
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Membuat area animasi
fig, ax = plt.subplots(figsize=(8, 4))
ax.set_xlim(0, 10)
ax.set_ylim(0, 4)
ax.set_aspect('equal')
ax.axis('off')

# Judul animasi
ax.set_title(
    "Animasi Translasi dan Rotasi",
    fontsize=14,
    fontweight='bold'
)

# =========================
# OBJEK 1: BOLA (TRANSLASI)
# =========================
bola, = ax.plot([], [], 'o', color='red', markersize=20)

# =========================
# OBJEK 2: RODA (ROTASI)
# =========================
pusat_x = 2
pusat_y = 2
radius = 0.5

# Lingkaran luar roda
roda_luar = plt.Circle(
    (pusat_x, pusat_y),
    radius,
    fill=False,
    color='gray',
    linewidth=5
)
ax.add_patch(roda_luar)

# Garis jari-jari roda
jari_jari = []
jumlah_spoke = 6

for i in range(jumlah_spoke):
    garis, = ax.plot([], [], color='gray', linewidth=3)
    jari_jari.append(garis)

# =========================
# PARAMETER ANIMASI
# =========================
dx = 0.2                 # Kecepatan translasi
dtheta = 10               # Kecepatan rotasi (derajat)

# =========================
# FUNGSI UPDATE ANIMASI
# =========================
def update(frame):

    # Translasi bola ke kanan
    x = frame * dx
    bola.set_data([x], [2])

    # Rotasi roda
    theta = np.deg2rad(frame * dtheta)

    for i, garis in enumerate(jari_jari):
        sudut = (2 * np.pi * i / jumlah_spoke) + theta

        x_akhir = pusat_x + radius * np.cos(sudut)
        y_akhir = pusat_y + radius * np.sin(sudut)

        garis.set_data(
            [pusat_x, x_akhir],
            [pusat_y, y_akhir]
        )

    return (bola, *jari_jari)

# =========================
# MENJALANKAN ANIMASI
# =========================
ani = animation.FuncAnimation(
    fig,
    update,
    frames=100,
    interval=30,
    blit=True
)

plt.show()
