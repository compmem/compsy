# Author Denis A. Engemann <d.engemann@gmail.com>
# Adjustments: Josef Perktold, Per Sederberg
#
# License: BSD (3-clause)

import numpy as np
from scipy import stats
import pandas as pd

def ci_within(df, indexvar, withinvars, measvar, confint=0.95,
                      copy=True):
    """ Compute CI / SEM correction factor
    Morey 2008, Cousinaueu 2005, Loftus & Masson, 1994
    Also see R-cookbook http://goo.gl/QdwJl
    Note. This functions helps to generate appropriate confidence
    intervals for repeated measure designs.
    Standard confidence intervals are are computed on normalized data
    and a correction factor is applied that prevents insanely small values.
    df : instance of pandas.DataFrame
        The data frame objetct.
    indexvar : str
        The column name of of the identifier variable that representing
        subjects or repeated measures
    withinvars : str | list of str
        The column names of the categorial data identifying random effects
    measvar : str
        The column name of the response measure
    confint : float
        The confidence interval
    copy : bool
        Whether to copy the data frame or not.
    """
    if copy:
        df = df.copy()

    # Apply Cousinaueu's method:
    # compute grand mean
    mean_ = df[measvar].mean()

    # compute subject means
    subj_means = df.groupby(indexvar)[measvar].mean().values
    for subj, smean_ in zip(df[indexvar].unique(), subj_means):
        # center
        #df[measvar][df[indexvar] == subj] -= smean_
        df.loc[df[indexvar] == subj, measvar] -= smean_
        # add grand average
        #df[measvar][df[indexvar] == subj] += mean_
        df.loc[df[indexvar] == subj, measvar] += mean_

    def sem(x):
        return x.std() / np.sqrt(len(x))

    def ci(x):
        se = sem(x)
        return se * stats.t.interval(confint, len(x - 1))[1]

    aggfuncs = [np.mean, np.std, sem, ci, len]
    out = df.groupby(withinvars)[measvar].agg(aggfuncs)

    # compute & apply correction factor
    n_within = np.prod([len(df[k].unique()) for k in withinvars],
                       dtype= df[measvar].dtype)
    cf = np.sqrt(n_within / (n_within - 1.))
    for k in ['sem', 'std', 'ci']:
        out[k] *= cf

    out['ci'] = stats.t.isf((1 - confint) / 2., out['len'] - 1) * out['sem']

    return out


if __name__ == '__main__':
    ss = '''
     subject condition value
           1   pretest  59.4
           2   pretest  46.4
           3   pretest  46.0
           4   pretest  49.0
           5   pretest  32.5
           6   pretest  45.2
           7   pretest  60.3
           8   pretest  54.3
           9   pretest  45.4
          10   pretest  38.9
           1  posttest  64.5
           2  posttest  52.4
           3  posttest  49.7
           4  posttest  48.7
           5  posttest  37.4
           6  posttest  49.5
           7  posttest  59.9
           8  posttest  54.1
           9  posttest  49.6
          10  posttest  48.5'''

    import StringIO
    df = pd.read_fwf(StringIO.StringIO(ss), widths=[8, 10, 6], header=1)
    res = ci_within(df2, 'subject', ['condition'], 'value', confint=0.95)
    print(res)
    print(res[['len', 'mean', 'std', 'sem', 'ci']])

    #ci is different from R
    #http://www.cookbook-r.com/Graphs/Plotting_means_and_error_bars_%28ggplot2%29/#error-bars-for-within-subjects-variables

    #dfwc <- summarySEwithin(dfw.long, measurevar="value", withinvars="condition",
    #                        idvar="subject", na.rm=FALSE, conf.interval=.95)
    # condition  N value value_norm       sd        se       ci
    #  posttest 10 51.43      51.43 2.262361 0.7154214 1.618396
    #   pretest 10 47.74      47.74 2.262361 0.7154214 1.618396
