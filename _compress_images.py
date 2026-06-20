from PIL import Image
import os

base = "assets/images"

# === Compress logo-full.png ===
logo_path = os.path.join(base, "logo-full.png")
img = Image.open(logo_path)
orig_size_mb = os.path.getsize(logo_path) / 1024 / 1024
print(f"Original logo: {orig_size_mb:.1f} MB, {img.size}, mode={img.mode}")

# Resize to reasonable web dimensions (the logo displays at max 36px height, so 200px is plenty)
# But keep higher res for retina: 400px height
ratio = 400 / max(img.size)
new_size = (int(img.size[0] * ratio), int(img.size[1] * ratio))
img_resized = img.resize(new_size, Image.LANCZOS)

# Save optimized PNG (replace original)
opt_path = os.path.join(base, "logo-full-optimized.png")
img_resized.save(opt_path, "PNG", optimize=True)
print(f"Optimized PNG: {os.path.getsize(opt_path)/1024:.0f} KB, {img_resized.size}")

# Backup original and replace
backup_path = os.path.join(base, "logo-full-original.png")
if not os.path.exists(backup_path):
    os.rename(logo_path, backup_path)
    print(f"Backed up original to {backup_path}")
# Copy optimized to replace original name
img_resized.save(logo_path, "PNG", optimize=True)
print(f"Replaced logo-full.png: {os.path.getsize(logo_path)/1024:.0f} KB")

# === Compress ace-logo.png ===
ace_path = os.path.join(base, "ace-logo.png")
img2 = Image.open(ace_path)
orig2_mb = os.path.getsize(ace_path) / 1024 / 1024
print(f"\nOriginal ace-logo: {orig2_mb:.1f} MB, {img2.size}, mode={img2.mode}")

# ACE logo displays at 75px height, keep 300px for retina
ratio2 = 300 / max(img2.size)
new_size2 = (int(img2.size[0] * ratio2), int(img2.size[1] * ratio2))
img2_resized = img2.resize(new_size2, Image.LANCZOS)

backup2 = os.path.join(base, "ace-logo-original.png")
if not os.path.exists(backup2):
    os.rename(ace_path, backup2)
    print(f"Backed up original to {backup2}")
img2_resized.save(ace_path, "PNG", optimize=True)
print(f"Replaced ace-logo.png: {os.path.getsize(ace_path)/1024:.0f} KB, {img2_resized.size}")

print("\n=== IMAGE COMPRESSION COMPLETE ===")
print(f"Logo: {orig_size_mb:.1f} MB -> {os.path.getsize(logo_path)/1024:.0f} KB")
print(f"ACE: {orig2_mb:.1f} MB -> {os.path.getsize(ace_path)/1024:.0f} KB")
