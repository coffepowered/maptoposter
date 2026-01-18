# 🗺️ Modena, Italia Map Posters - Complete Guide

## 📋 Project Summary

This implementation provides everything needed to generate **8 beautiful map poster variations** of Modena, Italia using **bright themes** and **different zoom levels**.

## ✅ What Has Been Created

### 1. 📜 Batch Generation Scripts

#### Option A: Python Script
```bash
python generate_modena_maps.py
```
- Generates all 8 variations automatically
- Progress bars with tqdm
- Error handling for each variation
- Estimated time: 15-30 minutes

#### Option B: Bash Script
```bash
./generate_modena_maps.sh
```
- Alternative shell-based approach
- Progress counter (X/8)
- Shows file listings at completion

### 2. 📚 Documentation Files

| File | Purpose |
|------|---------|
| `MODENA_VARIATIONS.md` | Detailed guide for each variation, themes, and tips |
| `IMPLEMENTATION_SUMMARY.md` | Technical implementation overview |
| `README.md` (updated) | Integrated Modena examples throughout |
| `USAGE_GUIDE.md` (this file) | Quick start guide with visual examples |

## 🎨 The 8 Variations (Bright Themes Focus)

### Overview Table

| # | Theme | Distance | Zoom Level | Background Color | Character |
|---|-------|----------|------------|------------------|-----------|
| 1 | **Terracotta** | 8000m | Medium | Cream (#F5EDE4) | 🇮🇹 Mediterranean warmth |
| 2 | **Warm Beige** | 6000m | Close-up | Beige (#F5F0E8) | 📜 Vintage sepia aesthetic |
| 3 | **Sunset** | 10000m | Wide | Soft Peach (#FDF5F0) | 🌅 Golden hour vibes |
| 4 | **Pastel Dream** | 8000m | Medium | Off-white (#FAF7F2) | 🎨 Artistic minimalism |
| 5 | **Autumn** | 12000m | Large | Warm Autumn | 🍂 Seasonal burnt oranges |
| 6 | **Copper Patina** | 5000m | Tight | Aged Copper | 🏛️ Historic metal aesthetic |
| 7 | **Ocean** | 8000m | Medium | Soft Blue | 🌊 Cool bright alternative |
| 8 | **Feature Based** | 8000m | Medium | White (#FFFFFF) | ⚫ Classic high-contrast |

## 🚀 Quick Start Guide

### Step 1: Verify Prerequisites
```bash
# Check Python installation
python --version  # Should be 3.8+

# Install dependencies
pip install -r requirements.txt

# Verify internet connection (required for OSM data)
ping -c 3 openstreetmap.org
```

### Step 2: Generate All Variations
```bash
# Using Python script (recommended)
python generate_modena_maps.py

# OR using Bash script
chmod +x generate_modena_maps.sh
./generate_modena_maps.sh
```

### Step 3: View Generated Posters
```bash
# List all Modena posters
ls -lh posters/modena_*.png

# View with image viewer
open posters/modena_terracotta_*.png  # macOS
xdg-open posters/modena_terracotta_*.png  # Linux
start posters/modena_terracotta_*.png  # Windows
```

## 📸 Expected Output Examples

### File Naming Convention
```
posters/
├── modena_terracotta_20260118_123456.png
├── modena_warm_beige_20260118_123712.png
├── modena_sunset_20260118_123928.png
├── modena_pastel_dream_20260118_124144.png
├── modena_autumn_20260118_124400.png
├── modena_copper_patina_20260118_124616.png
├── modena_ocean_20260118_124832.png
└── modena_feature_based_20260118_125048.png
```

### Poster Specifications
- **Dimensions**: 12" × 16" (3600 × 4800 pixels)
- **Resolution**: 300 DPI (print-ready)
- **Format**: PNG with transparency support
- **File Size**: ~3-11 MB per poster

### Poster Contents
Each poster includes:
- Street network with road hierarchy visualization
- Water features (rivers, canals, ponds)
- Parks and green spaces
- **City name** in spaced capitals: `M  O  D  E  N  A`
- **Country name**: `ITALIA`
- **Coordinates**: `44.6471° N / 10.9252° E`
- **Attribution**: © OpenStreetMap contributors

## 🎯 Individual Variation Commands

Want to generate just one specific variation? Use these commands:

```bash
# 1. Terracotta - Perfect Italian aesthetic
python create_map_poster.py -c "Modena" -C "Italia" -t terracotta -d 8000

# 2. Warm Beige - Vintage close-up of historic center
python create_map_poster.py -c "Modena" -C "Italia" -t warm_beige -d 6000

# 3. Sunset - Wide golden hour perspective
python create_map_poster.py -c "Modena" -C "Italia" -t sunset -d 10000

# 4. Pastel Dream - Soft artistic tones
python create_map_poster.py -c "Modena" -C "Italia" -t pastel_dream -d 8000

# 5. Autumn - Full metropolitan area
python create_map_poster.py -c "Modena" -C "Italia" -t autumn -d 12000

# 6. Copper Patina - Intimate downtown core
python create_map_poster.py -c "Modena" -C "Italia" -t copper_patina -d 5000

# 7. Ocean - Cool blues alternative
python create_map_poster.py -c "Modena" -C "Italia" -t ocean -d 8000

# 8. Feature Based - Classic black & white
python create_map_poster.py -c "Modena" -C "Italia" -t feature_based -d 8000
```

## 🔍 Zoom Level Details

### Understanding Distance Parameter

The distance parameter determines the radius of the map area:

```
5000m  (5km)  ──► Historic center detail
               ├─ Piazza Grande
               ├─ Cathedral (UNESCO)
               └─ Dense medieval streets

6000m  (6km)  ──► Downtown focus
               ├─ Old town + immediate surroundings
               └─ Main commercial districts

8000m  (8km)  ──► Balanced city view ⭐ Most versatile
               ├─ Central city
               ├─ Major neighborhoods
               └─ Key infrastructure

10000m (10km) ──► City + near suburbs
               ├─ Full urban core
               └─ Suburban development

12000m (12km) ──► Full metropolitan area
               ├─ Greater Modena
               ├─ Regional connections
               └─ Surrounding towns
```

## 🎨 Theme Descriptions

### Warm Bright Themes (Primary)

#### 1. Terracotta 🏺
- **Colors**: Burnt orange roads on cream background
- **Mood**: Mediterranean, earthy, warm Italian character
- **Best for**: Authentic Italian aesthetic
- **Water**: Muted teal (#A8C4C4)
- **Parks**: Light cream (#E8E0D0)

#### 2. Warm Beige 📜
- **Colors**: Sepia tones on warm beige background
- **Mood**: Vintage, nostalgic, old-world charm
- **Best for**: Historic documentation feel
- **Water**: Dusty beige (#DDD5C8)
- **Parks**: Light beige (#E8E4D8)

#### 3. Sunset 🌅
- **Colors**: Coral and pink roads on soft peach
- **Mood**: Golden hour, dreamy, romantic
- **Best for**: Artistic presentation
- **Water**: Soft pink-beige (#F0D8D0)
- **Parks**: Peachy cream (#F8E8E0)

#### 4. Pastel Dream 🎨
- **Colors**: Dusty blues and mauves on off-white
- **Mood**: Soft, artistic, minimalist
- **Best for**: Modern gallery aesthetic
- **Water**: Soft blue (#D4E4ED)
- **Parks**: Pale sage (#E8EDE4)

#### 5. Autumn 🍂
- **Colors**: Burnt oranges and reds
- **Mood**: Seasonal, warm, natural
- **Best for**: Fall atmosphere
- **Water**: Autumn tones
- **Parks**: Golden autumn hues

### Bright Alternative Themes

#### 6. Copper Patina 🏛️
- **Colors**: Oxidized copper tones with verdigris
- **Mood**: Historic, aged, architectural
- **Best for**: Antique metal aesthetic
- **Water**: Patina green-blue
- **Parks**: Aged copper-green

#### 7. Ocean 🌊
- **Colors**: Blues and teals
- **Mood**: Cool, fresh, coastal
- **Best for**: Bright alternative to warm themes
- **Water**: Deep ocean blue
- **Parks**: Sea foam green

### Reference Theme

#### 8. Feature Based ⚫⚪
- **Colors**: Black roads on white background
- **Mood**: Clean, technical, high-contrast
- **Best for**: Reference comparison
- **Water**: Gray
- **Parks**: Light gray

## 📊 Generation Timeline

Expected time for each variation:

```
[Starting] Geocoding lookup............ ~2 seconds
[Step 1/3] Street network download..... 30-90 seconds
[Step 2/3] Water features download..... 15-45 seconds
[Step 3/3] Parks download.............. 15-45 seconds
[Render]   Map rendering............... 10-30 seconds
[Save]     High-res export............. 5-15 seconds
───────────────────────────────────────────────────
Total per poster.................... 2-5 minutes

All 8 variations.................... 15-30 minutes
```

## 🔧 Troubleshooting

### Issue: "No module named 'osmnx'"
```bash
Solution: pip install -r requirements.txt
```

### Issue: "Could not find coordinates for Modena, Italia"
```bash
Solution: Use the batch scripts which have coordinates hardcoded
```

### Issue: "HTTPSConnectionPool... Max retries exceeded"
```bash
Solution: Check internet connection. OSM data download requires internet.
- Test: ping overpass-api.de
- Wait a moment if API is busy
- Try again
```

### Issue: Network timeout during download
```bash
Solution: Increase timeout or try again later
- OSM Overpass API can be busy during peak hours
- Script will retry automatically
```

## 📁 Project Structure

```
maptoposter/
├── create_map_poster.py         # Main generator (single maps)
├── generate_modena_maps.py      # Batch generator (Python)
├── generate_modena_maps.sh      # Batch generator (Bash)
├── MODENA_VARIATIONS.md         # Detailed variations guide
├── IMPLEMENTATION_SUMMARY.md    # Technical implementation
├── USAGE_GUIDE.md              # This quick start guide
├── README.md                    # Main documentation
├── requirements.txt             # Python dependencies
├── themes/                      # Theme JSON files
│   ├── terracotta.json
│   ├── warm_beige.json
│   ├── sunset.json
│   ├── pastel_dream.json
│   ├── autumn.json
│   ├── copper_patina.json
│   ├── ocean.json
│   └── feature_based.json
├── fonts/                       # Roboto font family
│   ├── Roboto-Bold.ttf
│   ├── Roboto-Regular.ttf
│   └── Roboto-Light.ttf
└── posters/                     # Generated output
    └── modena_*.png            # 8 variations (when generated)
```

## 🎓 Tips & Best Practices

### 1. Theme Selection
- **For Italian aesthetic**: Use Terracotta or Warm Beige
- **For modern look**: Use Pastel Dream or Ocean
- **For vintage feel**: Use Warm Beige or Sunset
- **For reference**: Use Feature Based

### 2. Distance Selection
- **Historic focus**: 5000-6000m
- **City overview**: 8000m (most versatile)
- **Regional context**: 10000-12000m

### 3. Batch Generation
- Use batch scripts for consistency
- Generate all 8 to compare and choose favorites
- Each takes 2-5 minutes, plan accordingly

### 4. Quality Tips
- Output is 300 DPI print-ready quality
- PNG format preserves quality
- No compression artifacts
- Suitable for large format printing

## 📖 Further Documentation

- **MODENA_VARIATIONS.md**: In-depth guide for each variation
- **IMPLEMENTATION_SUMMARY.md**: Technical implementation details
- **README.md**: Complete project documentation

## ✨ Summary

You now have everything needed to create 8 stunning map posters of Modena, Italia:

✅ Two batch generation scripts (Python & Bash)  
✅ Comprehensive documentation  
✅ 8 bright themes with varied zoom levels  
✅ Focus on Italian character with warm colors  
✅ Print-ready 300 DPI output  
✅ Individual command options for flexibility  

**Ready to generate?**
```bash
python generate_modena_maps.py
```

Then check the `posters/` directory for your beautiful Modena maps! 🗺️🇮🇹
