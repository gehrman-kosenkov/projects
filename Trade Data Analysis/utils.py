import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from dateutil import parser

def week_to_date(df, product_name):

    def week_end_start(marketing_year, week):
        start_year = int(marketing_year.split('/')[0])
        end_year = int(marketing_year.split('/')[1])

        # Adjust week calculation if needed
        if week <= 26:
            year = start_year
            week_number = week
        else:
            year = end_year
            week_number = week - 26

        jan_1 = datetime(year, 1, 1)
        first_week_start = jan_1 + timedelta(days=(7 - jan_1.weekday()))
        week_start = first_week_start + timedelta(weeks=week_number - 1)
        week_end = week_start + timedelta(days=6)

        return week_start, week_end

    df[['Start date', 'End date']] = df.apply(
        lambda row: pd.Series(week_end_start(row['marketingYear'], row['week'])),
        axis=1
    )

    def split_week_into_months(row):
        result = []
        total_days = (row['End date'] - row['Start date']).days + 1
        current_date = row['Start date']

        while current_date <= row['End date']:
            start_of_month = current_date.replace(day=1)
            end_of_month = (start_of_month + pd.DateOffset(months=1) - pd.DateOffset(days=1)).date()
            
            if current_date.date() == row['End date'].date():
                end_of_period = row['End date']
            else:
                end_of_period = min(pd.Timestamp(end_of_month), row['End date'])
            
            days_in_period = (end_of_period - current_date).days + 1
            proportion = days_in_period / total_days
            value_for_period = (row['kgEquivalent'] * proportion) / 1000
            
            result.append({
                'date': current_date,
                'product': row['product'],
                f'TAXUD_{product_name}': value_for_period
            })

            current_date = end_of_period + timedelta(days=1)
        
        return pd.DataFrame(result)

    # Apply function to each row and concatenate results
    monthly_data = pd.concat(df.apply(split_week_into_months, axis=1).tolist(), ignore_index=True)
    
    return monthly_data
