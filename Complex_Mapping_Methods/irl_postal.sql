SELECT 
    value:unparsed_name::STRING AS territory_name
FROM 
    MAPS_DATA_ANALYTICS_CORE_DB.BASEMAP_FEATURES_CORE.irl_kh_sr_csr1_ndm_data,
    LATERAL FLATTEN(input => FEATURE_PROTO:territory:name) AS name
WHERE 
    FEATURE_TYPE = 'TERRITORY' 
    AND FEATURE_PROTO:territory:territory_type::STRING = 'POSTAL_DISTRICT'
    AND name.value:language::ARRAY[0]::STRING = 'en';