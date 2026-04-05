---
created: 2025-01-23
---

Paste the following code in the 'javascript console', available through clicking F12 in both Firefox and Chrome.

The script goes through all link elements in the page, checks if they are video urls, puts them as associative array (to eliminate duplicates), then runs through that associative array again to collect all of the video urls. Finally the script generates a DataUrl which it puts into an invisible link on the webpage and then calls .click() on that invisible link, so your browser pop-ups a window to download video list as txt file.
Note: if you got like 1300 videos in your watch later playlist like me, you should first scroll down the watch later playlist for a while until all video thumbnails/links have been loaded. Then execute the script to get all video urls.



```js
var videoObj = new Object();

for(var links=document.getElementsByTagName("a"), i=0; i < links.length; ++i)

  if(links[i] && links[i].href && links[i].href.match(/\/watch\?v=[-_a-zA-Z0-9]/))

    videoObj[links[i].href.replace(/&.*/,"")] = "1";

var videolist = "";

for(var attr in videoObj) videolist+= attr + "\n";

var dataUrl = URL.createObjectURL( new Blob([videolist], { type: "text/txt;charset: utf-8;"}));

var dlLink = document.createElement("a");

dlLink.href = dataUrl;

dlLink.download = "youtube-video-ids.txt";

dlLink=document.body.appendChild(dlLink);

dlLink.click();
```