Note: move 

img-to-zoomable-link.py
jpp-example.md
pandoc.css

outside the highslide dir, eg:

./highslide/highslide.js
./highslide/graphics/
./img-to-zoomable-link.py
./jpp-example.md
./pandoc.css







---
title: Ben Bales' Diablo 2 Bot
header-includes:
    <meta name="keywords" content="MachineLearning,Diablo2,TensorFlow" />
    <meta name="description" content="Use machine learning to shoot bad guys in Diablo 2" />
    <script type="text/javascript" src="highslide/highslide.js" ></script>
---


{
    "shell_cmd": "pandoc -s --toc -f markdown -t html --filter img-to-zoomable-link.py -c pandoc.css -o \"$file_base_name.html\" \"$file_name\" && open \"$file_base_name.html\""   

}
