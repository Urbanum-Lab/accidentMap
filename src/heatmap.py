import pandas as pd
import pydeck as pdk

df = pd.read_csv("data/interim/cleaned.csv")


def weight_accident(row):
    try:
        death = row["Meghaltak"] * 100
        bad = row["Súlyos"] * 10
        light = row["Könnyű"]
        no_ppl = row["Résztvevők száma"]
        return death + bad + light + no_ppl
    except:
        return 1


accident_weights = []
for _, row in df.iterrows():
    accident_weights.append(weight_accident(row))

df["weights"] = accident_weights

heat_layer = pdk.Layer(
    "HeatmapLayer",
    df,
    opacity=0.9,
    get_position=["LON", "LAT"],
    get_weight="weights",
)

dot_layer = pdk.Layer(
    "ScatterplotLayer",
    df,
    pickable=True,
    opacity=0.0,
    get_position=["LON", "LAT"],
)

view_state = pdk.ViewState(
    latitude=47.490000, longitude=19.074436, zoom=14, bearing=0, pitch=0
)

r = pdk.Deck(
    layers=[heat_layer, dot_layer],
    initial_view_state=view_state,
    tooltip={"text": "Kimenetel: {Kimenetel}"},
)
r.to_html("vizs/test.html")
