# Linux Assignment
%%bash --bg --out output
tail -20 -16 ~/mnt/data/public/gutenberg/1/6/6/1661/1661.txt

%%bash --bg --out output
cat /mnt/data/public/agora/Agora.csv | grep Drugs/Cannabis/Weed | wc -l

%%bash
rm -rf a
rm -rf d
rm -rf j
mkdir -p ./a/b/c
mkdir -p ./d/e/f
mkdir -p ./j/k/l

%%bash --bg --out output
ls -lrhS /mnt/data/public/amazon-reviews | tail -n -1

%%bash --bg --out output
find /mnt/data/public/millionsong/A -name "*A*.h5" | sort

%%bash --bg --out output
find /mnt/data/public/census -size +1000000c -exec ls -l {} + | tr -s ' '| cut -d ' ' -f 5,9,10,11 | sort

%%bash --bg --out output
cat /mnt/data/public/gdeltv2/masterfilelist.txt | cut -d ' ' -f 3 | grep 20190214080* | grep mentions

%%bash --bg --out output
cat /mnt/data/public/movielens/20m/ml-20m/tags.csv | cut -d ',' -f 3 | sort | uniq | wc -l

%%bash
cat /mnt/data/public/book-crossing/BX-Books.csv | grep -i pandemic |cut -d ';' -f 2 > ./pandemic-books.txt

