#!/usr/bin/env python3
"""
Cohen
=====

Beinhaltet Funktionen zum errechnen der Effektstärke d_s nach
Cohen, J. (1988). Statistical Power Analysis for the Behavioral Sciences. 2. Auflage. Lawrence Erlbaum Associates, Hillsdale 1988, ISBN 0-8058-0283-5.

https://de.wikipedia.org/wiki/Effektst%C3%A4rke
"""
import numpy as np  # import sum, mean, sqrt, square, array


def pooled_std(A, B):
    '''
    Pooled within-sample estimate of the standard deviation.

    Formula (2.5.2) of Cohen, J. (1988). Statistical power analysis for the
    behavioral sciences. Hillsdale, NJ: Erlbaum.
    '''
    return np.sqrt(
        (
            np.sum(np.square(A - np.mean(A)))
            + np.sum(np.square(B - np.mean(B)))
        )
        /
        (len(A) + len(B) - 2)
    )


def ds(A, B):
    '''
    Cohen's d effect size for independent samples.

    Formula (2.5.1) of Cohen, J. (1988). Statistical power analysis for the
    behavioral sciences. Hillsdale, NJ: Erlbaum.
    '''
    # A = array(A)
    # B = array(B)
    return (np.mean(A) - np.mean(B)) / pooled_std(A, B)


if __name__ == '__main__':
    import pandas as pd
    A = pd.Series([60, 50, 68, 59, 64, 72, 64, 70, 73, 63, 72])
    B = pd.Series([69, 75, 64, 66, 71])

    d_s = abs(ds(A, B)) - 0.63133
    assert d_s < 0.00001, d_s

    height_m = [175, 170, 179, 180, 184, 188, 179, 187, 196, 183, 190]
    height_f = [164, 168, 170, 172, 169]

    d_s = abs(ds(height_m, height_f)) - 2.23056
    assert d_s < 0.00001, d_s
