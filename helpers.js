// function scrollToBottom() {
//   return new Promise((resolve, reject) => {
//     try {
//         setTimeout(() => {
//           const scrollHeight = document.body.scrollHeight;
//           window.scrollTo(0, scrollHeight);
//           resolve();
//         }, 1000);

//     } catch (error) {
//       reject(error);
//     }
//   });
// }

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

function waitForAssetLoad() {
  return new Promise((resolve) => {
    if (document.readyState === "complete") {
      resolve();
    } else {
      window.addEventListener("load", () => resolve());
    }
  });
}

window.scrollToBottom = scrollToBottom;
window.waitForAssetLoad = waitForAssetLoad;
