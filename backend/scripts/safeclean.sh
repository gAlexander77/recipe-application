if [ -d ../scripts ]; then echo "chdir"; cd ..; fi

find . -type d -name __pycache__ -exec rm -rf {} +
rm -rf uploads
rm -f db/db.sqlite3
