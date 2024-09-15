var staticCacheName = "django-pwa-v" + new Date().getTime();
var filesToCache = [
    '/offline/',
    "https://cdn.jsdelivr.net/npm/bootstrap-icons@1.7.2/font/bootstrap-icons.css",
    "https://cdn.jsdelivr.net/npm/halfmoon@2.0.1/css/halfmoon.min.css",
    "https://code.jquery.com/jquery-3.7.1.min.js",
    '/static/assets/css/halfmoon-2.0.1/cores/halfmoon.poisonwiki.css',
    '/static/assets/js/htmx.min.js',
    // '/static/assets/js/recorder.js',
    '/static/assets/js/main.js',
    '/static/assets/js/landing.js',
    '/static/assets/imgs/LogoTeraScience.png',
    '/static/assets/imgs/favicon.ico',
    '/static/assets/imgs/tera_icon.png',
    '/static/images/icons/icon-72x72.png',
    '/static/images/icons/icon-96x96.png',
    '/static/images/icons/icon-128x128.png',
    '/static/images/icons/icon-144x144.png',
    '/static/images/icons/icon-152x152.png',
    '/static/images/icons/icon-192x192.png',
    '/static/images/icons/icon-384x384.png',
    '/static/images/icons/icon-512x512.png',
    '/static/images/icons/splash-640x1136.png',
    '/static/images/icons/splash-750x1334.png',
    '/static/images/icons/splash-1242x2208.png',
    '/static/images/icons/splash-1125x2436.png',
    '/static/images/icons/splash-828x1792.png',
    '/static/images/icons/splash-1242x2688.png',
    '/static/images/icons/splash-1536x2048.png',
    '/static/images/icons/splash-1668x2224.png',
    '/static/images/icons/splash-1668x2388.png',
    '/static/images/icons/splash-2048x2732.png'
];

// Cache on install
self.addEventListener("install", event => {
    self.skipWaiting();
    event.waitUntil(
        caches.open(staticCacheName)
            .then(cache => {
                return cache.addAll(filesToCache);
            })
    );
});

// Clear cache on activate
self.addEventListener('activate', event => {
    event.waitUntil(
        caches.keys().then(cacheNames => {
            return Promise.all(
                cacheNames
                    .filter(cacheName => (cacheName.startsWith("django-pwa-")))
                    .filter(cacheName => (cacheName !== staticCacheName))
                    .map(cacheName => caches.delete(cacheName))
            );
        })
    );
    self.clients.claim(); // Ensure that the latest service worker is controlling the clients
});

// Extract cookies from request headers
function getCookieFromHeaders(headers, name) {
    let cookieValue = null;
    const cookies = headers.get('cookie');
    if (cookies) {
        const cookieArray = cookies.split(';');
        cookieArray.forEach(cookie => {
            const [cookieName, cookieVal] = cookie.trim().split('=');
            if (cookieName === name) {
                cookieValue = decodeURIComponent(cookieVal);
            }
        });
    }
    return cookieValue;
}

// Fetch event
self.addEventListener("fetch", event => {
    const clearCacheCookie = getCookieFromHeaders(event.request.headers, 'clear-cache');

    if (clearCacheCookie === 'true') {
        console.log('Clearing cache');
        event.waitUntil(
            caches.keys().then(cacheNames => {
                return Promise.all(
                    cacheNames.map(cacheName => {
                        if (cacheName.startsWith("django-pwa-v")) {
                            return caches.delete(cacheName);
                        }
                    })
                );
            })
        );
    }

    // Only handle GET requests
    if (event.request.method === 'GET') {
        // Check if the request is for a static file
        if (filesToCache.some(file => event.request.url.includes(file))) {
            event.respondWith(
                // Stale-while-revalidate
                caches.match(event.request).then(response => {
                    return response || fetch(event.request).then(networkResponse => {
                        return caches.open(staticCacheName).then(cache => {
                            cache.put(event.request, networkResponse.clone());
                            return networkResponse;
                        });
                    });
                }).catch(() => {
                    return caches.match('/offline/');
                })
            );
        } else {
            // Always fetch pages from the server
            event.respondWith(
                fetch(event.request).catch(() => {
                    return caches.match('/offline/');
                })
            );
        }
    } else {
        // For non-GET requests, do not use cache, just fetch from network
        event.respondWith(fetch(event.request));
    }
});

// Check for updates periodically
setInterval(() => {
    self.registration.update(); // Check for new service worker versions and install them
}, 60 * 60 * 1000); // Check every hour
