#!/usr/bin/env python3
"""
Script untuk membuat mapping UUID ke NIM dan Nama mahasiswa
"""

import pandas as pd
import json
from pathlib import Path

# Paths
base_path = Path(__file__).parent.parent
prestasi_path = base_path / "docs" / "prestasi_clean_20250913_143222.csv"
mahasiswa_path = base_path / "docs" / "mahasiswa_clean_20250913_143222.csv"
uuid_mapping_path = base_path / "docs" / "uuid_to_nim_mapping.json"
complete_mapping_path = base_path / "docs" / "uuid_to_student_mapping.json"

print("🔍 Loading data files...")

# Load prestasi data
prestasi_df = pd.read_csv(prestasi_path)
print(f"✅ Loaded {len(prestasi_df)} prestasi records")
print(f"   Columns: {prestasi_df.columns.tolist()[:10]}...")

# Load mahasiswa data
mahasiswa_df = pd.read_csv(mahasiswa_path)
print(f"✅ Loaded {len(mahasiswa_df)} mahasiswa records")
print(f"   Columns: {mahasiswa_df.columns.tolist()[:10]}...")

# Get unique UUID mahasiswa from prestasi
unique_uuids = prestasi_df['id_mahasiswa'].unique()
print(f"📊 Found {len(unique_uuids)} unique student UUIDs in prestasi data")

# Load existing UUID mapping if exists
existing_mapping = {}
if uuid_mapping_path.exists():
    with open(uuid_mapping_path, 'r') as f:
        existing_mapping = json.load(f)
    print(f"📖 Loaded {len(existing_mapping)} existing UUID->NIM mappings")

# Create NIM to Name mapping
nim_to_name = {}
for _, row in mahasiswa_df.iterrows():
    nim = str(row['nim']).strip()
    nama = str(row['nama']).strip() if pd.notna(row['nama']) else 'Unknown'
    nim_to_name[nim] = nama

print(f"🔗 Created {len(nim_to_name)} NIM->Nama mappings")

# Create complete mapping (UUID -> {NIM, Nama})
complete_mapping = {}
mapped_count = 0
unmapped_uuids = []

for uuid in unique_uuids:
    if pd.isna(uuid):
        continue
    
    uuid_str = str(uuid).strip()
    
    # Check if UUID is in existing mapping
    if uuid_str in existing_mapping:
        nim = existing_mapping[uuid_str]
        nama = nim_to_name.get(nim, 'Unknown')
        complete_mapping[uuid_str] = {
            'nim': nim,
            'nama': nama
        }
        mapped_count += 1
    else:
        unmapped_uuids.append(uuid_str)

print(f"\n📈 Mapping Results:")
print(f"   ✅ Mapped: {mapped_count} UUIDs")
print(f"   ❌ Unmapped: {len(unmapped_uuids)} UUIDs")

if unmapped_uuids:
    print(f"\n⚠️  Sample unmapped UUIDs:")
    for uuid in unmapped_uuids[:5]:
        print(f"   - {uuid}")

# Save complete mapping
with open(complete_mapping_path, 'w') as f:
    json.dump(complete_mapping, f, indent=2, ensure_ascii=False)

print(f"\n💾 Saved complete mapping to: {complete_mapping_path}")
print(f"   Total entries: {len(complete_mapping)}")

# Also create a simplified version for direct UUID -> data
prestasi_with_names = []
for _, row in prestasi_df.iterrows():
    uuid = str(row['id_mahasiswa']).strip() if pd.notna(row['id_mahasiswa']) else None
    
    entry = {
        'id_mahasiswa': uuid,
        'judul': row.get('judul', ''),
        'tingkat': row.get('tingkat', ''),
        'kategori': row.get('kategori', ''),
        'tanggal': row.get('tanggal', ''),
        'nim': '',
        'nama': '-'
    }
    
    if uuid and uuid in complete_mapping:
        entry['nim'] = complete_mapping[uuid]['nim']
        entry['nama'] = complete_mapping[uuid]['nama']
    
    prestasi_with_names.append(entry)

# Save enriched prestasi data
enriched_path = base_path / "docs" / "prestasi_with_names.json"
with open(enriched_path, 'w') as f:
    json.dump(prestasi_with_names, f, indent=2, ensure_ascii=False)

print(f"💾 Saved enriched prestasi data to: {enriched_path}")

# Print statistics
print(f"\n📊 Statistics:")
print(f"   Total prestasi records: {len(prestasi_df)}")
print(f"   Records with NIM/Nama: {sum(1 for e in prestasi_with_names if e['nim'])}")
print(f"   Records without mapping: {sum(1 for e in prestasi_with_names if not e['nim'])}")

# Show some examples
print(f"\n✨ Sample mapped records:")
mapped_records = [e for e in prestasi_with_names if e['nim']][:3]
for i, record in enumerate(mapped_records, 1):
    print(f"   {i}. {record['nim']} - {record['nama']}")
    print(f"      Lomba: {record['judul'][:50]}...")

print("\n✅ Mapping completed!")
