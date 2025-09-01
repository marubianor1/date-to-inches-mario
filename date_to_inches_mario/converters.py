import numpy as np
import pandas as pd

MONTH_TO_FEET = {
    'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6,
    'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12
}

def date_to_inches(ht_str):
    if pd.isna(ht_str):
        return np.nan
    ht_str = str(ht_str).strip()
    try:
        day_str, month_str = ht_str.split('-')
        inches = int(day_str)
        feet = MONTH_TO_FEET.get(month_str.strip().title(), np.nan)
        if pd.isna(feet):
            return np.nan
        return feet * 12 + inches
    except Exception:
        return np.nan

def apply_date_to_inches(series: pd.Series) -> pd.Series:
    return series.apply(date_to_inches)
