# TILEIFY 

<div class="gif-container">
  <!-- All three GIFs are loaded together when the page loads -->
  <img src="widecat_tiles/widecat_0_0.gif" alt="First GIF" id="gif1">
  <img src="widecat_tiles/widecat_0_1.gif" alt="Second GIF" id="gif2">
  <img src="widecat_tiles/widecat_0_2.gif" alt="Third GIF" id="gif3">
</div>

<script>
  // This script ensures the GIFs start together
  window.onload = function() {
    // Get all GIF elements
    const gif1 = document.getElementById('gif1');
    const gif2 = document.getElementById('gif2');
    const gif3 = document.getElementById('gif3');
    
    // Force reload of all GIFs simultaneously to synchronize them
    gif1.src = gif1.src;
    gif2.src = gif2.src;
    gif3.src = gif3.src;
  }
</script>

> Tool to convert images into a collage of emojis.
> Credit Rutvik Choudhary (@rchoudhary, rutvikc2@illinois.edu) for the initial script.
> Optimized and improved by Evan Matthews (@ematth, evanmm3@illinois.edu)

## Directions
- Clone this repo with `git clone https://github.com/ematth/tileify.git`
- run script with `python3 tileify.py path/to/image`
- Output appears in `name_tiles/` directory, labeled by `name_row_column`
- Upload directory to slack, enjoy your multi-tile emoji :)
