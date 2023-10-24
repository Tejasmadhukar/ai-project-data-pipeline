<p align="center">
<h1 align="center">Data Pipeline</h1>
  <p align="center">
    A simple data pipeline for youtube comments chrome extension
    <br/>
  </p>
</p>

</br>

## How to use 

### Use standalone 

Clone the repo

```
git clone https://github.com/Tejasmadhukar/ai-project-data-pipeline.git
cd DocumentQuerying
```

Add youtube video id of videos to <strong>videos.csv</strong> of which you wish to download commments. 

Now Just install requirements 

``` 
pip install -r requirements.txt
```

Run the script 
```
chmod +x script.sh
./script.sh
```

Comments will be downloaded in /downloaded_comments directorty and 1000 comments will be downloaded by default sorted by most Popular.