CREATE OR REPLACE TRANSIENT TABLE $TARGET_TABLE_DATA AS
WITH boundary_agg AS (
    SELECT
        feature_id,
        boundary_type as boundary_type,
        geometry
    FROM $SOURCE_GEOM_DATA g
)
SELECT
    f.feature_id AS feature_id,
    feature_proto:iso_country_code::STRING AS iso_country_code,
    feature_proto:iso_subdivision_code::STRING AS iso_subdivision_code,
    feature_proto:country_code::STRING AS country_code,
    feature_proto:country_subdivision_code::STRING AS country_subdivision_code,
    feature_type::STRING AS feature_type,
    feature_proto:island.type AS island_type,
    feature_proto:is_active::BOOLEAN AS is_active,
    feature_proto:display_class::NUMBER AS display_class,
    feature_proto:vendor_info.vendor_id::NUMBER AS vendor_id,
    feature_proto:vendor_info.vendor_feature_id::STRING AS vendor_feature_id,
    feature_proto:vendor_info.vendor_version::NUMBER AS vendor_version,
    feature_proto:island.name[0].unparsed_name AS unparsed_name,
    feature_proto:island.name[0].language AS language,
    feature_proto:island.name AS names_arr,
    b.boundary_type AS boundary_type,
    feature_version AS version,
    b.geometry as geom
FROM $SOURCE_TABLE_DATA f
JOIN boundary_agg b
    ON f.feature_id = b.feature_id,
WHERE feature_type = 'ISLAND';