import cv2  # Computer vision
import numpy as np  # Math
import mss  # Screen grabbing

# Take screenshot of monitor
with mss.mss() as sct:
    img = np.array(sct.grab(sct.monitors[0]))  # Change monitor index if needed

# Drag box and press Enter to confirm
roi = cv2.selectROI('Image', img, False, False)
cv2.destroyAllWindows()

# Output the zone
zone = {
    "top": roi[1],
    "left": roi[0],
    "width": roi[2],
    "height": roi[3]
}
print(f"\n{zone}")

# Can now use zone to capture where you selected, eg.
# with mss.mss() as sct:
#     img = np.array(sct.grab(zone))
# cv2.imshow('Image', img)
# cv2.waitKey(0)
