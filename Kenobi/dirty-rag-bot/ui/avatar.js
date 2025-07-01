const avatar = document.getElementById('avatar');

async function fetchState() {
  try {
    const res = await fetch('state.json?_=' + new Date().getTime());
    const data = await res.json();
    const mood = data.mood || 'idle';
    const nsfw = data.nsfw || false;

    let state = mood;
    if (nsfw && mood === 'flirty') {
      state = 'nsfw_bikini';
    } else if (nsfw && mood === 'aroused') {
      state = 'nsfw_nude';
    }

    const imgPath = `assets/${state}.png`;
    console.log(`[Avatar Debug] mood="${mood}", nsfw=${nsfw}, loading: ${imgPath}`);
    avatar.src = imgPath;
  } catch (e) {
    console.error("[Avatar Error]", e);
  }
}

fetchState();
setInterval(fetchState, 1000);
