import numpy as np
import matplotlib.dates as dts


def polyfit(dates, levels, p):
    try:
        # converting the dates to int
        adjusted = dts.date2num(dates)
        # recording initial value
        shift = adjusted[0]
        # normalising time integer values
        for i in adjusted:
            i -= shift
        # obtaining coefficients of the fitting polynomial of deg p
        p_coeff = np.polyfit(adjusted, levels, p)
        # producing polynomial function with coeffs
        poly = np.poly1d(p_coeff)
        # producing tuple with fitted func and norm shift
        output = (poly, shift)
        return(output)
    except:
        print("Data for this station is invalid and further assessment thus cannot be conducted.")