import plotly.express as px


def create_gender_chart(df):

    gender_chart = px.pie(
        df,
        names="Gender",
        title="Gender Distribution"
    )


    return gender_chart