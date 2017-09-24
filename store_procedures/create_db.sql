CREATE TABLE nyc_air_data(

    key int PRIMARY KEY,
    indicator_data_id int,
    indicator_id int,
    name text,
    Measure text,
    geo_type_name text,
    geo_entity_id int,
    geo_entity_name text,
    year_description text,
    data_valuemessage text
);

COPY nyc_air_data FROM 'Air_Quality.csv' delimiter ',' csv;