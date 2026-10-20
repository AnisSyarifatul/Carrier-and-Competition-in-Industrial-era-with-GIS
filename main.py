import math
import pandas as pd
import folium
from itertools import combinations

data = pd.read_csv("gerai.csv")

print("=" * 45)
print("GIS ANALISIS LOKASI GERAI")
print("=" * 45)
print(f"Jumlah gerai: {len(data)}")
print(data[["nama_gerai", "latitude", "longitude"]].to_string(index=False))

def hitung_jarak(lat1, lon1, lat2, lon2):
    """Menghitung jarak dua koordinat dalam kilometer."""
    radius_bumi = 6371

    lat1, lat2 = math.radians(lat1), math.radians(lat2)
    selisih_lat = math.radians(lat2 - lat1)
    selisih_lon = math.radians(lon2 - lon1)

    a = (
        math.sin(selisih_lat / 2) ** 2
        + math.cos(lat1)
        * math.cos(lat2)
        * math.sin(selisih_lon / 2) ** 2
    )

    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return radius_bumi * c

hasil = []
ambang_jarak = 1.0  # kilometer, untuk simulasi

for gerai1, gerai2 in combinations(
    data.to_dict("records"), 2
):
    jarak = hitung_jarak(
        gerai1["latitude"],
        gerai1["longitude"],
        gerai2["latitude"],
        gerai2["longitude"],
    )

    status = (
        "Berdekatan"
        if jarak < ambang_jarak
        else "Tidak berdekatan"
    )

    hasil.append({
        "gerai_1": gerai1["nama_gerai"],
        "gerai_2": gerai2["nama_gerai"],
        "jarak_km": round(jarak, 3),
        "status": status,
    })

hasil_df = pd.DataFrame(hasil)
hasil_df.to_csv("hasil_analisis_jarak.csv", index=False)

print("\nHASIL ANALISIS JARAK")
print(hasil_df.to_string(index=False))
print("\nLaporan disimpan ke hasil_analisis_jarak.csv")

pusat_peta = [
    data["latitude"].mean(),
    data["longitude"].mean(),
]

peta = folium.Map(
    location=pusat_peta,
    zoom_start=14,
    tiles="OpenStreetMap",
)

for _, gerai in data.iterrows():
    folium.Marker(
        location=[gerai["latitude"], gerai["longitude"]],
        tooltip=gerai["nama_gerai"],
        popup=(
            f"<b>{gerai['nama_gerai']}</b><br>"
            f"Latitude: {gerai['latitude']}<br>"
            f"Longitude: {gerai['longitude']}"
        ),
        icon=folium.Icon(color="blue", icon="shopping-cart"),
    ).add_to(peta)

    folium.Circle(
        location=[gerai["latitude"], gerai["longitude"]],
        radius=ambang_jarak * 1000,
        color="blue",
        fill=True,
        fill_opacity=0.08,
        tooltip="Jangkauan simulasi 1 km",
    ).add_to(peta)

folium.LayerControl().add_to(peta)

peta.save("peta_gerai.html")

print("\nPeta berhasil dibuat: peta_gerai.html")
print("Buka file HTML tersebut di browser.")