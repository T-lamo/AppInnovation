# Seting up duckling 
## wget -qO- https://get.haskellstack.org/ | sh 
## sudo apt install libicu-dev
## sudo apt install libpcre3-dev
## git clone git@github.com:facebook/duckling.git
## stack build
## stack exec duckling-example-exe 
## curl -XPOST http://0.0.0.0:8000/parse --data 'locale=en_GB&text=tomorrow at eight I had 7 euros and 2 cents yesterday' | python -m json.tool

curl -XPOST http://duckling.rasa.com:8000 --data 'locale=en_GB&text=tomorrow at eight I had 7 euros and 2 cents yesterday'
## https://gist.github.com/dainiusjocas/74ddfbca05d7ff68c230747fbf311a3e
## https://github.com/duckling-python-wrapper/fb_duckling


## https://rasa.com/docs/rasa/components/#ducklingentityextractor
### sudo docker run -p 8000:8000 rasa/duckling