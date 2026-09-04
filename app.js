document.addEventListener("DOMContentLoaded", () => {
    const data = window.feedbackData || (typeof feedbackData !== "undefined" ? feedbackData : []);
    const totalScraped = data.length || 1500;

    // Update Header Badge
    const scrapedElem = document.getElementById("scrapedTotal");
    if (scrapedElem) scrapedElem.innerText = totalScraped.toLocaleString();

    // Channel Sources Breakdown Calculation
    const sourceCounts = {};
    data.forEach(item => {
        const src = item.source || item.Source || "Other";
        sourceCounts[src] = (sourceCounts[src] || 0) + 1;
    });

    const sourcesTableBody = document.getElementById("sourcesTableBody");
    if (sourcesTableBody && Object.keys(sourceCounts).length > 0) {
        sourcesTableBody.innerHTML = "";
        Object.entries(sourceCounts).forEach(([src, count]) => {
            const pct = ((count / totalScraped) * 100).toFixed(1);
            const row = document.createElement("tr");
            row.innerHTML = `
                <td>${src}</td>
                <td><strong>${count}</strong></td>
                <td>
                    <span style="font-size: 11px; color: var(--text-muted);">${pct}%</span>
                    <div class="bar-container">
                        <div class="bar-fill" style="width: ${pct}%"></div>
                    </div>
                </td>
            `;
            sourcesTableBody.appendChild(row);
        });
    }

    // Dynamic Decision Friction Landscape Bars Calculation
    const catCounts = {};
    data.forEach(d => {
        const cat = d.primary_category || d.category_tag || "Other / Emerging";
        catCounts[cat] = (catCounts[cat] || 0) + 1;
    });

    const cssChartBars = document.getElementById("cssChartBars");
    if (cssChartBars) {
        cssChartBars.innerHTML = "";
        const sortedCats = Object.entries(catCounts).sort((a, b) => b[1] - a[1]);
        sortedCats.forEach(([catName, count]) => {
            const pct = ((count / totalScraped) * 100).toFixed(1);
            const barRow = document.createElement("div");
            barRow.className = "css-chart-bar";
            barRow.innerHTML = `
                <div class="css-chart-label" title="${catName}">${catName}</div>
                <div class="css-chart-track"><div class="css-chart-fill" style="width: ${pct}%;"></div></div>
                <div class="css-chart-val">${pct}% (${count})</div>
            `;
            cssChartBars.appendChild(barRow);
        });
    }

    // Feed & Pagination Setup
    const feedContainer = document.getElementById("feedbackFeed");
    const searchInput = document.getElementById("searchBar");
    const catSelect = document.getElementById("catFilter");
    const barrierSelect = document.getElementById("barrierFilter");
    const resultsCountBadge = document.getElementById("resultsCount");
    const loadMoreBtn = document.getElementById("loadMoreBtn");

    let filteredItems = [...data];
    let currentRenderLimit = 30;

    function renderFeedCard(item) {
        const card = document.createElement("div");
        card.className = "feed-card";
        
        const barrierClass = item.barrier_level === "High" ? "pill-barrier-high" : (item.barrier_level === "Medium" ? "pill-barrier-medium" : "pill-barrier-low");
        const sentClass = item.sentiment === "Negative" ? "pill-sent-neg" : (item.sentiment === "Positive" ? "pill-sent-pos" : "pill-sent-neu");
        const evClass = item.evidence_type && item.evidence_type.includes("Verbatim") ? "pill-verbatim" : (item.evidence_type && item.evidence_type.includes("Paraphrase") ? "pill-paraphrase" : "pill-inference");
        
        let srcUrl = item.source_url || item.Original_URL || '#';
        if (String(srcUrl).toLowerCase() === 'nan') srcUrl = '#';

        let painPoint = item.primary_pain_point || item.Friction_tags || ((item.primary_category || 'General') + " Friction");
        let confScore = item.confidence_score || item.AI_confidence || 0.95;
        let commentText = item.comment || item.Raw_text || "";

        card.innerHTML = `
            <div class="card-meta">
                <span class="source-tag">${item.source || item.Source}</span>
                <span>Segment: <strong>${item.behavioral_segment || item.Segment || item.user_segment}</strong></span>
                <span class="pill ${evClass}">${item.evidence_type || '🟡 AI-Synthesized Evidence'}</span>
            </div>
            <div class="comment-text">"${commentText}"</div>
            <div style="display: flex; justify-content: space-between; align-items: center; font-size: 11px; color: var(--text-muted); margin-top: 2px;">
                <span style="font-style: italic;">${item.thread_ref || 'Audit Reference #1001'} (${item.date || item.Date || 'Aug 2026'})</span>
                <a href="${srcUrl}" target="_blank" style="color: var(--primary); font-weight: 700; text-decoration: none;">View original ↗</a>
            </div>
            <div class="pain-point" style="margin-top: 6px;">📌 Primary Blocker: <strong>${painPoint}</strong></div>
            <div class="tag-pill-container">
                <span class="pill pill-cat">${item.primary_category || item.category_tag}</span>
                <span class="pill pill-intent">${item.intent_type || item.Intent + ' Intent'}</span>
                <span class="pill ${barrierClass}">${item.barrier_level || 'High'} Barrier</span>
                <span class="pill ${sentClass}">${item.sentiment || 'Negative'}</span>
                <span class="pill" style="background-color: var(--meta-bg); color: var(--text-muted);">AI Conf: ${confScore}</span>
                <span class="pill" style="background-color: rgba(16, 185, 129, 0.15); color: #10B981;">Human Val: ${item.Human_validation || 'Agree'}</span>
            </div>
        `;
        return card;
    }

    function updateFeedDisplay() {
        if (!feedContainer) return;
        feedContainer.innerHTML = "";
        
        if (resultsCountBadge) {
            resultsCountBadge.innerText = `Showing ${Math.min(currentRenderLimit, filteredItems.length)} of ${filteredItems.length} items`;
        }

        if (filteredItems.length === 0) {
            feedContainer.innerHTML = `
                <div style="text-align: center; color: var(--text-muted); padding: 40px; border: 1px dashed var(--border-color); border-radius: 12px;">
                    No feedback found matching current filters.
                </div>
            `;
            if (loadMoreBtn) loadMoreBtn.style.display = "none";
            return;
        }

        const itemsToRender = filteredItems.slice(0, currentRenderLimit);
        itemsToRender.forEach(item => {
            feedContainer.appendChild(renderFeedCard(item));
        });

        if (loadMoreBtn) {
            if (currentRenderLimit >= filteredItems.length) {
                loadMoreBtn.style.display = "none";
            } else {
                loadMoreBtn.style.display = "block";
                loadMoreBtn.innerText = `Load More Evidence Cards (+30 remaining: ${filteredItems.length - currentRenderLimit})`;
            }
        }
    }

    function applyFilters() {
        const searchVal = searchInput ? searchInput.value.toLowerCase().trim() : "";
        const catVal = catSelect ? catSelect.value : "All";
        const barrierVal = barrierSelect ? barrierSelect.value : "All";

        filteredItems = data.filter(item => {
            const segName = item.behavioral_segment || item.Segment || item.user_segment || "";
            const commentStr = item.comment || item.Raw_text || "";
            const painStr = item.primary_pain_point || item.Friction_tags || "";
            const srcStr = item.source || item.Source || "";

            const matchesSearch = !searchVal || 
                                  commentStr.toLowerCase().includes(searchVal) || 
                                  painStr.toLowerCase().includes(searchVal) ||
                                  segName.toLowerCase().includes(searchVal) ||
                                  srcStr.toLowerCase().includes(searchVal);

            const matchesCat = catVal === "All" || segName === catVal;
            const matchesBarrier = barrierVal === "All" || (item.barrier_level || 'High') === barrierVal;

            return matchesSearch && matchesCat && matchesBarrier;
        });

        currentRenderLimit = 30;
        updateFeedDisplay();
    }

    if (searchInput) searchInput.addEventListener("input", applyFilters);
    if (catSelect) catSelect.addEventListener("change", applyFilters);
    if (barrierSelect) barrierSelect.addEventListener("change", applyFilters);

    if (loadMoreBtn) {
        loadMoreBtn.addEventListener("click", () => {
            currentRenderLimit += 50;
            updateFeedDisplay();
        });
    }

    // Initial feed render
    updateFeedDisplay();

    // Chart.js Doughnut Chart setup
    const chartElem = document.getElementById('frictionDoughnut');
    if (chartElem) {
        const ctxFriction = chartElem.getContext('2d');
        new Chart(ctxFriction, {
            type: 'doughnut',
            data: {
                labels: Object.keys(catCounts),
                datasets: [{
                    data: Object.values(catCounts),
                    backgroundColor: [
                        '#D80E62', '#E11B74', '#9C27B0', '#673AB7', '#3F51B5', '#2196F3', '#10B981'
                    ],
                    borderColor: 'transparent',
                    borderWidth: 0
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: { display: false }
                }
            }
        });
    }

    // Theme toggle functionality
    const body = document.body;
    const themeToggle = document.getElementById("themeToggle");
    let currentTheme = localStorage.getItem("theme") || "dark";
    if (currentTheme === "light") {
        body.classList.add("light-theme");
        if (themeToggle) themeToggle.innerText = "🌙 Dark Mode";
    }

    if (themeToggle) {
        themeToggle.addEventListener("click", () => {
            if (body.classList.contains("light-theme")) {
                body.classList.remove("light-theme");
                themeToggle.innerText = "☀️ Light Mode";
                localStorage.setItem("theme", "dark");
            } else {
                body.classList.add("light-theme");
                themeToggle.innerText = "🌙 Dark Mode";
                localStorage.setItem("theme", "light");
            }
        });
    }

    // Full 14-Field CSV Download Functionality
    const csvBtn = document.getElementById("csvDownloadBtn");
    if (csvBtn) {
        csvBtn.addEventListener("click", (e) => {
            e.preventDefault();
            if (data.length === 0) return;

            const targetSchemaFields = [
                "Source", "Original_URL", "Date", "Raw_text", "Wishlist_reason", 
                "Intent", "Friction_tags", "Information_gap", "External_behaviour", 
                "Purchase_timeline", "Product_category", "Segment", "AI_confidence", "Human_validation"
            ];

            const csvRows = [];
            csvRows.push(targetSchemaFields.join(","));

            data.forEach(row => {
                const values = targetSchemaFields.map(field => {
                    const val = row[field] === null || row[field] === undefined ? "" : String(row[field]);
                    const escaped = val.replace(/"/g, '""');
                    return `"${escaped}"`;
                });
                csvRows.push(values.join(","));
            });

            const csvString = csvRows.join("\n");
            const blob = new Blob([csvString], { type: "text/csv;charset=utf-8;" });
            const url = URL.createObjectURL(blob);
            const link = document.createElement("a");
            link.setAttribute("href", url);
            link.setAttribute("download", "feedback_analysis_output.csv");
            document.body.appendChild(link);
            link.click();
            document.body.removeChild(link);
        });
    }
});

// Accordion toggle helper
function toggleAccordion(id, el) {
    const content = document.getElementById(id);
    if (!content) return;
    const arrow = el.querySelector(".accordion-arrow");
    
    if (content.classList.contains("active")) {
        content.classList.remove("active");
        if (arrow) arrow.classList.remove("rotated");
    } else {
        content.classList.add("active");
        if (arrow) arrow.classList.add("rotated");
    }
}
