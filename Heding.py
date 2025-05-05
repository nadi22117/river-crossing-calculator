import math


def compute_crossing(vb, vr, theta_deg, D):
    """
    מחשבת זמן חציית נהר וסטייה אופקית (drift) עבור סירה.
    """

    theta_rad = math.radians(theta_deg)

    vx = vb * math.sin(theta_rad)  # רכיב אופקי של הסירה
    vy = vb * math.cos(theta_rad)  # רכיב אנכי
    v_total_x = vx + vr  # סה"כ מהירות בציר X (כוללת זרם)

    if vy == 0:
        raise ValueError("Vertical component of velocity is zero – can't cross the river!")

    t = abs(D) / vy  # זמן חצייה (מרחק / רכיב אנכי)
    drift = v_total_x * t  # סטייה בציר X

    return {
        "time": t,
        "drift": drift
    }
