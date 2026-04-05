---
created: 2024-05-22 
---


```python
from PIL import Image
import rmbg

img = Image.open('virat.png')
img
img_bg_removed = rembg.remove(img)
img_bg_removed
```

