
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Circle, Ellipse, Polygon, Rectangle

# ==================================================
# 1. AREA ANIMASI
# ==================================================

fig, ax = plt.subplots(figsize=(12, 6.5))
fig.patch.set_facecolor('#DDF4FF')

ax.set_xlim(0, 10)
ax.set_ylim(0, 5.5)
ax.set_aspect('equal')
ax.axis('off')

# ==================================================
# 2. BACKGROUND TAMAN
# ==================================================

ax.add_patch(Rectangle((0, 0), 10, 5.5,
                       color='#BDEAFF'))

# Matahari
ax.add_patch(Circle((8.7, 4.6), 0.4,
                    color='#FFE078'))

for angle in np.linspace(0, 2*np.pi, 12):
    x1 = 8.7 + 0.48*np.cos(angle)
    y1 = 4.6 + 0.48*np.sin(angle)
    x2 = 8.7 + 0.60*np.cos(angle)
    y2 = 4.6 + 0.60*np.sin(angle)
    ax.plot([x1, x2], [y1, y2],
            color='#FFD45E', linewidth=2)

# Awan
def buat_awan(x, y, s=1):
    for dx, dy, r in [
        (0, 0, 0.18),
        (0.2, 0.08, 0.23),
        (0.43, 0, 0.18),
        (0.22, -0.06, 0.19)
    ]:
        ax.add_patch(Circle(
            (x+dx*s, y+dy*s), r*s,
            color='white', zorder=1
        ))

buat_awan(0.7, 4.5)
buat_awan(4.5, 4.8)
buat_awan(7.1, 3.9, 0.7)

# Bukit
ax.add_patch(Ellipse(
    (1.2, 0.35), 4.5, 3.2,
    color='#A1DF9B', zorder=1
))

ax.add_patch(Ellipse(
    (9, 0.35), 4.5, 3.2,
    color='#A1DF9B', zorder=1
))

# Tanah
ax.add_patch(Rectangle(
    (0, 0), 10, 0.65,
    color='#76CE79', zorder=2
))

# Jalan setapak
ax.add_patch(Rectangle(
    (0, 0), 10, 0.20,
    color='#F4D9BB', zorder=3
))

# Pohon
def buat_pohon(x):
    ax.add_patch(Rectangle(
        (x-0.08, 0.65), 0.16, 0.65,
        color='#986344', zorder=3
    ))

    for cx, cy, r in [
        (x, 1.45, 0.38),
        (x-0.23, 1.30, 0.27),
        (x+0.23, 1.30, 0.27)
    ]:
        ax.add_patch(Circle(
            (cx, cy), r,
            color='#68B879', zorder=3
        ))

buat_pohon(0.7)
buat_pohon(9.3)

# Bunga
def buat_bunga(x, y, color):
    for a in np.linspace(0, 2*np.pi, 5, endpoint=False):
        ax.add_patch(Circle(
            (x+0.09*np.cos(a), y+0.09*np.sin(a)),
            0.075, color=color, zorder=4
        ))

    ax.add_patch(Circle(
        (x, y), 0.04,
        color='#FFE16A', zorder=5
    ))

for x, c in [
    (0.3, '#FF82B4'), (1.7, 'white'),
    (2.6, '#FFD46C'), (3.5, '#FF82B4'),
    (5.0, 'white'), (6.2, '#FFD46C'),
    (7.6, '#FF82B4'), (8.7, 'white'),
    (9.7, '#FFD46C')
]:
    buat_bunga(x, 0.72, c)

# ==================================================
# 3. DEKORASI KUPU-KUPU
# ==================================================

for x, y, c in [
    (2.0, 3.5, '#FF80B5'),
    (7.9, 3.1, '#A98CF5'),
    (5.8, 4.0, '#FFB45D')
]:
    ax.add_patch(Ellipse(
        (x-0.1, y), 0.18, 0.12,
        angle=35, color=c, zorder=5
    ))
    ax.add_patch(Ellipse(
        (x+0.1, y), 0.18, 0.12,
        angle=-35, color=c, zorder=5
    ))
    ax.plot([x, x], [y-0.1, y+0.1],
            color='#60404D', linewidth=1.5)

# ==================================================
# 4. FUNGSI MEMBUAT KARAKTER
# ==================================================

polygons = []
ellipses = []

def polygon(points, color, z=10):
    obj = Polygon(
        points,
        closed=True,
        facecolor=color,
        edgecolor='#68424F',
        linewidth=1.2,
        zorder=z
    )
    ax.add_patch(obj)
    polygons.append((obj, np.array(points, dtype=float)))
    return obj

def ellipse(center, width, height, color,
            angle=0, z=10, edge='#68424F'):

    obj = Ellipse(
        center,
        width, height,
        angle=angle,
        facecolor=color,
        edgecolor=edge,
        linewidth=1,
        zorder=z
    )
    ax.add_patch(obj)

    ellipses.append((
        obj, np.array(center, dtype=float),
        width, height, angle
    ))
    return obj

def line(color, width, z=15):
    obj, = ax.plot(
        [], [],
        color=color,
        linewidth=width,
        solid_capstyle='round',
        zorder=z
    )
    return obj

# ==================================================
# 5. RAMBUT BELAKANG
# ==================================================

ellipse((0, 2.85), 1.20, 1.40, '#57372F', z=8)
ellipse((-0.43, 2.35), 0.38, 1.35,
        '#57372F', angle=8, z=8)
ellipse((0.43, 2.35), 0.38, 1.35,
        '#57372F', angle=-8, z=8)

# ==================================================
# 6. TUBUH DAN GAUN PINK
# ==================================================

ellipse((0, 2.20), 0.30, 0.34,
        '#FFD0B8', z=10)

# Badan
polygon([
    (-0.36, 2.25), (0.36, 2.25),
    (0.48, 1.70), (-0.48, 1.70)
], '#FF91C2', 11)

# Rok
polygon([
    (-0.45, 1.78), (0.45, 1.78),
    (0.72, 0.95), (-0.72, 0.95)
], '#FF78B4', 12)

# Lapisan bawah rok
polygon([
    (-0.64, 1.05), (0.64, 1.05),
    (0.72, 0.95), (-0.72, 0.95)
], '#F45D9E', 13)

# Kerah
polygon([
    (-0.17, 2.25), (0, 2.06),
    (0.17, 2.25)
], 'white', 14)

# Pita pinggang
polygon([
    (-0.39, 1.78), (0.39, 1.78),
    (0.36, 1.69), (-0.36, 1.69)
], '#E94F94', 14)

# Pita tengah
polygon([
    (-0.04, 1.76), (-0.20, 1.87),
    (-0.18, 1.67)
], '#FFB5D2', 15)

polygon([
    (0.04, 1.76), (0.20, 1.87),
    (0.18, 1.67)
], '#FFB5D2', 15)

ellipse((0, 1.76), 0.10, 0.10,
        '#FFE4F0', z=16)

# Hiasan gaun
for x, y in [(-0.35, 1.35), (0.35, 1.35), (0, 1.22)]:
    ellipse((x, y), 0.10, 0.10,
            '#FFE8F1', z=15, edge='none')

# ==================================================
# 7. KEPALA DAN WAJAH
# ==================================================

# Telinga
ellipse((-0.49, 2.92), 0.20, 0.26,
        '#FFD0B8', z=10)
ellipse((0.49, 2.92), 0.20, 0.26,
        '#FFD0B8', z=10)

# Wajah
ellipse((0, 2.96), 0.94, 1.08,
        '#FFD5BF', z=11)

# Rambut atas
polygon([
    (-0.48, 3.00), (-0.52, 3.43),
    (-0.30, 3.66), (0.10, 3.73),
    (0.43, 3.51), (0.50, 3.12),
    (0.25, 3.34), (0.04, 3.30),
    (-0.18, 3.39), (-0.35, 3.20)
], '#57372F', 12)

# Poni
polygon([
    (-0.43, 3.35), (-0.30, 3.50),
    (-0.10, 3.46), (0.06, 3.32),
    (0.28, 3.40), (0.42, 3.30),
    (0.35, 3.13), (0.15, 3.23),
    (-0.05, 3.20), (-0.24, 3.11)
], '#694238', 13)

# Mata
for x in [-0.19, 0.19]:
    ellipse((x, 2.99), 0.105, 0.15,
            '#49302F', z=14)
    ellipse((x-0.02, 3.04), 0.035, 0.045,
            'white', z=15, edge='none')

# Bulu mata
for x, d in [(-0.19, -1), (0.19, 1)]:
    ax.plot(
        [x, x+d*0.08], [3.08, 3.16],
        color='#49302F', linewidth=2, zorder=16
    )

# Pipi
ellipse((-0.31, 2.79), 0.16, 0.085,
        '#FF9BB2', z=14, edge='none')
ellipse((0.31, 2.79), 0.16, 0.085,
        '#FF9BB2', z=14, edge='none')

# Hidung
ellipse((0, 2.85), 0.055, 0.045,
        '#E99B91', z=15, edge='none')

# Senyum
mx = np.linspace(-0.09, 0.09, 30)
my = 2.75 - 0.045*(1-(mx/0.09)**2)
ax.plot(mx, my, color='#B75A65',
        linewidth=2, zorder=16)

# ==================================================
# 8. PITA RAMBUT
# ==================================================

polygon([
    (-0.39, 3.53), (-0.73, 3.78),
    (-0.66, 3.38), (-0.39, 3.40)
], '#FF78B4', 17)

polygon([
    (-0.39, 3.53), (-0.12, 3.83),
    (-0.18, 3.42), (-0.39, 3.40)
], '#F65A9C', 17)

ellipse((-0.39, 3.53), 0.14, 0.14,
        '#FFE1EE', z=18)

# ==================================================
# 9. TANGAN, KAKI DAN SEPATU
# ==================================================

leg_left = line('#FFD1BC', 13)
leg_right = line('#FFD1BC', 13)

shoe_left = line('#F04D9C', 12)
shoe_right = line('#F04D9C', 12)

arm_left = line('#FFD1BC', 10)
arm_right = line('#FFD1BC', 10)

sleeve_left = line('#FF86B8', 14)
sleeve_right = line('#FF86B8', 14)

# ==================================================
# 10. TRANSFORMASI GEOMETRI
# ==================================================

def transform(points, x, y, scale, angle):

    # Scaling
    S = np.array([
        [scale, 0],
        [0, scale]
    ])

    # Rotasi
    R = np.array([
        [np.cos(angle), -np.sin(angle)],
        [np.sin(angle), np.cos(angle)]
    ])

    # Gabungan scaling dan rotasi
    result = (R @ S @ points.T).T

    # Translasi
    result[:, 0] += x
    result[:, 1] += y

    return result

# ==================================================
# 11. ANIMASI KARAKTER
# ==================================================

def update(frame):

    phase = frame * 0.16

    # Translasi
    x = 1.15 + (frame / 239) * 7.65

    # Scaling
    scale = 1 + 0.018 * np.sin(phase * 2)

    # Rotasi
    angle = np.deg2rad(3) * np.sin(phase)

    # Posisi vertikal tubuh
    bounce = 0.0

    # Perbarui polygon
    for obj, original in polygons:
        points = transform(
            original.copy(), x, 0.65+bounce,
            scale, angle
        )
        obj.set_xy(points)

    # Perbarui ellipse
    for obj, center, width, height, old_angle in ellipses:

        new_center = transform(
            center.reshape(1, 2).copy(),
            x, 0.65+bounce, scale, angle
        )[0]

        obj.center = new_center
        obj.width = width*scale
        obj.height = height*scale
        obj.angle = old_angle + np.rad2deg(angle)

    # Ayunan kaki
    swing = np.sin(phase)*0.34

    hip_left = np.array([-0.22, 1.08])
    hip_right = np.array([0.22, 1.08])

    lift_left = max(0, np.sin(phase))*0.12
    lift_right = max(0, -np.sin(phase))*0.12

    foot_left = np.array([
        -0.22+swing,
        0.06+lift_left
    ])

    foot_right = np.array([
        0.22-swing,
        0.06+lift_right
    ])

    # Ayunan tangan
    shoulder_left = np.array([-0.37, 2.13])
    shoulder_right = np.array([0.37, 2.13])

    hand_left = shoulder_left + np.array([
        -swing, -0.45
    ])

    hand_right = shoulder_right + np.array([
        swing, -0.45
    ])

    # Fungsi menggerakkan garis
    def move_line(obj, p1, p2):

        points = transform(
            np.array([p1, p2]),
            x, 0.65+bounce, scale, angle
        )

        obj.set_data(
            points[:, 0],
            points[:, 1]
        )

    # Kaki
    move_line(leg_left, hip_left, foot_left)
    move_line(leg_right, hip_right, foot_right)

    # Sepatu
    move_line(
        shoe_left,
        foot_left,
        foot_left+np.array([0.23, -0.02])
    )

    move_line(
        shoe_right,
        foot_right,
        foot_right+np.array([0.23, -0.02])
    )

    # Tangan
    move_line(arm_left, shoulder_left, hand_left)
    move_line(arm_right, shoulder_right, hand_right)

    # Lengan baju
    move_line(
        sleeve_left,
        shoulder_left,
        shoulder_left+(hand_left-shoulder_left)*0.35
    )

    move_line(
        sleeve_right,
        shoulder_right,
        shoulder_right+(hand_right-shoulder_right)*0.35
    )

    return (
        [obj for obj, _ in polygons]
        + [obj for obj, *_ in ellipses]
        + [
            leg_left, leg_right,
            shoe_left, shoe_right,
            arm_left, arm_right,
            sleeve_left, sleeve_right
        ]
    )

# ==================================================
# 12. JUDUL ANIMASI
# ==================================================

ax.text(
    5, 5.12,
    'PINK PRINCESS',
    fontsize=23,
    fontweight='bold',
    color='#E94F94',
    ha='center'
)

ax.text(
    5, 4.83,
    "A Little Girl's Dreamy Garden",
    fontsize=11,
    color='#8A5574',
    ha='center'
)

# ==================================================
# 13. MENJALANKAN ANIMASI
# ==================================================

ani = animation.FuncAnimation(
    fig,
    update,
    frames=240,
    interval=1000/30,
    blit=False,
    repeat=True
)

plt.tight_layout()
plt.show()
