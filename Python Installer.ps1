cd ..
cd ..

echo "Alterando Explorer"

Set-ItemProperty -Path "HKLM:\SOFTWARE\Microsoft\Internet Explorer\Main" -Name "DisableFirstRunCustomize" -Value 2
echo "Downloading Python"

wget https://www.python.org/ftp/python/3.11.0/python-3.11.0-amd64.exe

echo "Python Microsoft Store"
python