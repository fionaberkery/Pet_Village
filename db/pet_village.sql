DROP TABLE IF EXISTS bookings;
DROP TABLE IF EXISTS treatments;
DROP TABLE IF EXISTS pets;
DROP TABLE IF EXISTS nurses;
DROP TABLE IF EXISTS vets;
DROP TABLE IF EXISTS owners;
DROP TABLE IF EXISTS prices;

CREATE TABLE owners (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR (100),
    last_name VARCHAR (100),
    email VARCHAR (200),
    mobile VARCHAR (150)
);

CREATE TABLE vets (
    id SERIAL PRIMARY KEY,
    vet_name VARCHAR (100),
    speciality VARCHAR (150),
    email VARCHAR (150)
);

CREATE TABLE nurses (
    id SERIAL PRIMARY KEY,
    nurse_name VARCHAR (200),
    days_works VARCHAR (255),
    available_weekends BOOLEAN,
    email VARCHAR (250)
);

CREATE TABLE prices (
    id SERIAL PRIMARY KEY,
    treatment_type VARCHAR (255),
    price VARCHAR (200),
    time_req VARCHAR (255),
    vet_req BOOLEAN,
    nurses_req INT
);

CREATE TABLE pets (
    id SERIAL PRIMARY KEY,
    pet_name VARCHAR (100),
    dob DATE,
    pet_type VARCHAR (100),
    owner_id INT REFERENCES owners (id) ON DELETE CASCADE,
    vet_id INT REFERENCES vets (id)
);



CREATE TABLE treatments (
    id SERIAL PRIMARY KEY,
    treatment_date VARCHAR (100),
    procedure_type VARCHAR (200),
    pet_id INT REFERENCES pets (id) ON DELETE CASCADE,
    vet_id INT REFERENCES vets (id)
);

CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    date DATE,
    time VARCHAR (200),
    pet_id INT REFERENCES pets (id),
    price_id INT REFERENCES prices (id),
    vet_id INT REFERENCES vets (id)
);