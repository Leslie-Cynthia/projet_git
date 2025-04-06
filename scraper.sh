#!/bin/bash

# Absolute path to the CSV file
CSV="/home/frank/projet_git/data.csv"

# Call CoinGecko API
response=$(curl -s "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=eur")

# Extract the price from the API response
price=$(echo "$response" | grep -oP '"eur":\K[0-9]+(\.[0-9]+)?')

# Check if price is empty (e.g., API failure)
if [ -z "$price" ]; then
    echo "[WARNING $(date '+%Y-%m-%d %H:%M:%S')] Price not found. Skipping entry."
    exit 1
fi

# Create the CSV file if it doesn't exist
if [ ! -f "$CSV" ]; then
    echo "timestamp,price" > "$CSV"
fi

# Remove lines containing 'NAN'
sed -i '/NAN/d' "$CSV"

# Append the new entry to the CSV
echo "$(date '+%Y-%m-%d %H:%M:%S'),$price" >> "$CSV"

# Log confirmation to the console
echo "[INFO $(date '+%Y-%m-%d %H:%M:%S')] Price scraped: $price EUR added to data.csv"

