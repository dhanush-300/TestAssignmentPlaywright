def apply_stealth(context):
    # Hide navigator.webdriver
    context.add_init_script("""
        Object.defineProperty(navigator, 'webdriver', {
            get: () => undefined
        });
    """)

    # Remove Chrome runtime fingerprint
    context.add_init_script("""
        // Remove window.chrome
        Object.defineProperty(window, 'chrome', {
            get: () => undefined
        });
    """)

    # Fake plugins
    context.add_init_script("""
        Object.defineProperty(navigator, 'plugins', {
            get: () => [1, 2, 3, 4, 5]
        });
    """)

    # Fake languages
    context.add_init_script("""
        Object.defineProperty(navigator, 'languages', {
            get: () => ['en-US', 'en']
        });
    """)

    # Patch permissions (notifications)
    context.add_init_script("""
        const originalQuery = window.navigator.permissions.query;
        window.navigator.permissions.query = (parameters) => (
            parameters.name === 'notifications'
                ? Promise.resolve({ state: 'denied' })
                : originalQuery(parameters)
        );
    """)

    # Fake WebGL vendor
    context.add_init_script("""
        const getParameter = WebGLRenderingContext.prototype.getParameter;
        WebGLRenderingContext.prototype.getParameter = function(parameter) {
            if (parameter === 37445) return 'Intel Inc.'; // UNMASKED_VENDOR_WEBGL
            if (parameter === 37446) return 'Intel Iris OpenGL Engine'; // UNMASKED_RENDERER_WEBGL
            return getParameter(parameter);
        };
    """)

    # Spoof user agent hints
    context.add_init_script("""
        Object.defineProperty(navigator, 'userAgentData', {
            get: () => ({
                brands: [{ brand: "Google Chrome", version: "120" }],
                mobile: false,
                platform: "Windows"
            })
        });
    """)