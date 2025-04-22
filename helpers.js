function scrollToBottom(speed = 100, step = 100) {
  return new Promise((resolve, reject) => {
    try {
      const scrollInterval = setInterval(() => {
        const currentScroll = window.scrollY;
        const maxScroll = document.body.scrollHeight - window.innerHeight;

        if (currentScroll < maxScroll) {
          window.scrollBy(0, step);
        } else {
          clearInterval(scrollInterval); // stop when bottom is reached
          resolve();
        }
      }, speed);
    } catch (error) {
      reject(error);
    }
  });
}

function setPageZoom(zoom) {
  document.body.style.zoom = `${zoom}%`;
}

window.setPageZoom = setPageZoom;
window.scrollToBottom = scrollToBottom;
