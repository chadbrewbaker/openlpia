today=$(date "+%m_%d_%y")
mkdir -p  $today
cd $today
wget -nc --random-wait http://www.assess.co.polk.ia.us/web/exports/basic/resAllI.html
wget -nc --random-wait http://www.assess.co.polk.ia.us/web/exports/resA/inven/POLKCOUNTY.txt -O resPolkInv.txt

wget -nc --random-wait http://www.assess.co.polk.ia.us/web/exports/basic/commAllS.html
wget -nc --random-wait http://www.assess.co.polk.ia.us/web/exports/commA/sales/POLKCOUNTY.txt -O commPolkSales.txt

wget -nc --random-wait http://www.assess.co.polk.ia.us/web/exports/basic/commAllI.html
wget -nc --random-wait http://www.assess.co.polk.ia.us/web/exports/commA/inven/POLKCOUNTY.txt -O commPolkInv.txt

wget -nc --random-wait http://www.assess.co.polk.ia.us/web/exports/basic/agAllS.html
wget -nc --random-wait http://www.assess.co.polk.ia.us/web/exports/agA/sales/POLKCOUNTY.txt -O agPolkSales.txt
wget -nc --random-wait http://www.assess.co.polk.ia.us/web/exports/basic/agAllI.html
wget -nc --random-wait http://www.assess.co.polk.ia.us/web/exports/agA/inven/POLKCOUNTY.txt -O agPolkInv.txt

mkdir -p resPolkSales2016
cd resPolkSales2016
wget -nc -e robots=off --random-wait -r -nd --accept-regex ".*\.txt" 'http://www.assess.co.polk.ia.us/web/exports/res/sales/2016/'
cd ..
mkdir -p resPolkSales2017
wget -nc -e robots=off --random-wait  -r -nd --accept-regex ".*\.txt" 'http://www.assess.co.polk.ia.us/web/exports/res/sales/2017/'
cd ..
cd ..
