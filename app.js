/**
 * Toronto Opera Now - Frontend Engine (app.js)
 * Implements real-time filtering, search, view-swapping, and details modal.
 */

// Global State
let operaData = { companies: [] };
let activeCompanyFilter = null; // Company abbreviation
let activeMonthFilter = null;    // Format: "YYYY-MM" (e.g. "2026-06")
let searchQuery = "";
let currentView = "grid";        // "grid" or "calendar"

// Define our 12-Month Calendar window (May 2026 to May 2027)
const calendarMonths = [
    { name: "May 2026", key: "2026-05" },
    { name: "June 2026", key: "2026-06" },
    { name: "July 2026", key: "2026-07" },
    { name: "August 2026", key: "2026-08" },
    { name: "September 2026", key: "2026-09" },
    { name: "October 2026", key: "2026-10" },
    { name: "November 2026", key: "2026-11" },
    { name: "December 2026", key: "2026-12" },
    { name: "January 2027", key: "2027-01" },
    { name: "February 2027", key: "2027-02" },
    { name: "March 2027", key: "2027-03" },
    { name: "April 2027", key: "2027-04" },
    { name: "May 2027", key: "2027-05" }
];

// Document Elements
const globalSearchInput = document.getElementById("global-search");
const companiesFilterContainer = document.getElementById("companies-filter-container");
const monthSelectInput = document.getElementById("month-select");
const productionsGrid = document.getElementById("productions-grid-container");
const calendarTimelineContainer = document.getElementById("calendar-timeline-container");
const companyDirectoryContainer = document.getElementById("company-directory-container");

const btnGridView = document.getElementById("btn-grid-view");
const btnCalendarView = document.getElementById("btn-calendar-view");
const gridViewPanel = document.getElementById("grid-view-panel");
const calendarViewPanel = document.getElementById("calendar-view-panel");

const filterStatusBar = document.getElementById("filter-status-bar");
const filterStatusText = document.getElementById("filter-status-text");
const resetAllFiltersBtn = document.getElementById("reset-all-filters");
const clearCompanyFilterBtn = document.getElementById("clear-company-filter");
const clearMonthFilterBtn = document.getElementById("clear-month-filter");

// Modal Elements
const productionModal = document.getElementById("production-modal");
const modalCloseBtn = document.getElementById("modal-close-btn");
const modalCompanyLabel = document.getElementById("modal-company-name");
const modalTitle = document.getElementById("modal-title");
const modalComposer = document.getElementById("modal-composer");
const modalDateTime = document.getElementById("modal-date-time");
const modalVenue = document.getElementById("modal-venue");
const modalPrice = document.getElementById("modal-price");
const modalDescriptionText = document.getElementById("modal-description-text");
const modalTicketLink = document.getElementById("modal-ticket-link");
const modalWebsiteLink = document.getElementById("modal-website-link");
const modalImageContainer = document.getElementById("modal-image-container");

// Initialization
document.addEventListener("DOMContentLoaded", () => {
    initApp();
});

async function initApp() {
    try {
        const response = await fetch("data.json");
        if (!response.ok) throw new Error("Could not load data.json");
        operaData = await response.json();
        
        // Sort companies alphabetically (in case data.json wasn't fully sorted)
        operaData.companies.sort((a, b) => a.name.localeCompare(b.name));
        
        setupEventListeners();
        renderCompanyFilters();
        renderMonthTimeline();
        renderDirectory();
        updateDisplay();
    } catch (error) {
        console.error("Initialization error:", error);
        productionsGrid.innerHTML = `<div class="loading-spinner">Error loading data.json database. Please check console logs.</div>`;
    }
}

// Set up UI Event Listeners
function setupEventListeners() {
    // Search
    globalSearchInput.addEventListener("input", (e) => {
        searchQuery = e.target.value.toLowerCase().trim();
        updateDisplay();
    });

    // View toggles
    btnGridView.addEventListener("click", () => switchView("grid"));
    btnCalendarView.addEventListener("click", () => switchView("calendar"));

    // Clear filter buttons
    if (clearCompanyFilterBtn) {
        clearCompanyFilterBtn.addEventListener("click", () => {
            activeCompanyFilter = null;
            updateCompanyPills();
            updateDisplay();
        });
    }
    
    if (clearMonthFilterBtn) {
        clearMonthFilterBtn.addEventListener("click", () => {
            activeMonthFilter = null;
            updateMonthPills();
            updateDisplay();
        });
    }
    
    if (monthSelectInput) {
        monthSelectInput.addEventListener("change", (e) => {
            activeMonthFilter = e.target.value || null;
            updateDisplay();
        });
    }

    resetAllFiltersBtn.addEventListener("click", () => {
        activeCompanyFilter = null;
        activeMonthFilter = null;
        searchQuery = "";
        globalSearchInput.value = "";
        updateCompanyPills();
        updateMonthPills();
        updateDisplay();
    });

    // Modal close listeners
    modalCloseBtn.addEventListener("click", hideModal);
    productionModal.addEventListener("click", (e) => {
        if (e.target === productionModal) hideModal();
    });
    document.addEventListener("keydown", (e) => {
        if (e.key === "Escape") hideModal();
    });
}

function switchView(view) {
    currentView = view;
    const monthTimelineWrapper = document.getElementById("month-timeline-wrapper");
    
    if (view === "grid") {
        btnGridView.classList.add("active");
        btnGridView.setAttribute("aria-selected", "true");
        btnCalendarView.classList.remove("active");
        btnCalendarView.setAttribute("aria-selected", "false");
        
        gridViewPanel.style.display = "block";
        calendarViewPanel.style.display = "none";
        
        if (monthTimelineWrapper) {
            monthTimelineWrapper.style.display = "block";
        }
    } else {
        btnCalendarView.classList.add("active");
        btnCalendarView.setAttribute("aria-selected", "true");
        btnGridView.classList.remove("active");
        btnGridView.setAttribute("aria-selected", "false");
        
        calendarViewPanel.style.display = "block";
        gridViewPanel.style.display = "none";
        
        // Clear the month filter when switching to the full 12-month calendar view
        activeMonthFilter = null;
        updateMonthPills();
        
        if (monthTimelineWrapper) {
            monthTimelineWrapper.style.display = "none";
        }
    }
    updateDisplay();
}

// Render company filters row at top
function renderCompanyFilters() {
    if (!companiesFilterContainer) return;
    companiesFilterContainer.innerHTML = "";
    
    operaData.companies.forEach(company => {
        const pill = document.createElement("button");
        pill.className = "company-pill";
        pill.dataset.abbreviation = company.abbreviation;
        pill.innerHTML = `${company.name} <span style="font-size: 10px; opacity:0.6;">(${company.abbreviation})</span>`;
        
        pill.addEventListener("click", () => {
            if (activeCompanyFilter === company.abbreviation) {
                activeCompanyFilter = null; // Toggle off
            } else {
                activeCompanyFilter = company.abbreviation;
            }
            updateCompanyPills();
            updateDisplay();
        });
        companiesFilterContainer.appendChild(pill);
    });
}

function updateCompanyPills() {
    if (!companiesFilterContainer) return;
    const pills = companiesFilterContainer.querySelectorAll(".company-pill");
    pills.forEach(pill => {
        if (pill.dataset.abbreviation === activeCompanyFilter) {
            pill.classList.add("active");
        } else {
            pill.classList.remove("active");
        }
    });
}

// Render month timeline options in the select dropdown
function renderMonthTimeline() {
    if (!monthSelectInput) return;
    monthSelectInput.options.length = 1; // Clear all except "All Months"
    
    calendarMonths.forEach(m => {
        const count = getProductionCountForMonth(m.key);
        const opt = document.createElement("option");
        opt.value = m.key;
        opt.textContent = `${m.name} (${count} show${count !== 1 ? "s" : ""})`;
        monthSelectInput.appendChild(opt);
    });
}

function updateMonthPills() {
    if (monthSelectInput) {
        monthSelectInput.value = activeMonthFilter || "";
    }
}

function getProductionCountForMonth(monthKey) {
    let count = 0;
    operaData.companies.forEach(company => {
        company.productions.forEach(prod => {
            if (isProductionInMonth(prod, monthKey)) {
                count++;
            }
        });
    });
    return count;
}

function isProductionInMonth(prod, monthKey) {
    if (!prod.isoStart) return false;
    // Format of monthKey: "YYYY-MM"
    // Checks if production falls in this month.
    // If it is a multi-day show, it check if start month or end month matches the key.
    const startMonth = prod.isoStart.substring(0, 7);
    const endMonth = prod.isoEnd ? prod.isoEnd.substring(0, 7) : startMonth;
    return (monthKey >= startMonth && monthKey <= endMonth);
}

// Render full alphabetical company directory at bottom
function renderDirectory() {
    companyDirectoryContainer.innerHTML = "";
    
    operaData.companies.forEach(company => {
        const card = document.createElement("div");
        card.className = "dir-card";
        
        const hasUpcoming = company.productions.length > 0;
        const statusClass = hasUpcoming ? "status-active" : "status-inactive";
        const statusText = hasUpcoming ? "Active Season" : "No Upcoming Shows";
        
        let socialIcons = "";
        if (company.socials) {
            Object.entries(company.socials).forEach(([platform, url]) => {
                socialIcons += `
                    <a href="${url}" target="_blank" title="Follow on ${platform}">
                        <svg class="dir-social-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            ${getSocialIconPath(platform)}
                        </svg>
                    </a>
                `;
            });
        }
        
        card.innerHTML = `
            <div class="dir-header">
                <span class="dir-name">${company.name}</span>
                <span class="status-badge ${statusClass}">${statusText}</span>
            </div>
            <p class="dir-desc">${company.description}</p>
            <div class="dir-footer">
                <a href="${company.website}" target="_blank" class="dir-web-link">Visit Website →</a>
                <div class="dir-socials">${socialIcons}</div>
            </div>
        `;
        companyDirectoryContainer.appendChild(card);
    });
}

// Main logic to filter productions and update active panels
function updateDisplay() {
    let filteredList = [];
    
    operaData.companies.forEach(company => {
        // Skip if filtering by another company
        if (activeCompanyFilter && company.abbreviation !== activeCompanyFilter) return;
        
        company.productions.forEach(prod => {
            // Apply month filter
            if (activeMonthFilter && !isProductionInMonth(prod, activeMonthFilter)) return;
            
            // Apply search filter
            if (searchQuery) {
                const titleMatch = prod.title.toLowerCase().includes(searchQuery);
                const composerMatch = prod.composer.toLowerCase().includes(searchQuery);
                const venueMatch = prod.venue.toLowerCase().includes(searchQuery);
                const companyMatch = company.name.toLowerCase().includes(searchQuery);
                const descMatch = prod.description.toLowerCase().includes(searchQuery);
                if (!titleMatch && !composerMatch && !venueMatch && !companyMatch && !descMatch) return;
            }
            
            // Add reference to company for card rendering
            filteredList.push({
                ...prod,
                companyName: company.name,
                companyAbbr: company.abbreviation,
                companyWeb: company.website
            });
        });
    });
    
    // Sort productions by starting date
    filteredList.sort((a, b) => new Date(a.isoStart) - new Date(b.isoStart));
    
    // Update Filter Status Info
    const isFiltered = activeCompanyFilter || activeMonthFilter || searchQuery;
    if (isFiltered) {
        filterStatusBar.style.display = "flex";
        filterStatusText.textContent = `Found ${filteredList.length} matching production${filteredList.length !== 1 ? "s" : ""}`;
    } else {
        filterStatusBar.style.display = "none";
    }
    
    // Update timelines and months counts
    updateTimelineCounts();
    
    // Update filter buttons visibility
    updateFilterButtons();
    
    // Render current view
    if (currentView === "grid") {
        renderGridPanel(filteredList);
    } else {
        renderCalendarPanel(filteredList);
    }
}

function updateTimelineCounts() {
    if (!monthSelectInput) return;
    calendarMonths.forEach((m, idx) => {
        let count = 0;
        operaData.companies.forEach(company => {
            if (activeCompanyFilter && company.abbreviation !== activeCompanyFilter) return;
            company.productions.forEach(prod => {
                if (isProductionInMonth(prod, m.key)) {
                    if (searchQuery) {
                        const titleMatch = prod.title.toLowerCase().includes(searchQuery);
                        const composerMatch = prod.composer.toLowerCase().includes(searchQuery);
                        const venueMatch = prod.venue.toLowerCase().includes(searchQuery);
                        const companyMatch = company.name.toLowerCase().includes(searchQuery);
                        const descMatch = prod.description.toLowerCase().includes(searchQuery);
                        if (!titleMatch && !composerMatch && !venueMatch && !companyMatch && !descMatch) return;
                    }
                    count++;
                }
            });
        });
        
        // Option index is idx + 1 because index 0 is the "All Months" placeholder
        const option = monthSelectInput.options[idx + 1];
        if (option) {
            option.textContent = `${m.name} (${count} show${count !== 1 ? "s" : ""})`;
        }
    });
}

// Render Grid panel cards
function renderGridPanel(productions) {
    productionsGrid.innerHTML = "";
    
    if (productions.length === 0) {
        productionsGrid.innerHTML = `<div class="loading-spinner">No upcoming productions found matching your filters. Try resetting search parameters.</div>`;
        return;
    }
    
    productions.forEach((prod, index) => {
        const card = document.createElement("div");
        card.className = "prod-card";
        
        card.innerHTML = `
            <div class="card-img-wrap">
                <img src="${prod.imageLink}" alt="${prod.title}" onerror="this.src='https://images.squarespace-cdn.com/content/v1/66900b857cbcd75ecec7aebb/76c5f834-b81a-4593-a1ec-3a56fc73f5e7/Toronto+Opera+Festival+26+bannertickets+on+sale.png'">
                <span class="card-company-tag">${prod.companyAbbr}</span>
            </div>
            <div class="card-content">
                <span class="card-composer">${prod.composer}</span>
                <h3 class="card-title">${prod.title}</h3>
                
                <div class="card-meta-list">
                    <div class="card-meta-item">
                        <svg class="meta-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect>
                            <line x1="16" y1="2" x2="16" y2="6"></line>
                            <line x1="8" y1="2" x2="8" y2="6"></line>
                            <line x1="3" y1="10" x2="21" y2="10"></line>
                        </svg>
                        <span>${prod.date}</span>
                    </div>
                    <div class="card-meta-item">
                        <svg class="meta-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path>
                            <circle cx="12" cy="10" r="3"></circle>
                        </svg>
                        <span>${prod.venue}</span>
                    </div>
                </div>
                
                <div class="card-actions">
                    <button class="cta-btn secondary-btn view-details-trigger">Details</button>
                    <a href="${prod.ticketLink}" target="_blank" class="cta-btn book-tickets-btn">Tickets</a>
                </div>
            </div>
        `;
        
        // Add detail modal event listener
        card.querySelector(".view-details-trigger").addEventListener("click", () => {
            showModal(prod);
        });
        
        productionsGrid.appendChild(card);
    });
}

// Render Calendar panel listings
function renderCalendarPanel(productions) {
    calendarTimelineContainer.innerHTML = "";
    
    // We display months chronologically
    calendarMonths.forEach(m => {
        const monthSection = document.createElement("div");
        monthSection.className = "cal-month-section";
        
        // Filter productions for this specific month
        const monthEvents = productions.filter(prod => isProductionInMonth(prod, m.key));
        
        const countBadge = monthEvents.length > 0 
            ? `<span class="cal-month-count">${monthEvents.length} event${monthEvents.length !== 1 ? "s" : ""}</span>` 
            : "";
            
        monthSection.innerHTML = `
            <div class="cal-month-header">
                <span class="cal-month-title">${m.name}</span>
                ${countBadge}
            </div>
            <div class="cal-events-list">
                <!-- Events filled here -->
            </div>
        `;
        
        const eventsList = monthSection.querySelector(".cal-events-list");
        
        if (monthEvents.length === 0) {
            eventsList.innerHTML = `<div class="cal-month-empty">No scheduled productions this month.</div>`;
        } else {
            monthEvents.forEach(prod => {
                const eventRow = document.createElement("div");
                eventRow.className = "cal-event-row";
                
                // Parse date box digits
                const dateObj = new Date(prod.isoStart);
                const dayDigit = dateObj.getDate() || "—";
                const mName = dateObj.toLocaleString("en-US", { month: "short" }) || "";
                
                eventRow.innerHTML = `
                    <div class="cal-event-date-box">
                        <span class="day">${dayDigit}</span>
                        <span class="month-abbr">${mName}</span>
                    </div>
                    <div class="cal-event-info">
                        <div class="cal-event-company">${prod.companyName}</div>
                        <div class="cal-event-title-composer">
                            <span class="cal-event-title">${prod.title}</span>
                            <span class="cal-event-composer">by ${prod.composer}</span>
                        </div>
                        <div class="cal-event-meta">
                            <span>🕒 ${prod.time || "Time TBA"}</span>
                            <span>📍 ${prod.venue}</span>
                            <span>🎟️ ${prod.price || "Check site"}</span>
                        </div>
                    </div>
                    <div class="cal-event-action">
                        <button class="cta-btn secondary-btn details-btn cal-details-trigger">Details</button>
                    </div>
                `;
                
                eventRow.querySelector(".cal-details-trigger").addEventListener("click", () => {
                    showModal(prod);
                });
                
                eventsList.appendChild(eventRow);
            });
        }
        
        calendarTimelineContainer.appendChild(monthSection);
    });
}

// Modal Interaction
function showModal(prod) {
    modalCompanyLabel.textContent = prod.companyName;
    modalTitle.textContent = prod.title;
    modalComposer.textContent = prod.composer;
    modalDateTime.textContent = `${prod.date} (${prod.time})`;
    modalVenue.textContent = `${prod.venue} — ${prod.address}`;
    modalPrice.textContent = prod.price || "Check details on ticketing site";
    modalDescriptionText.textContent = prod.description;
    
    modalTicketLink.href = prod.ticketLink;
    modalWebsiteLink.href = prod.companyWeb;
    
    modalImageContainer.innerHTML = `
        <img src="${prod.imageLink}" alt="${prod.title}" onerror="this.src='https://images.squarespace-cdn.com/content/v1/66900b857cbcd75ecec7aebb/76c5f834-b81a-4593-a1ec-3a56fc73f5e7/Toronto+Opera+Festival+26+bannertickets+on+sale.png'">
        <span class="card-company-tag" style="top:20px; left:20px;">${prod.companyAbbr}</span>
    `;
    
    productionModal.classList.add("show");
    document.body.style.overflow = "hidden"; // Disable background scrolling
}

function hideModal() {
    productionModal.classList.remove("show");
    document.body.style.overflow = ""; // Re-enable scrolling
}

// Icons Helper
function getSocialIconPath(platform) {
    switch (platform) {
        case "twitter":
            return `
                <path d="M23 3a10.9 10.9 0 0 1-3.14 1.53 4.48 4.48 0 0 0-7.86 3v1A10.66 10.66 0 0 1 3 4s-4 9 5 13a11.64 11.64 0 0 1-7 2c9 5 20 0 20-11.5a4.5 4.5 0 0 0-.08-.83A7.72 7.72 0 0 0 23 3z"></path>
            `;
        case "facebook":
            return `
                <path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"></path>
            `;
        case "instagram":
            return `
                <rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect>
                <path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path>
                <line x1="17.5" y1="6.5" x2="17.51" y2="6.5"></line>
            `;
        case "youtube":
            return `
                <path d="M22.54 6.42a2.78 2.78 0 0 0-1.95-1.96C18.88 4 12 4 12 4s-6.88 0-8.59.46a2.78 2.78 0 0 0-1.95 1.96A29 29 0 0 0 1 11.75a29 29 0 0 0 .46 5.33A2.78 2.78 0 0 0 3.41 19c1.71.46 8.59.46 8.59.46s6.88 0 8.59-.46a2.78 2.78 0 0 0 1.95-1.96 29 29 0 0 0 .46-5.33 29 29 0 0 0-.46-5.33z"></path>
                <polygon points="9.75 15.02 15.5 11.75 9.75 8.48 9.75 15.02"></polygon>
            `;
        default:
            return `
                <circle cx="12" cy="12" r="10"></circle>
                <line x1="2" y1="12" x2="22" y2="12"></line>
                <path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path>
            `;
    }
}

// Update the visibility of company and month filter clear buttons dynamically
function updateFilterButtons() {
    if (clearCompanyFilterBtn) {
        clearCompanyFilterBtn.style.display = activeCompanyFilter ? "inline-block" : "none";
    }
    if (clearMonthFilterBtn) {
        // Only show the month clear button if a month filter is active in grid view
        clearMonthFilterBtn.style.display = (currentView === "grid" && activeMonthFilter) ? "inline-block" : "none";
    }
}
