#!/usr/bin/env python3
"""
Convert prestasi.csv to JSON format for dashboard
"""

import pandas as pd
import json
from pathlib import Path

# Paths
csv_path = Path("/workspaces/Skripsi/docs/prestasi.csv")
json_path = Path("/workspaces/Skripsi/docs/prestasi_data.json")

print("🔄 Converting CSV to JSON...")

# Read CSV
df = pd.read_csv(csv_path)
print(f"✅ Loaded {len(df)} records from CSV")

# Remove rows with empty judul (invalid records)
df_valid = df[df['judul'].notna() & (df['judul'].str.strip() != '')]
print(f"✅ Found {len(df_valid)} valid records")

# Convert to JSON format
prestasi_data = []
for _, row in df_valid.iterrows():
    prestasi_data.append({
        'nim': str(row['nim']).strip() if pd.notna(row['nim']) and str(row['nim']).strip() != '0' else '',
        'nama': str(row['nama']).strip() if pd.notna(row['nama']) else '',
        'judul': str(row['judul']).strip() if pd.notna(row['judul']) else '',
        'tingkat': str(row['tingkat']).strip() if pd.notna(row['tingkat']) else '',
        'kategori': str(row['kategori']).strip() if pd.notna(row['kategori']) else '',
        'tanggal': str(row['tanggal']).strip() if pd.notna(row['tanggal']) else ''
    })

# Save as JSON
with open(json_path, 'w', encoding='utf-8') as f:
    json.dump(prestasi_data, f, indent=2, ensure_ascii=False)

print(f"💾 Saved to: {json_path}")
print(f"📊 Total records: {len(prestasi_data)}")

# Statistics
with_nim = sum(1 for p in prestasi_data if p['nim'])
without_nim = len(prestasi_data) - with_nim

print(f"\n📈 Statistics:")
print(f"   ✅ With NIM: {with_nim} ({with_nim/len(prestasi_data)*100:.1f}%)")
print(f"   ❌ Without NIM: {without_nim} ({without_nim/len(prestasi_data)*100:.1f}%)")

# Show sample
print(f"\n✨ Sample records with NIM:")
for i, record in enumerate([p for p in prestasi_data if p['nim']][:3], 1):
    print(f"   {i}. {record['nim']} - {record['nama']}")
    print(f"      {record['judul'][:50]}...")

print("\n✅ Conversion completed!")
