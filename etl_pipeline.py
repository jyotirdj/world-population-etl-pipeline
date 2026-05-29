import pandas as pd
from sqlalchemy import create_engine


# =====================
# EXTRACT
# =====================
def extract():
    df = pd.read_csv("world_population.csv")
    print("Extract done — shape:", df.shape)
    return df


# =====================
# TRANSFORM
# =====================
def transform(df):
    df = df.dropna(subset=["Country/Territory", "2022 Population"])

    # Keep only useful columns
    df = df[
        [
            "Country/Territory",
            "Continent",
            "2022 Population",
            "Area (km²)",
            "Density (per km²)",
        ]
    ]

    # Rename for cleanliness
    df = df.rename(
        columns={
            "Country/Territory": "country",
            "Continent": "continent",
            "2022 Population": "population",
            "Area (km²)": "area_km2",
            "Density (per km²)": "density_per_km2",
        }
    )

    # Round density column
    df["density_per_km2"] = df["density_per_km2"].round(2)

    # Add a new column — population category
    df["population_category"] = df["population"].apply(
        lambda x: "Large" if x > 100000000 else "Medium" if x > 10000000 else "Small"
    )

    print("Transform done — shape:", df.shape)
    print(df.head())
    return df


# =====================
# LOAD
# =====================
def load(df):
    # Connect to your PostgreSQL
    engine = create_engine("postgresql://postgres:admin123@localhost:5432/etl_project")

    # Load into PostgreSQL table
    df.to_sql("world_population", engine, if_exists="replace", index=False)
    print("Load done — data saved to PostgreSQL!")


# =====================
# RUN PIPELINE
# =====================
if __name__ == "__main__":
    raw_data = extract()
    clean_data = transform(raw_data)
    load(clean_data)
