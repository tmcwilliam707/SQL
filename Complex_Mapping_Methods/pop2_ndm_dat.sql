SELECT 
    FEATURE_PROTO:iso_country_code::string as country, 
    FEATURE_PROTO:territory:territory_type::string as territory_type,
    FEATURE_PROTO:territory:population[0].population::string AS population
FROM
    KH_TERRITORY_NDM_DATA
WHERE 
    FEATURE_PROTO:territory:territory_type::string = 'COUNTRY' 