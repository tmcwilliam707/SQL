SELECT 
    feature_id, 
    unparsed_name, 
    territory_type, 
    COUNT(DISTINCT language) as language_count, 
    ARRAY_TO_STRING(ARRAY_AGG(DISTINCT language), ', ') as languages
FROM (
    SELECT 
        FEATURE_PROTO:feature_id::string as feature_id, 
        name.value:unparsed_name::string as unparsed_name, 
        name.value:language::string as language, 
        FEATURE_PROTO:territory:territory_type::string as territory_type
    FROM MAPS_DATA_SEMANTIC_DB.CPMA_APP.WEEKLY_ARCHES_SUNDANCE_PRODUCTION_NDM_DATA,
    LATERAL FLATTEN(input => FEATURE_PROTO:territory:name) as name
    WHERE feature_type = 'TERRITORY'
    AND FEATURE_PROTO:iso_country_code::string = 'NZL'
    AND name.value:name_type::string = 'PRIMARY_FOR_LANGUAGE'
) subquery
GROUP BY feature_id, unparsed_name, territory_type
HAVING COUNT(DISTINCT language) > 1;