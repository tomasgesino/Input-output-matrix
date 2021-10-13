import numpy as np
import fractions

initial_boot = input("""
                        1) Input-output matrix
                        """)


def matriz_insumo_producto():
    aa = float(input("Number @ 11: "))
    ab = float(input("Number @ 12: "))
    ba = float(input("Number @ 21: "))
    bb = float(input("Number @ 22: "))

    pt_a = float(input("Number Total Col 1: "))
    pt_b = float(input("Number Total Col 2: "))

    d_a = float(input("New Demand Row 1: "))
    d_b = float(input("New Demand Row 2: "))

    print("""
    {Xa = (%s / %s) * Xa + (%s / %s) * Xb + %s
    {Xb = (%s / %s) * Xa + (%s / %s) * Xb + %s
    """ % (aa, pt_a, ab, pt_b, d_a, ba, pt_a, bb, pt_b, d_b))

    aa_pt_a = fractions.Fraction(aa, pt_a)
    ab_pt_b = fractions.Fraction(ab, pt_b)
    ba_pt_a = fractions.Fraction(ba, pt_a)
    bb_pt_b = fractions.Fraction(bb, pt_b)

    print("""
        {Xa = %s * Xa + %s * Xb + %s
        {Xb = %s * Xa + %s * Xb + %s
        """ % (aa_pt_a, ab_pt_b, d_a, ba_pt_a, bb_pt_b, d_b))

    x = np.array[["X_a"], ["X_b"]]
    i = np.array[[1.0, 0.0], [0.0, 1.0]]
    a = np.array[[aa_pt_a, ab_pt_b], [ba_pt_a, bb_pt_b]]
    d = np.array[[d_a], [d_b]]

    print("""
        x = (%s - %s)^-1 * %s
        """ % (i, a, d))

    beta = i - a

    print("""
        x = (%s)^-1 * %s
        """ % (beta, d))

    beta_det = np.linalg.det(beta)

    beta_det_fraction = str(fractions.Fraction(beta_det))

    print(beta_det_fraction)

    print("""
        |%s| = %s
        """ % (beta, np.linalg.inv(beta_det_fraction)))



if initial_boot == 1:
    matriz_insumo_producto()
