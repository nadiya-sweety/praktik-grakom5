
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Circle, Polygon

# ==========================================
# 1. MEMBUAT AREA DAN LATAR BELAKANG
# ==========================================

fig, ax = plt.subplots(figsize=(10, 5.5))

ax.set_xlim(0, 10)
ax.set_ylim(0, 5.5)
ax.set_aspect('equal')
ax.axis('off')
ax.set_facecolor('#BDEEFF')

fig.patch.set_facecolor('#BDEEFF')

# Langit
ax.add_patch(plt.Rectangle(
    (0, 0), 10, 5.5,
    color='#BDEEFF'
))

# Matahari
ax.add_patch(Circle(
    (8.8, 4.7), 0.4,
    color='#FFD84D'
))

# Bukit
ax.add_patch(Circle(
    (1.5, 0.4), 2,
    color='#91D98B'
))

ax.add_patch(Circle(
    (8, 0.3), 2.5,
    color='#A5E69A'
))

# Tanah
ax.add_patch(plt.Rectangle(
    (0, 0), 10, 0.55,
    color='#72C96A'
))

# Awan
def buat_awan(x, y):
    for dx, dy, r in [
        (0, 0, 0.22),
        (0.25, 0.08, 0.28),
        (0.52, 0, 0.22)
    ]:
        ax.add_patch(Circle(
            (x + dx, y + dy),
            r,
            color='white',
            zorder=1
        ))

buat_awan(1, 4.5)
buat_awan(5, 4.8)

# Bunga di taman
for x in [0.5, 2, 4, 6, 8, 9.5]:
    ax.add_patch(Circle(
        (x, 0.65), 0.07,
        color='#FF70B5'
    ))
    ax.add_patch(Circle(
        (x, 0.65), 0.025,
        color='#FFE45E'
    ))

# ==========================================
# 2. FUNGSI MEMBUAT BAGIAN KARAKTER
# ==========================================

polygons = []
circles = []

def buat_polygon(points, color, zorder=5):
    obj = Polygon(
        points,
        closed=True,
        facecolor=color,
        edgecolor='#663D4D',
        linewidth=1.3,
        zorder=zorder
    )
    ax.add_patch(obj)
    polygons.append((obj, np.array(points)))

    return obj


def buat_lingkaran(center, radius, color, zorder=5):
    obj = Circle(
        center,
        radius,
        facecolor=color,
        edgecolor='#663D4D',
        linewidth=1,
        zorder=zorder
    )
    ax.add_patch(obj)
    circles.append((obj, np.array(center), radius))

    return obj


# ==========================================
# 3. MEMBUAT KARAKTER CEWEK PINK
# ==========================================

# Warna karakter
pink = '#FF78B7'
dark_pink = '#E94F94'
skin = '#FFD0B5'
hair = '#49302E'
shoes = '#F04491'

# Rambut belakang
buat_lingkaran((-0.08, 2.55), 0.48, hair)

# Kuncir rambut
buat_lingkaran((-0.43, 2.65), 0.20, hair)

# Badan / gaun pink
buat_polygon([
    (-0.23, 2.12),
    (0.23, 2.12),
    (0.46, 1.15),
    (-0.46, 1.15)
], pink)

# Kerah gaun
buat_polygon([
    (-0.13, 2.16),
    (0, 2.03),
    (0.13, 2.16)
], 'white')

# Hiasan pita di pinggang
buat_polygon([
    (-0.38, 1.55),
    (0.38, 1.55),
    (0.34, 1.46),
    (-0.34, 1.46)
], dark_pink)

# Kepala
buat_lingkaran((0, 2.58), 0.37, skin)

# Rambut bagian atas
buat_polygon([
    (-0.37, 2.63),
    (-0.35, 2.88),
    (-0.17, 3.02),
    (0.10, 3.04),
    (0.34, 2.86),
    (0.37, 2.67),
    (0.22, 2.78),
    (0.05, 2.83),
    (-0.13, 2.78),
    (-0.28, 2.68)
], hair)

# Pita rambut
buat_polygon([
    (-0.40, 2.90),
    (-0.61, 3.06),
    (-0.57, 2.81),
    (-0.40, 2.82)
], pink)

buat_polygon([
    (-0.40, 2.90),
    (-0.22, 3.08),
    (-0.25, 2.82),
    (-0.40, 2.82)
], dark_pink)

buat_lingkaran((-0.40, 2.90), 0.07, '#FFDAE9')

# Mata
buat_lingkaran((-0.13, 2.61), 0.035, hair)
buat_lingkaran((0.13, 2.61), 0.035, hair)

# Pipi
buat_lingkaran((-0.23, 2.49), 0.055, '#FF9EAA')
buat_lingkaran((0.23, 2.49), 0.055, '#FF9EAA')

# ==========================================
# 4. MEMBUAT TANGAN DAN KAKI
# ==========================================

def buat_garis(color, width, zorder=4):
    line, = ax.plot(
        [], [],
        color=color,
        linewidth=width,
        solid_capstyle='round',
        zorder=zorder
    )
    return line


# Tangan
tangan_kiri = buat_garis(skin, 10)
tangan_kanan = buat_garis(skin, 10)

# Lengan baju
lengan_kiri = buat_garis(pink, 13)
lengan_kanan = buat_garis(pink, 13)

# Kaki
kaki_kiri = buat_garis(skin, 12)
kaki_kanan = buat_garis(skin, 12)

# Sepatu
sepatu_kiri = buat_garis(shoes, 10)
sepatu_kanan = buat_garis(shoes, 10)

# ==========================================
# 5. FUNGSI TRANSFORMASI GEOMETRI
# ==========================================

def transformasi(points, x, y, scale, angle):

    # Matriks scaling
    S = np.array([
        [scale, 0],
        [0, scale]
    ])

    # Matriks rotasi
    R = np.array([
        [np.cos(angle), -np.sin(angle)],
        [np.sin(angle), np.cos(angle)]
    ])

    # Transformasi gabungan
    hasil = (R @ S @ points.T).T

    # Translasi
    hasil[:, 0] += x
    hasil[:, 1] += y

    return hasil


# ==========================================
# 6. FUNGSI MENGGERAKKAN KARAKTER
# ==========================================

def update(frame):

    # Sudut gerakan berjalan
    phase = frame * 0.13

    # TRANSFORMASI 1: TRANSLASI
    x = 0.8 + (frame / 299) * 8.2

    # Gerakan naik turun
    bounce = abs(np.sin(phase * 2)) * 0.07

    # TRANSFORMASI 2: SCALING
    scale = 1 + 0.025 * np.sin(phase * 2)

    # TRANSFORMASI 3: ROTASI
    angle = 0.035 * np.sin(phase)

    # Memperbarui semua polygon
    for obj, original in polygons:
        hasil = transformasi(
            original.copy(),
            x, bounce, scale, angle
        )
        obj.set_xy(hasil)

    # Memperbarui semua lingkaran
    for obj, center, radius in circles:
        hasil = transformasi(
            center.reshape(1, 2).copy(),
            x, bounce, scale, angle
        )

        obj.center = hasil[0]
        obj.radius = radius * scale

    # Gerakan kaki bergantian
    swing = np.sin(phase) * 0.42

    # Titik pangkal kaki
    hip_left = np.array([-0.16, 1.18])
    hip_right = np.array([0.16, 1.18])

    # Gerakan kaki
    foot_left = hip_left + np.array([
        np.sin(phase) * 0.40,
        -0.88 + abs(np.sin(phase)) * 0.15
    ])

    foot_right = hip_right + np.array([
        -np.sin(phase) * 0.40,
        -0.88 + abs(np.sin(phase)) * 0.15
    ])

    # Gerakan tangan berlawanan dengan kaki
    shoulder_left = np.array([-0.22, 2.02])
    shoulder_right = np.array([0.22, 2.02])

    hand_left = shoulder_left + np.array([
        np.sin(phase + np.pi) * 0.35,
        -0.48
    ])

    hand_right = shoulder_right + np.array([
        np.sin(phase) * 0.35,
        -0.48
    ])

    # Fungsi mengubah garis menjadi koordinat layar
    def gerakkan_garis(line, p1, p2):
        points = np.array([p1, p2])
        result = transformasi(
            points, x, bounce, scale, angle
        )
        line.set_data(result[:, 0], result[:, 1])

    # Menggerakkan lengan dan tangan
    gerakkan_garis(
        lengan_kiri, shoulder_left,
        (shoulder_left + hand_left) / 2
    )
    gerakkan_garis(
        lengan_kanan, shoulder_right,
        (shoulder_right + hand_right) / 2
    )

    gerakkan_garis(
        tangan_kiri,
        (shoulder_left + hand_left) / 2,
        hand_left
    )
    gerakkan_garis(
        tangan_kanan,
        (shoulder_right + hand_right) / 2,
        hand_right
    )

    # Menggerakkan kaki
    gerakkan_garis(kaki_kiri, hip_left, foot_left)
    gerakkan_garis(kaki_kanan, hip_right, foot_right)

    # Sepatu mengikuti gerakan kaki
    gerakkan_garis(
        sepatu_kiri,
        foot_left,
        foot_left + np.array([0.23, -0.02])
    )
    gerakkan_garis(
        sepatu_kanan,
        foot_right,
        foot_right + np.array([0.23, -0.02])
    )

    return (
        [obj for obj, _ in polygons]
        + [obj for obj, _, _ in circles]
        + [
            tangan_kiri, tangan_kanan,
            lengan_kiri, lengan_kanan,
            kaki_kiri, kaki_kanan,
            sepatu_kiri, sepatu_kanan
        ]
    )


# ==========================================
# 7. JUDUL ANIMASI
# ==========================================

ax.text(
    5, 5.25,
    "MY LITTLE PINK WORLD",
    fontsize=17,
    fontweight='bold',
    color='#E94F94',
    ha='center'
)

ax.text(
    5, 4.95,
    "A Cute Girl Walking in the Garden",
    fontsize=9,
    color='#80516B',
    ha='center'
)

# ==========================================
# 8. MENJALANKAN ANIMASI
# ==========================================

ani = animation.FuncAnimation(
    fig,
    update,
    frames=300,
    interval=1000/30,
    blit=False,
    repeat=True
)

# Simpan hasil dalam format GIF
ani.save(
    "hasil_animasi_cewek_pink.gif",
    writer="pillow",
    fps=30
)

plt.show()
