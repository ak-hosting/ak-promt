// Analytics and Tracking for AI Guide

// Google Analytics 4
function initGA() {
    if (typeof gtag !== 'undefined') {
        gtag('config', 'G-XXXXXXXXXX', {
            page_title: document.title,
            page_location: window.location.href
        });
    }
}

// Custom Event Tracking
function trackEvent(eventName, parameters = {}) {
    if (typeof gtag !== 'undefined') {
        gtag('event', eventName, parameters);
    }
    
    // Console logging for development
    console.log('Event tracked:', eventName, parameters);
}

// Page View Tracking
function trackPageView(pageName) {
    trackEvent('page_view', {
        page_name: pageName,
        page_url: window.location.href
    });
}

// Feature Usage Tracking
function trackFeatureUsage(featureName, action = 'view') {
    trackEvent('feature_usage', {
        feature_name: featureName,
        action: action,
        timestamp: new Date().toISOString()
    });
}

// Prompt Usage Tracking
function trackPromptUsage(promptId, platform) {
    trackEvent('prompt_usage', {
        prompt_id: promptId,
        platform: platform,
        timestamp: new Date().toISOString()
    });
}

// Search Tracking
function trackSearch(searchTerm, resultsCount) {
    trackEvent('search', {
        search_term: searchTerm,
        results_count: resultsCount
    });
}

// Error Tracking
function trackError(errorMessage, errorStack) {
    trackEvent('error', {
        error_message: errorMessage,
        error_stack: errorStack,
        page_url: window.location.href
    });
}

// Performance Tracking
function trackPerformance(metricName, value) {
    trackEvent('performance', {
        metric_name: metricName,
        value: value
    });
}

// Initialize Analytics
document.addEventListener('DOMContentLoaded', function() {
    initGA();
    trackPageView(document.title);
    
    // Track navigation
    document.querySelectorAll('a[href^="/"]').forEach(link => {
        link.addEventListener('click', function() {
            trackEvent('navigation', {
                from_page: window.location.pathname,
                to_page: this.getAttribute('href')
            });
        });
    });
    
    // Track form submissions
    document.querySelectorAll('form').forEach(form => {
        form.addEventListener('submit', function() {
            trackEvent('form_submit', {
                form_id: this.id || 'unknown',
                form_action: this.action
            });
        });
    });
    
    // Track button clicks
    document.querySelectorAll('button').forEach(button => {
        button.addEventListener('click', function() {
            trackEvent('button_click', {
                button_text: this.textContent.trim(),
                button_class: this.className
            });
        });
    });
});

// Export functions for use in other scripts
window.Analytics = {
    trackEvent,
    trackPageView,
    trackFeatureUsage,
    trackPromptUsage,
    trackSearch,
    trackError,
    trackPerformance
}; 