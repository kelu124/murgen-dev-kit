for F in ./*.csv; do
  mv "$F" "$(md5sum "$F" | cut -d' ' -f1).${F##*.}";
done	

for F in ./*.csv; do
  bzip2 "$F";
done	
