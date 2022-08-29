# BinancePremiums

![screenshot](assets/screenshot.png)


BinancePremiums is a simple tool to track crypto spot-perp premia on Binance.

-   `data_downloader.py` scrapes data from binance
-   `dashboard.py` is the main dashboard
-   `content/` for markdown files called by `dashboard`.

I originally deployed this on heroku, but now they are killing the free plans so I am using Streamlit Cloud. 




## Heroku deployment

Heroku deployment following [this](https://towardsdatascience.com/a-quick-tutorial-on-how-to-deploy-your-streamlit-app-to-heroku-874e1250dadd) tutorial.

Scheduled restarts ([SO](https://stackoverflow.com/questions/43926740/schedule-heroku-to-restart-dynos-every-10-or-so-minutes)):

```
curl -n -X DELETE https://api.heroku.com/apps/binancepremiums/dynos \n -H "Content-Type: application/json" \n -H "Accept: application/vnd.heroku+json; version=3" \n -H "Authorization: Bearer 4c136a81-9889-4267-9f65-325b6b1ce8d2"
```<!--  -->

binance2Premiums

DO steps:

ssh root@ip

apt upgrade
apt install python3-pip
git clone https://github.com/robertmartin8/BinancePremiums
cd BinancePremiums
pip3 install -r requirements.txt

tmux
`ctrl b c` to create new
`ctrl b 0-9` to swap between

python3 fix_streamlit.py
streamlit run dashboard.py --server.headless=true --server.enableCORS=false

## Setting up HTTPS

control panel -> manage -> networking -> domains.

https://www.digitalocean.com/community/questions/how-to-protect-a-website-droplet-with-https

https://www.digitalocean.com/community/tutorials/how-to-secure-nginx-with-let-s-encrypt-on-ubuntu-18-04
