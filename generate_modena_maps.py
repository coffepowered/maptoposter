#!/usr/bin/env python3
"""
Generate multiple map variations for Modena, Italia
This script bypasses the geocoding step by using hardcoded coordinates
"""

import osmnx as ox
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from tqdm import tqdm
import time
import os
from datetime import datetime

# Import functions from create_map_poster
import sys
sys.path.insert(0, os.path.dirname(__file__))

from create_map_poster import (
    load_theme, create_gradient_fade, get_edge_colors_by_type,
    get_edge_widths_by_type, load_fonts, THEMES_DIR, FONTS_DIR, POSTERS_DIR
)

# Modena, Italia coordinates
MODENA_COORDS = (44.6471, 10.9252)
CITY = "Modena"
COUNTRY = "Italia"

# Variations to generate (theme, distance, description)
VARIATIONS = [
    ("terracotta", 8000, "Mediterranean warmth - medium city view"),
    ("warm_beige", 6000, "Vintage aesthetic - focused downtown"),
    ("sunset", 10000, "Golden hour vibes - wider view"),
    ("pastel_dream", 8000, "Soft muted tones - medium view"),
    ("autumn", 12000, "Seasonal warmth - large view"),
    ("copper_patina", 5000, "Oxidized copper - tight downtown"),
    ("ocean", 8000, "Coastal blues - medium view"),
    ("feature_based", 8000, "Classic contrast - medium view"),
]

def generate_output_filename(city, theme_name):
    """Generate unique output filename with city, theme, and datetime."""
    if not os.path.exists(POSTERS_DIR):
        os.makedirs(POSTERS_DIR)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    city_slug = city.lower().replace(' ', '_')
    filename = f"{city_slug}_{theme_name}_{timestamp}.png"
    return os.path.join(POSTERS_DIR, filename)

def create_poster(city, country, point, dist, output_file, THEME, FONTS):
    print(f"\nGenerating map for {city}, {country}...")
    print(f"Theme: {THEME.get('name', 'Unknown')}")
    print(f"Distance: {dist}m")
    
    # Progress bar for data fetching
    with tqdm(total=3, desc="Fetching map data", unit="step", bar_format='{l_bar}{bar}| {n_fmt}/{total_fmt}') as pbar:
        # 1. Fetch Street Network
        pbar.set_description("Downloading street network")
        G = ox.graph_from_point(point, dist=dist, dist_type='bbox', network_type='all')
        pbar.update(1)
        time.sleep(0.5)
        
        # 2. Fetch Water Features
        pbar.set_description("Downloading water features")
        try:
            water = ox.features_from_point(point, tags={'natural': 'water', 'waterway': 'riverbank'}, dist=dist)
        except:
            water = None
        pbar.update(1)
        time.sleep(0.3)
        
        # 3. Fetch Parks
        pbar.set_description("Downloading parks/green spaces")
        try:
            parks = ox.features_from_point(point, tags={'leisure': 'park', 'landuse': 'grass'}, dist=dist)
        except:
            parks = None
        pbar.update(1)
    
    print("✓ All data downloaded successfully!")
    
    # Setup Plot
    print("Rendering map...")
    fig, ax = plt.subplots(figsize=(12, 16), facecolor=THEME['bg'])
    ax.set_facecolor(THEME['bg'])
    ax.set_position([0, 0, 1, 1])
    
    # Plot Layers
    if water is not None and not water.empty:
        water.plot(ax=ax, facecolor=THEME['water'], edgecolor='none', zorder=1)
    if parks is not None and not parks.empty:
        parks.plot(ax=ax, facecolor=THEME['parks'], edgecolor='none', zorder=2)
    
    # Roads with hierarchy coloring
    print("Applying road hierarchy colors...")
    edge_colors = get_edge_colors_by_type(G)
    edge_widths = get_edge_widths_by_type(G)
    
    ox.plot_graph(
        G, ax=ax, bgcolor=THEME['bg'],
        node_size=0,
        edge_color=edge_colors,
        edge_linewidth=edge_widths,
        show=False, close=False
    )
    
    # Gradients
    create_gradient_fade(ax, THEME['gradient_color'], location='bottom', zorder=10)
    create_gradient_fade(ax, THEME['gradient_color'], location='top', zorder=10)
    
    # Typography
    if FONTS:
        font_main = FontProperties(fname=FONTS['bold'], size=60)
        font_top = FontProperties(fname=FONTS['bold'], size=40)
        font_sub = FontProperties(fname=FONTS['light'], size=22)
        font_coords = FontProperties(fname=FONTS['regular'], size=14)
        font_attr = FontProperties(fname=FONTS['light'], size=8)
    else:
        font_main = FontProperties(family='monospace', weight='bold', size=60)
        font_top = FontProperties(family='monospace', weight='bold', size=40)
        font_sub = FontProperties(family='monospace', weight='normal', size=22)
        font_coords = FontProperties(family='monospace', size=14)
        font_attr = FontProperties(family='monospace', size=8)
    
    spaced_city = "  ".join(list(city.upper()))
    
    # Bottom text
    ax.text(0.5, 0.14, spaced_city, transform=ax.transAxes,
            color=THEME['text'], ha='center', fontproperties=font_main, zorder=11)
    
    ax.text(0.5, 0.10, country.upper(), transform=ax.transAxes,
            color=THEME['text'], ha='center', fontproperties=font_sub, zorder=11)
    
    lat, lon = point
    coords = f"{lat:.4f}° N / {lon:.4f}° E" if lat >= 0 else f"{abs(lat):.4f}° S / {lon:.4f}° E"
    if lon < 0:
        coords = coords.replace("E", "W")
    
    ax.text(0.5, 0.07, coords, transform=ax.transAxes,
            color=THEME['text'], alpha=0.7, ha='center', fontproperties=font_coords, zorder=11)
    
    ax.plot([0.4, 0.6], [0.125, 0.125], transform=ax.transAxes, 
            color=THEME['text'], linewidth=1, zorder=11)
    
    # Attribution
    ax.text(0.98, 0.02, "© OpenStreetMap contributors", transform=ax.transAxes,
            color=THEME['text'], alpha=0.5, ha='right', va='bottom', 
            fontproperties=font_attr, zorder=11)
    
    # Save
    print(f"Saving to {output_file}...")
    plt.savefig(output_file, dpi=300, facecolor=THEME['bg'])
    plt.close()
    print(f"✓ Done! Poster saved as {output_file}")

def main():
    print("=" * 60)
    print("Modena, Italia - Map Poster Generator")
    print("=" * 60)
    print(f"\nGenerating {len(VARIATIONS)} variations...")
    print(f"City: {CITY}, {COUNTRY}")
    print(f"Coordinates: {MODENA_COORDS[0]}° N, {MODENA_COORDS[1]}° E\n")
    
    FONTS = load_fonts()
    
    for i, (theme_name, distance, description) in enumerate(VARIATIONS, 1):
        print(f"\n{'='*60}")
        print(f"Variation {i}/{len(VARIATIONS)}: {theme_name} ({distance}m)")
        print(f"{'='*60}")
        
        try:
            # Load theme
            THEME = load_theme(theme_name)
            
            # Generate filename
            output_file = generate_output_filename(CITY, theme_name)
            
            # Create poster
            create_poster(CITY, COUNTRY, MODENA_COORDS, distance, output_file, THEME, FONTS)
            
            print(f"✓ Variation {i} complete!")
            
        except Exception as e:
            print(f"✗ Error creating variation {i}: {e}")
            import traceback
            traceback.print_exc()
            continue
    
    print(f"\n{'='*60}")
    print("✓ All variations complete!")
    print(f"{'='*60}")
    print(f"\nGenerated posters saved to: {POSTERS_DIR}/")

if __name__ == "__main__":
    main()
