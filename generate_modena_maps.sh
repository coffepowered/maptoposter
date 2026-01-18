#!/bin/bash
# Generate all 8 Modena, Italia map poster variations
# Focuses on bright themes with varied zoom levels

echo "============================================================"
echo "Modena, Italia - Map Poster Batch Generator"
echo "============================================================"
echo ""
echo "Generating 8 variations with bright themes..."
echo "City: Modena, Italia (44.6471° N, 10.9252° E)"
echo ""

# Counter for tracking progress
TOTAL=8
CURRENT=0

# Variation 1: Terracotta - 8000m
CURRENT=$((CURRENT+1))
echo "[$CURRENT/$TOTAL] Generating Terracotta (8000m - medium city view)..."
python create_map_poster.py -c "Modena" -C "Italia" -t terracotta -d 8000
echo ""

# Variation 2: Warm Beige - 6000m
CURRENT=$((CURRENT+1))
echo "[$CURRENT/$TOTAL] Generating Warm Beige (6000m - focused downtown)..."
python create_map_poster.py -c "Modena" -C "Italia" -t warm_beige -d 6000
echo ""

# Variation 3: Sunset - 10000m
CURRENT=$((CURRENT+1))
echo "[$CURRENT/$TOTAL] Generating Sunset (10000m - wider view)..."
python create_map_poster.py -c "Modena" -C "Italia" -t sunset -d 10000
echo ""

# Variation 4: Pastel Dream - 8000m
CURRENT=$((CURRENT+1))
echo "[$CURRENT/$TOTAL] Generating Pastel Dream (8000m - artistic medium)..."
python create_map_poster.py -c "Modena" -C "Italia" -t pastel_dream -d 8000
echo ""

# Variation 5: Autumn - 12000m
CURRENT=$((CURRENT+1))
echo "[$CURRENT/$TOTAL] Generating Autumn (12000m - large view)..."
python create_map_poster.py -c "Modena" -C "Italia" -t autumn -d 12000
echo ""

# Variation 6: Copper Patina - 5000m
CURRENT=$((CURRENT+1))
echo "[$CURRENT/$TOTAL] Generating Copper Patina (5000m - tight downtown)..."
python create_map_poster.py -c "Modena" -C "Italia" -t copper_patina -d 5000
echo ""

# Variation 7: Ocean - 8000m
CURRENT=$((CURRENT+1))
echo "[$CURRENT/$TOTAL] Generating Ocean (8000m - cool alternative)..."
python create_map_poster.py -c "Modena" -C "Italia" -t ocean -d 8000
echo ""

# Variation 8: Feature Based - 8000m
CURRENT=$((CURRENT+1))
echo "[$CURRENT/$TOTAL] Generating Feature Based (8000m - classic contrast)..."
python create_map_poster.py -c "Modena" -C "Italia" -t feature_based -d 8000
echo ""

echo "============================================================"
echo "✓ All $TOTAL variations generated successfully!"
echo "============================================================"
echo ""
echo "Generated posters are saved in the 'posters/' directory:"
ls -lh posters/modena_*.png | tail -n 8
echo ""
echo "To view all Modena variations:"
echo "  ls -1 posters/modena_*.png"
