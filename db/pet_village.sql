DROP TABLE IF EXISTS treatments;
DROP TABLE IF EXISTS pets;

DROP TABLE IF EXISTS vets;
DROP TABLE IF EXISTS owners;

CREATE TABLE owners (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR (100),
    last_name VARCHAR (100),
    email VARCHAR (200),
    mobile VARCHAR (150)
);

CREATE TABLE vets (
    id SERIAL PRIMARY KEY,
    vet_name VARCHAR (100)
);

CREATE TABLE pets (
    id SERIAL PRIMARY KEY,
    pet_name VARCHAR (100),
    dob VARCHAR (20),
    pet_type VARCHAR (100),
    owner_id SERIAL REFERENCES owners (id),
    vet_id SERIAL REFERENCES vets (id)
);

CREATE TABLE treatments (
    id SERIAL PRIMARY KEY,
    treatment_date VARCHAR (20),
    procedure_type VARCHAR (200),
    pet_id SERIAL REFERENCES pets (id),
    vet_id SERIAL REFERENCES vets (id)
);
