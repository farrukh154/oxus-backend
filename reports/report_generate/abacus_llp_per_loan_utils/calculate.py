from .constants import CATEGORY_COLUMN
from .constants import CATEGORY_COLUMN_ID
from .constants import COLUMN_NUMBER
from .constants import LLP_COLUMN_SUM

from .calculate_helper import calculate_standard
from .calculate_helper import calculate_under_control
from .calculate_helper import calculate_not_standard
from .calculate_helper import calculate_uncertain
from .calculate_helper import calculate_hopeless
from .calculate_helper import calculate_o_court_case
from .calculate_helper import calculate_max_category
from .calculate_helper import calculate_o_RSCHD
from .calculate_helper import calculate_o_parallels
from .calculate_helper import calculate_o_set_percentage


def calculate_llp(excel_data_df):
    for i in iter(range(COLUMN_NUMBER)):
        excel_data_df.insert(CATEGORY_COLUMN_ID + i, f'{CATEGORY_COLUMN}{i}', 0, True)
    for i in iter(range(COLUMN_NUMBER)):
        calculate_standard(excel_data_df, i)
    for i in iter(range(COLUMN_NUMBER)):
        calculate_under_control(excel_data_df, i)
    for i in iter(range(COLUMN_NUMBER)):
        calculate_not_standard(excel_data_df, i)
    for i in iter(range(COLUMN_NUMBER)):
        calculate_uncertain(excel_data_df, i)
    for i in iter(range(COLUMN_NUMBER)):
        calculate_hopeless(excel_data_df, i)
    excel_data_df.insert(CATEGORY_COLUMN_ID + COLUMN_NUMBER, 'court_case', 1, True)
    calculate_o_court_case(excel_data_df)
    excel_data_df.insert(CATEGORY_COLUMN_ID + COLUMN_NUMBER + 1, 'max_category', 1, True)
    calculate_max_category(excel_data_df)
    excel_data_df.insert(CATEGORY_COLUMN_ID + COLUMN_NUMBER + 2, 'category_add_if_RSCHD', 0, True)
    excel_data_df.insert(CATEGORY_COLUMN_ID + COLUMN_NUMBER + 3, 'final_category', 0, True)
    calculate_o_RSCHD(excel_data_df)
    calculate_o_parallels(excel_data_df)
    excel_data_df.insert(CATEGORY_COLUMN_ID + COLUMN_NUMBER + 4, 'percentage', 0.0, True)
    calculate_o_set_percentage(excel_data_df)

    # set sum of LLP
    # --------------------------------------------------------------------------------------
    excel_data_df.insert(CATEGORY_COLUMN_ID + COLUMN_NUMBER + 4, LLP_COLUMN_SUM, 0.0, True)
    excel_data_df.loc[(excel_data_df['final_category'] <= 2) | (excel_data_df['olbintjs'] < 25000), LLP_COLUMN_SUM] = excel_data_df['olbintjs'] * excel_data_df['percentage']
    excel_data_df.loc[(excel_data_df['final_category'] > 2) & (excel_data_df['collateral_realestate'].isnull()) & (excel_data_df['olbintjs'] > 25000), LLP_COLUMN_SUM] = excel_data_df['olbintjs']
    excel_data_df.loc[(excel_data_df['final_category'] > 2) & (excel_data_df['collateral_realestate'].notnull()) & (excel_data_df['olbintjs'] > 25000), LLP_COLUMN_SUM] = excel_data_df['olbintjs'] / 2