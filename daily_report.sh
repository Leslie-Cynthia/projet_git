#reading of data on data.csv

report=$(awk -F, -v today=$(date '+%Y-%m-%d') '
	BEGIN {
		min = ""; max =""; total = 0; count = 0;
	}
	NR > 1 && $1 ~ today {
		price = $2 + 0;
		prices[count] = price;
		if (min =="" || price < min) min = price;
		if (max =="" || price > max) max = price;
		total += price;
		count ++;
	}
	END {

		if (count>0) {
			avg = total / count;
			
			var=0;
			for(i=0; i < count; i++) {
				var += (prices[i] - avg)*(prices[i] - avg);
			}
			volatility = sqrt(var /count);

			printf "Daily report of the  %s\n Averagee: %.2f EUR \n Max: %.2f EUR\n Min: %.2f EUR\n", today, avg, max, min;
		}else {
			print "No data available today."}
		}
	}
 ' /home/frank/projet_git/data.csv)


echo "report" > /home/frank/projet_git/rapport_$(date '+%Y-%m-%d').txt

echo " Report generated with sucess : /home/frank/ptojet_git/rapport_$(date '+%Y-%m-%d').txt"



