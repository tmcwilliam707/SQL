WITH ndm_feature_ids AS (
    SELECT DISTINCT
        FEATURE_PROTO:feature_id::string AS feature_id
    FROM 
        MAPS_DATA_ANALYTICS_CORE_DB.BASEMAP_FEATURES_CORE.irl_kh_sr_csr1_ndm_data
    WHERE 
        FEATURE_TYPE = 'TERRITORY'
        AND FEATURE_PROTO:territory:territory_type::STRING = 'POSTAL_SUB_DISTRICT'
)
SELECT *
FROM 
    MAPS_DATA_ANALYTICS_CORE_DB.BASEMAP_FEATURES_CORE.irl_kh_sr_csr1_geometry_data
WHERE 
    FEATURE_PROTO:feature_id::string IN (SELECT feature_id FROM ndm_feature_ids);