from services.data_loader import load_data
from services.validation_service import validate_data
from services.cleaning_service import clean_data
from services.transformation_service import transform_data
from services.analytics_service import generate_kpis


# ====================================
# LOAD DATA
# ====================================

raw_df = load_data(
    "data/raw/healthcare_dataset.csv"
)


# ====================================
# VALIDATE DATA
# ====================================

validation_results = validate_data(raw_df)

print("\nVALIDATION RESULTS")
print(validation_results)


# ====================================
# CLEAN DATA
# ====================================

clean_df = clean_data(raw_df)

print("\nCLEANED DATA")
print(clean_df.head())


# ====================================
# TRANSFORM DATA
# ====================================

transformed_df = transform_data(clean_df)

print("\nTRANSFORMED DATA")
print(transformed_df.head())


# ====================================
# GENERATE KPIs
# ====================================

kpis = generate_kpis(transformed_df)

print("\nKPI RESULTS")
print(kpis)