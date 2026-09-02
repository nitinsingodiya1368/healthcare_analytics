import pandas as pd


def transform_data(df):

    # ====================================
    # AGE GROUPS
    # ====================================

    if "Age" in df.columns:

        df["Age_Group"] = pd.cut(
            df["Age"],
            bins=[0, 18, 35, 60, 100],
            labels=[
                "Child",
                "Young Adult",
                "Adult",
                "Senior"
            ]
        )


    # ====================================
    # LENGTH OF STAY
    # ====================================

    if (
        "Date of Admission" in df.columns
        and
        "Discharge Date" in df.columns
    ):

        df["Length_of_Stay"] = (
            df["Discharge Date"]
            -
            df["Date of Admission"]
        ).dt.days


    # ====================================
    # ADMISSION MONTH
    # ====================================

    if "Date of Admission" in df.columns:

        df["Admission_Month"] = df[
            "Date of Admission"
        ].dt.month_name()


    return df