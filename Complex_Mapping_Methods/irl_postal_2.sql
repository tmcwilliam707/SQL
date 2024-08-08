SELECT DISTINCT
    FEATURE_PROTO:feature_id::string as feature_id,
    name.value:unparsed_name::string as unparsed_name,
    FEATURE_PROTO:territory:territory_type::string as territory_type
FROM 
    MAPS_DATA_ANALYTICS_CORE_DB.BASEMAP_FEATURES_CORE.irl_kh_sr_csr1_ndm_data,
    LATERAL FLATTEN(input => FEATURE_PROTO:territory:name) AS territory_name
WHERE 
    FEATURE_TYPE = 'TERRITORY'
    AND FEATURE_PROTO:territory:territory_type::STRING = 'POSTAL_SUB_DISTRICT'
LIMIT 2;

SELECT DISTINCT
    FEATURE_PROTO:feature_id::string as feature_id,
    territory_name.value:unparsed_name::string as unparsed_name,
    FEATURE_PROTO:territory:territory_type::string as territory_type
FROM 
    MAPS_DATA_ANALYTICS_CORE_DB.BASEMAP_FEATURES_CORE.irl_kh_sr_csr1_ndm_data,
    LATERAL FLATTEN(input => FEATURE_PROTO:territory:name) AS territory_name
WHERE 
    FEATURE_TYPE = 'TERRITORY'
    AND FEATURE_PROTO:territory:territory_type::STRING = 'POSTAL_SUB_DISTRICT'
LIMIT 2;