# Modena, Italia - Map Poster Variations Guide

This document provides detailed instructions for generating 8 beautiful map poster variations for Modena, Italia using bright themes and different zoom levels.

## About Modena

**Location**: Emilia-Romagna, Northern Italy  
**Coordinates**: 44.6471° N, 10.9252° E  
**Known for**: Historic city center (UNESCO World Heritage Site), medieval architecture, balsamic vinegar, and Ferrari

## Variations Overview

All variations emphasize bright, warm themes that complement Modena's Italian character:

| # | Theme | Distance | Background | Character |
|---|-------|----------|------------|-----------|
| 1 | Terracotta | 8000m | Cream (#F5EDE4) | Mediterranean warmth with clay tones |
| 2 | Warm Beige | 6000m | Beige (#F5F0E8) | Vintage sepia aesthetic, close-up |
| 3 | Sunset | 10000m | Soft Peach (#FDF5F0) | Golden hour vibes, wider view |
| 4 | Pastel Dream | 8000m | Off-white (#FAF7F2) | Soft muted artistic tones |
| 5 | Autumn | 12000m | Warm Autumn | Seasonal burnt oranges, large view |
| 6 | Copper Patina | 5000m | Aged Copper | Oxidized metal aesthetic, tight |
| 7 | Ocean | 8000m | Soft Blue | Cool alternative bright theme |
| 8 | Feature Based | 8000m | White (#FFFFFF) | Classic high-contrast reference |

## Generation Commands

### Quick Generation (All Variations)

Use the provided helper script to generate all 8 variations at once:

```bash
python generate_modena_maps.py
```

### Individual Generation

Or generate each variation individually:

```bash
# Variation 1: Terracotta - Medium city view
python create_map_poster.py -c "Modena" -C "Italia" -t terracotta -d 8000

# Variation 2: Warm Beige - Focused downtown
python create_map_poster.py -c "Modena" -C "Italia" -t warm_beige -d 6000

# Variation 3: Sunset - Wider perspective
python create_map_poster.py -c "Modena" -C "Italia" -t sunset -d 10000

# Variation 4: Pastel Dream - Artistic medium view
python create_map_poster.py -c "Modena" -C "Italia" -t pastel_dream -d 8000

# Variation 5: Autumn - Large metropolitan view
python create_map_poster.py -c "Modena" -C "Italia" -t autumn -d 12000

# Variation 6: Copper Patina - Intimate downtown
python create_map_poster.py -c "Modena" -C "Italia" -t copper_patina -d 5000

# Variation 7: Ocean - Alternative bright theme
python create_map_poster.py -c "Modena" -C "Italia" -t ocean -d 8000

# Variation 8: Feature Based - Classic contrast
python create_map_poster.py -c "Modena" -C "Italia" -t feature_based -d 8000
```

## Detailed Variation Descriptions

### 1. Terracotta (8000m) - Mediterranean Warmth
Perfect for capturing Modena's Italian essence with warm, earthy tones reminiscent of Mediterranean architecture.
- **Best for**: General city overview with authentic Italian color palette
- **Highlights**: Historic center, main streets, park areas
- **Color scheme**: Burnt orange roads on cream background

### 2. Warm Beige (6000m) - Vintage Focus
Closer view showcasing the historic downtown with vintage map aesthetics.
- **Best for**: Detailed view of medieval city center
- **Highlights**: Piazza Grande, Cathedral, dense historic streets
- **Color scheme**: Sepia tones creating nostalgic feel

### 3. Sunset (10000m) - Golden Hour
Wider perspective with dreamy golden hour colors extending to suburbs.
- **Best for**: Showing Modena in broader regional context
- **Highlights**: Full city plus surrounding areas
- **Color scheme**: Warm oranges and soft pinks

### 4. Pastel Dream (8000m) - Artistic Minimalism  
Soft, muted tones for an artistic, gallery-ready representation.
- **Best for**: Modern, minimalist aesthetic
- **Highlights**: Balanced city view with artistic flair
- **Color scheme**: Dusty blues and mauves

### 5. Autumn (12000m) - Seasonal Panorama
Largest view showing greater Modena metropolitan area with seasonal warmth.
- **Best for**: Understanding city's full extent and connections
- **Highlights**: Complete urban area, major arteries
- **Color scheme**: Burnt oranges and autumn reds

### 6. Copper Patina (5000m) - Intimate Core
Tightest zoom focusing on the densest historic center.
- **Best for**: Detailed street-level appreciation
- **Highlights**: UNESCO Heritage Site core, intricate medieval layout
- **Color scheme**: Aged copper with verdigris accents

### 7. Ocean (8000m) - Cool Alternative
Bright theme with cool tones providing contrast to warm variations.
- **Best for**: Alternative aesthetic, complementary to warm themes
- **Highlights**: Standard city overview with fresh perspective
- **Color scheme**: Blues and teals

### 8. Feature Based (8000m) - Technical Reference
Classic high-contrast map emphasizing road hierarchy and urban structure.
- **Best for**: Technical analysis, clear reference
- **Highlights**: Road types, urban planning visible
- **Color scheme**: Black on white with shading

## Distance Guide for Modena

- **5000m**: Captures historic center and immediate surroundings
- **6000m**: Includes main downtown districts
- **8000m**: Balanced view of central city
- **10000m**: City plus near suburbs
- **12000m**: Full metropolitan area

## Output Files

Generated posters will be saved in `posters/` directory with naming format:
```
modena_<theme>_<timestamp>.png
```

Examples:
- `modena_terracotta_20260118_120000.png`
- `modena_warm_beige_20260118_120130.png`
- etc.

## Tips for Best Results

1. **Internet Required**: Ensure stable internet connection for downloading OpenStreetMap data
2. **Generation Time**: Each poster takes 2-5 minutes depending on distance and network speed
3. **High Resolution**: Output is 300 DPI suitable for printing
4. **Batch Generation**: Use `generate_modena_maps.py` for unattended generation of all variations
5. **Bright Themes**: Selected themes emphasize Modena's warm, historic character

## Theme Comparison

The bright themes chosen specifically complement Modena's characteristics:

- **Terracotta, Warm Beige, Sunset**: Authentic Italian warmth
- **Pastel Dream**: Modern artistic interpretation  
- **Autumn**: Seasonal northern Italian atmosphere
- **Copper Patina**: Historic metal/patina of old buildings
- **Ocean**: Fresh alternative while staying bright
- **Feature Based**: Clean reference for comparison

## Requirements

- Python 3.8+
- All dependencies from `requirements.txt`
- Internet connection for OSM data download
- ~5-10 minutes total generation time for all 8 variations
