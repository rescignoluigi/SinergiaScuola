self.addEventListener("install", event => {
  console.log("Service worker installato");
});

self.addEventListener("fetch", event => {
  // Pass-through
});
