def generate_kpis(df):

    total_patients = len(df)


    average_age = None

    if "Age" in df.columns:

        average_age = round(
            df["Age"].mean(),
            2
        )


    total_revenue = None

    if "Billing Amount" in df.columns:

        total_revenue = round(
            df["Billing Amount"].sum(),
            2
        )


    average_stay = None

    if "Length_of_Stay" in df.columns:

        average_stay = round(
            df["Length_of_Stay"].mean(),
            2
        )


    kpi_report = {
        "total_patients": total_patients,
        "average_age": average_age,
        "total_revenue": total_revenue,
        "average_stay": average_stay
    }


    return kpi_report