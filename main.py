from scipy.stats import friedmanchisquare
import pandas as pd
import scikit_posthocs as sp

data1 = [
    2.38261E-01,
    1.25806E-01,
    -1.00000E+08,
    2.14973E-01,
    -3.99073E+02,
    6.47681E+02,
    3.49423E-01,
    5.67716E-02,
    9.36057E+01,
    2.13307E+01
]
data2 = [
    7.54952E-15,
    4.05812E-06,
    -1.00000E+08,
    6.48575E-09,
    -3.99111E+02,
    3.14285E-04,
    6.08654E-02,
    1.88505E-47,
    6.29153E-01,
    4.05030E-01
]
data3 = [
    1.71720E+01,
    2.18870E+00,
    -9.99822E+07,
    8.81781E+01,
    -2.68344E+02,
    8.13859E+02,
    9.55534E+01,
    7.27770E-29,
    4.64709E+01,
    1.65901E-28
]
data4 = [
    2.93731E-02,
    9.87446E-02,
    -1.00000E+08,
    3.81305E-02,
    -3.99111E+02,
    1.80594E+01,
    9.94959E-02,
    5.70226E-15,
    2.62479E+01,
    4.11928E-08
]
data5 = [
    6.01602E-05,
    1.81164E+00,
    -1.00000E+08,
    4.94388E-01,
    -3.99111E+02,
    1.70148E-04,
    9.94959E-02,
    1.87801E-11,
    6.21226E+01,
    1.57644E-05
]
data6 = [
    1.63869E-13,
    5.52171E-10,
    -9.99940E+07,
    1.17524E+02,
    -2.80175E+02,
    1.48139E-41,
    3.67820E+02,
    1.28913E-43,
    2.65496E+01,
    2.17610E-37
]

if __name__ == "__main__":
    stat, p = friedmanchisquare(data1, data2, data3, data4, data5, data6)
    print('Statistics=%.3f, p=%.3f' % (stat, p))

    alpha = 0.05
    if p < alpha:
        print('Different distributions (reject H0)')
    else:
        print('Same distribution (fail to reject H0)')

    data = pd.DataFrame({
        "Treatment1": data1,
        "Treatment2": data2,
        "Treatment3": data3,
        "Treatment4": data4,
        "Treatment5": data5,
        "Treatment6": data6
    })

    result = sp.posthoc_nemenyi_friedman(data.transpose())
    print(result)
