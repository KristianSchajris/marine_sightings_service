import sqlite3

# connect to the database
conn = sqlite3.connect('marine_sightings.db')

# create a cursor
cursor = conn.cursor()

# create the places table
cursor.execute('''
CREATE TABLE IF NOT EXISTS places (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name_place VARCHAR(100) NOT NULL,
    country VARCHAR(100) NOT NULL,
    state VARCHAR(100) NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
)
''')

# create the species table
cursor.execute('''
CREATE TABLE IF NOT EXISTS species (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    common_name VARCHAR(100) NOT NULL UNIQUE,
    scientific_name VARCHAR(100) NOT NULL UNIQUE,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
)
''')

# create the taxonomic_categories table
cursor.execute('''
CREATE TABLE IF NOT EXISTS taxonomic_categories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    kingdom VARCHAR(150) NOT NULL,
    phylum VARCHAR(150) NOT NULL,
    t_class VARCHAR(150) NOT NULL,
    t_order VARCHAR(150) NOT NULL,
    family VARCHAR(150) NOT NULL,
    genus VARCHAR(150) NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    specie_id INTEGER NOT NULL,
    FOREIGN KEY (specie_id) REFERENCES species (id)
)
''')

# create the sightings table
cursor.execute('''
CREATE TABLE IF NOT EXISTS sightings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    latitude REAL NOT NULL,
    longitude REAL NOT NULL,
    image_sighting TEXT,  -- Se mantiene como TEXT para permitir URLs largas
    notes TEXT NOT NULL,   -- Se mantiene como TEXT para permitir notas extensas
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    place_id INTEGER NOT NULL,
    specie_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    FOREIGN KEY (place_id) REFERENCES places (id),
    FOREIGN KEY (specie_id) REFERENCES species (id)
    -- FOREIGN KEY (user_id) REFERENCES auth_user (id) -- Descomentar y ajustar según tu modelo de usuario
)
''')

# insert records into the places table
cursor.executemany('''
INSERT INTO places (name_place, country, state) VALUES (?, ?, ?)
''', [
    ('Playa del Carmen', 'México', 'Quintana Roo'),
    ('Cancún', 'México', 'Quintana Roo'),
    ('Galápagos', 'Ecuador', 'Galápagos'),
    ('Great Barrier Reef', 'Australia', 'Queensland'),
    ('Islas Malvinas', 'Reino Unido', 'Falkland Islands'),
    ('Bahía de Todos los Santos', 'Brasil', 'Bahía')
])

# insert records into the species table
cursor.executemany('''
INSERT INTO species (common_name, scientific_name) VALUES (?, ?)
''', [
    ('Tortuga verde', 'Chelonia mydas'),
    ('Delfín nariz de botella', 'Tursiops truncatus'),
    ('Tiburón blanco', 'Carcharodon carcharias'),
    ('Ballena jorobada', 'Megaptera novaeangliae'),
    ('Estrella de mar', 'Asteroidea'),
    ('Pez payaso', 'Amphiprioninae')
])

# insert records into the taxonomic_categories table
cursor.executemany('''
INSERT INTO taxonomic_categories (kingdom, phylum, t_class, t_order, family, genus, specie_id) VALUES (?, ?, ?, ?, ?, ?, ?)
''', [
    ('Animalia', 'Chordata', 'Reptilia', 'Testudines', 'Cheloniidae', 'Chelonia', 1),
    ('Animalia', 'Chordata', 'Mammalia', 'Cetacea', 'Delphinidae', 'Tursiops', 2),
    ('Animalia', 'Chordata', 'Chondrichthyes', 'Lamniformes', 'Lamnidae', 'Carcharodon', 3),
    ('Animalia', 'Chordata', 'Mammalia', 'Balaenopteridae', 'Balaenoptera', 'Megaptera', 4),
    ('Animalia', 'Echinodermata', 'Asteroidea', 'Valvatida', 'Asteridae', 'Astropecten', 5),
    ('Animalia', 'Chordata', 'Actinopterygii', 'Perciformes', 'Pomacentridae', 'Amphiprion', 6)
])

# insert records into the sightings table
cursor.executemany('''
INSERT INTO sightings (latitude, longitude, image_sighting, notes, place_id, specie_id, user_id) VALUES (?, ?, ?, ?, ?, ?, ?)
''', [
    (20.6296, -87.0739, 'url_imagen_1.jpg', 'Observación de tortugas en Playa del Carmen', 1, 1, 1),
    (21.1619, -86.8515, 'url_imagen_2.jpg', 'Delfines avistados en Cancún', 2, 2, 1),
    (-0.5930, -90.9566, 'url_imagen_3.jpg', 'Tiburones en Galápagos', 3, 3, 1),
    (-10.5732, 142.9460, 'url_imagen_4.jpg', 'Ballenas en la Gran Barrera de Coral', 4, 4, 1),
    (-51.6963, -57.8500, 'url_imagen_5.jpg', 'Estrellas de mar en las Islas Malvinas', 5, 5, 1),
    (-12.8833, -38.3333, 'url_imagen_6.jpg', 'Pez payaso en la Bahía de Todos los Santos', 6, 6, 1)
])

# commit the changes and close the connection
conn.commit()
conn.close()