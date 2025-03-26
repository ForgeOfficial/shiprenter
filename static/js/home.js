const ships = [
    {
        id: 1,
        name: "C2 Hercules",
        category: "Transport",
        size: "Large",
        crew: 2,
        price: 400,
        description: "Vaisseau de transport militaire lourd",
        image: "https://static.wikia.nocookie.net/cheaseeating-citizens/images/0/0f/O2FYDAk.jpg/revision/latest/scale-to-width-down/1200?cb=20151022153346&path-prefix=fr"
    },
    {
        id: 2,
        name: "Avenger Titan",
        category: "Combat",
        size: "Petit",
        crew: 1,
        price: 150,
        description: "Chasseur polyvalent avec espace de stockage",
        image: "https://static.wikia.nocookie.net/cheaseeating-citizens/images/0/0f/O2FYDAk.jpg/revision/latest/scale-to-width-down/1200?cb=20151022153346&path-prefix=fr"
    },
    {
        id: 3,
        name: "Freelancer MAX",
        category: "Transport",
        size: "Moyen",
        crew: 2,
        price: 300,
        description: "Transport de marchandises pour trajets moyens",
        image: "https://static.wikia.nocookie.net/cheaseeating-citizens/images/0/0f/O2FYDAk.jpg/revision/latest/scale-to-width-down/1200?cb=20151022153346&path-prefix=fr"
    },
    {
        id: 4,
        name: "600i Explorer",
        category: "Exploration",
        size: "Large",
        crew: 3,
        price: 650,
        description: "Vaisseau d'exploration de luxe",
        image: "https://static.wikia.nocookie.net/cheaseeating-citizens/images/0/0f/O2FYDAk.jpg/revision/latest/scale-to-width-down/1200?cb=20151022153346&path-prefix=fr"
    },
    {
        id: 5,
        name: "Aurora MR",
        category: "Transport",
        size: "Petit",
        crew: 1,
        price: 100,
        description: "Vaisseau de démarrage idéal pour débutants",
        image: "https://static.wikia.nocookie.net/cheaseeating-citizens/images/0/0f/O2FYDAk.jpg/revision/latest/scale-to-width-down/1200?cb=20151022153346&path-prefix=fr"
    },
    {
        id: 6,
        name: "Hammerhead",
        category: "Combat",
        size: "Large",
        crew: 3,
        price: 800,
        description: "Corvette de combat lourdement armée",
        image: "https://static.wikia.nocookie.net/cheaseeating-citizens/images/0/0f/O2FYDAk.jpg/revision/latest/scale-to-width-down/1200?cb=20151022153346&path-prefix=fr"
    },
    {
        id: 7,
        name: "Mercury Star Runner",
        category: "Transport",
        size: "Moyen",
        crew: 2,
        price: 450,
        description: "Vaisseau rapide pour transport de données",
        image: "https://static.wikia.nocookie.net/cheaseeating-citizens/images/0/0f/O2FYDAk.jpg/revision/latest/scale-to-width-down/1200?cb=20151022153346&path-prefix=fr"
    },
    {
        id: 8,
        name: "Constellation Aquila",
        category: "Exploration",
        size: "Large",
        crew: 2,
        price: 500,
        description: "Vaisseau d'exploration avec véhicule terrestre",
        image: "https://static.wikia.nocookie.net/cheaseeating-citizens/images/0/0f/O2FYDAk.jpg/revision/latest/scale-to-width-down/1200?cb=20151022153346&path-prefix=fr"
    },
    {
        id: 9,
        name: "Prospector",
        category: "Exploration",
        size: "Petit",
        crew: 1,
        price: 250,
        description: "Vaisseau spécialisé dans l'extraction minière",
        image: "https://static.wikia.nocookie.net/cheaseeating-citizens/images/0/0f/O2FYDAk.jpg/revision/latest/scale-to-width-down/1200?cb=20151022153346&path-prefix=fr"
    },
    {
        id: 10,
        name: "Carrack",
        category: "Exploration",
        size: "Large",
        crew: 3,
        price: 950,
        description: "Vaisseau d'exploration de longue durée",
        image: "https://static.wikia.nocookie.net/cheaseeating-citizens/images/0/0f/O2FYDAk.jpg/revision/latest/scale-to-width-down/1200?cb=20151022153346&path-prefix=fr"
    }
];

let state = {
    ships: [...ships],
    filteredShips: [...ships],
    currentPage: 1,
    itemsPerPage: 6,
    sortBy: 'price-asc',
    filters: {
        model: '',
        size: '',
        category: '',
        crew: ''
    }
};

const shipsContainer = document.getElementById('ships-container');
const paginationContainer = document.getElementById('pagination');
const resultsCount = document.getElementById('results-count');
const modelSearchInput = document.getElementById('model-search');
const sizeFilterSelect = document.getElementById('size-filter');
const categoryFilterSelect = document.getElementById('category-filter');
const crewFilterSelect = document.getElementById('crew-filter');
const sortSelect = document.getElementById('sort-select');
const searchBtn = document.getElementById('search-btn');

function createShipCard(ship) {
    return `
        <div class="ship-card bg-white rounded-xl overflow-hidden shadow-md">
            <div class="relative aspect-w-16 aspect-h-9">
                <img src="${ship.image}" alt="${ship.name}" class="w-full h-48 object-cover">
                <div class="absolute top-3 left-3">
                    <span class="bg-slate-900/80 text-white text-xs px-2 py-1 rounded">${ship.category}</span>
                </div>
            </div>
            <div class="p-4">
                <h4 class="text-lg font-bold text-slate-800 mb-2">${ship.name}</h4>
                <p class="text-sm text-slate-600 mb-3">${ship.description}</p>
                <div class="flex flex-wrap gap-2 mb-3">
                    <span class="bg-slate-100 text-slate-700 text-xs px-2 py-1 rounded-full flex items-center">
                        <svg xmlns="http://www.w3.org/2000/svg" class="mr-1 text-slate-500 h-3 w-3" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <path d="M20 20v-5h-5"></path>
                            <path d="M4 4v5h5"></path>
                            <path d="M4 9l6 6"></path>
                            <path d="M14 14l6-6"></path>
                        </svg>
                        Taille: ${ship.size}
                    </span>
                    <span class="bg-slate-100 text-slate-700 text-xs px-2 py-1 rounded-full flex items-center">
                        <svg xmlns="http://www.w3.org/2000/svg" class="mr-1 text-slate-500 h-3 w-3" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <circle cx="12" cy="7" r="4"></circle>
                            <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path>
                        </svg>
                        Équipage max: ${ship.crew}
                    </span>
                </div>
                <div class="flex justify-between items-center pt-2 border-t border-slate-100">
                    <div class="text-xl font-bold text-blue-600">${ship.price}€ <span class="text-sm font-normal text-slate-500">/ jour</span></div>
                    <button class="bg-blue-50 hover:bg-blue-100 text-blue-600 px-3 py-1 rounded-lg transition-colors text-sm font-medium">
                        Réserver
                    </button>
                </div>
            </div>
        </div>
    `;
}

function createPaginationControls(totalPages) {
    let controls = `
        <a href="#" class="pagination-prev px-3 py-2 rounded-md bg-white border border-slate-300 text-slate-500 hover:bg-slate-50 ${state.currentPage === 1 ? 'opacity-50 pointer-events-none' : ''}">
            <span class="sr-only">Précédent</span>
            <i class="fas fa-chevron-left text-sm"></i>
        </a>
    `;
    
    for (let i = 1; i <= totalPages; i++) {
        controls += `
            <a href="#" class="pagination-page px-3 py-2 rounded-md ${i === state.currentPage ? 'bg-blue-600 text-white font-medium' : 'bg-white border border-slate-300 text-slate-700 hover:bg-slate-50'}" data-page="${i}">${i}</a>
        `;
    }
    
    controls += `
        <a href="#" class="pagination-next px-3 py-2 rounded-md bg-white border border-slate-300 text-slate-500 hover:bg-slate-50 ${state.currentPage === totalPages ? 'opacity-50 pointer-events-none' : ''}">
            <span class="sr-only">Suivant</span>
            <i class="fas fa-chevron-right text-sm"></i>
        </a>
    `;
    
    return controls;
}

function filterShips() {
    state.filteredShips = ships.filter(ship => {
        if (state.filters.model && !ship.name.toLowerCase().includes(state.filters.model.toLowerCase())) {
            return false;
        }
        
        if (state.filters.size && ship.size !== state.filters.size) {
            return false;
        }
        
        if (state.filters.category && ship.category !== state.filters.category) {
            return false;
        }
        
        if (state.filters.crew) {
            const crewValue = parseInt(state.filters.crew);
            if (crewValue === 3) {
                if (ship.crew < 3) return false;
            } else {
                if (ship.crew !== crewValue) return false;
            }
        }
        
        return true;
    });
    
    sortShips();
    
    state.currentPage = 1;
    
    updateUI();
}

function sortShips() {
    switch (state.sortBy) {
        case 'price-asc':
            state.filteredShips.sort((a, b) => a.price - b.price);
            break;
        case 'price-desc':
            state.filteredShips.sort((a, b) => b.price - a.price);
            break;
        case 'name-asc':
            state.filteredShips.sort((a, b) => a.name.localeCompare(b.name));
            break;
        case 'name-desc':
            state.filteredShips.sort((a, b) => b.name.localeCompare(a.name));
            break;
    }
}

function renderShips() {
    const startIndex = (state.currentPage - 1) * state.itemsPerPage;
    const endIndex = startIndex + state.itemsPerPage;
    const shipsToDisplay = state.filteredShips.slice(startIndex, endIndex);
    
    shipsContainer.innerHTML = '';
    
    if (shipsToDisplay.length === 0) {
        shipsContainer.innerHTML = `
            <div class="col-span-full text-center py-10">
                <div class="text-5xl mb-4">🔍</div>
                <h3 class="text-xl font-medium text-slate-800 mb-2">No ships found</h3>
                <p class="text-slate-600">Try adjusting your search filters</p>
            </div>
        `;
        return;
    }
    
    shipsToDisplay.forEach(ship => {
        shipsContainer.innerHTML += createShipCard(ship);
    });
}

function renderPagination() {
    const totalPages = Math.ceil(state.filteredShips.length / state.itemsPerPage);
    
    if (totalPages <= 1) {
        paginationContainer.innerHTML = '';
        return;
    }
    
    paginationContainer.innerHTML = createPaginationControls(totalPages);
    
    document.querySelectorAll('.pagination-page').forEach(button => {
        button.addEventListener('click', (e) => {
            e.preventDefault();
            state.currentPage = parseInt(button.dataset.page);
            updateUI();
        });
    });
    
    document.querySelector('.pagination-prev').addEventListener('click', (e) => {
        e.preventDefault();
        if (state.currentPage > 1) {
            state.currentPage--;
            updateUI();
        }
    });
    
    document.querySelector('.pagination-next').addEventListener('click', (e) => {
        e.preventDefault();
        const totalPages = Math.ceil(state.filteredShips.length / state.itemsPerPage);
        if (state.currentPage < totalPages) {
            state.currentPage++;
            updateUI();
        }
    });
}

function updateUI() {
    renderShips();
    renderPagination();
    resultsCount.textContent = state.filteredShips.length;
}

function initEventListeners() {
    searchBtn.addEventListener('click', () => {
        state.filters.model = modelSearchInput.value;
        state.filters.size = sizeFilterSelect.value;
        state.filters.category = categoryFilterSelect.value;
        state.filters.crew = crewFilterSelect.value;
        filterShips();
    });
    
    sortSelect.addEventListener('change', () => {
        state.sortBy = sortSelect.value;
        sortShips();
        updateUI();
    });
    
    modelSearchInput.addEventListener('keyup', (e) => {
        if (e.key === 'Enter') {
            searchBtn.click();
        }
    });
}

function init() {
    sortShips();
    updateUI();
    initEventListeners();
}

init();