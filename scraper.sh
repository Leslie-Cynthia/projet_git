response=$(curl -s "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=eur")

price=$(echo "$response" | grep -oP '"eur":\K[0-9]+(\.[0-9]+)?')

echo "Prix scrappe : $price EUR"


if [ ! -f data.csv ]; then
	echo "timestamp,price" > data.csv
fi

sed -i '/NAN/d' data.csv

echo "$(date '+%Y-%m-%d %H:%M:%S'),$price" >> data.csv

