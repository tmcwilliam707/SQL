CREATE OR REPLACE TRANSIENT TABLE $TARGET_TABLE_DATA AS
WITH geo AS (
    SELECT
        feature_id,
        wkb as geom,
        boundary_type AS boundary_type
    FROM $SOURCE_GEOM_DATA
)
SELECT
    f.feature_id AS feature_id,
    feature_proto:iso_country_code::STRING AS iso_country_code,
    feature_proto:iso_subdivision_code::STRING AS iso_subdivision_code,
    feature_type::STRING AS feature_type,
    feature_proto:is_active::BOOLEAN AS is_active,
    feature_proto:address_point.address_point_type AS address_point_type,
    boundary_type AS  address_boundary_type,
    feature_proto:address_point.address[0].address_type[0]:: STRING AS address_type,
    feature_proto:address_point.address[0].address_component[2].name[0].unparsed_name as house_number,
    feature_proto:address_point.address[0].address_component[2].address_component_type as post_code_reference,
    feature_proto:address_point:address[0]:address_component[2]:name[0]:unparsed_name as post_code,
    feature_version AS version,
    feature_proto:representative_point:latitude as rep_lat,
    feature_proto:representative_point:longitude as rep_lng,
    geom AS geom
FROM $SOURCE_TABLE_DATA f
JOIN geo g
    ON f.feature_id = g.feature_id,
WHERE feature_type = 'ADDRESS_POINT'
ORDER BY f.feature_id;