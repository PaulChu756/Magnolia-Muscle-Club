npm ci >/dev/null
npm install cypress >/dev/null
apt-get update >/dev/null
apt-get install -y python3 python3-pip python3-venv >/dev/null
apt-get install -y libgtk2.0-0 libgtk-3-0 libgbm-dev libnotify-dev libgconf-2-4 libnss3 libxss1 libasound2 libxtst6 xauth xvfb >/dev/null
pip install -q virtualenv
python -m venv .venv
source .venv/bin/activate
pip install --upgrade -q pip
pip install --no-cache-dir -qr requirements.txt
python manage.py migrate >/dev/null
python manage.py collectstatic --no-input >/dev/null
