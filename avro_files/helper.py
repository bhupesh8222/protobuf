from avro.schema import parse
import json


def infer_avro_type(value, parent_name=None, field_name=None):
    """Recursively infer Avro data types from a Python value and assign record names dynamically."""
    if value is None:
        return "null"
    elif isinstance(value, bool):
        return "boolean"
    elif isinstance(value, int):
        return "int"
    elif isinstance(value, float):
        return "float"
    elif isinstance(value, str):
        return "string"
    elif isinstance(value, dict):
        # For dictionaries, we assume they represent Avro records
        if field_name:
            # Dynamically generate the record name as 'ParentName_FieldName'
            record_name = field_name
        else:
            record_name = "NestedRecord"
        return {
            "type": "record",
            "name": record_name,
            "fields": infer_avro_fields(value, parent_name, field_name)
        }
    elif isinstance(value, list):
        # For lists, infer the type of the first item (assuming homogeneous lists)
        if value:
            return [infer_avro_type(value[0], parent_name, field_name)]
        else:
            return ["null"]  # Empty lists are treated as nullable
    else:
        return "string"  # Default to string for unknown types


def infer_avro_fields(json_obj, parent_name=None, field_name=None):
    """Recursively infer Avro fields from a JSON object and assign record names dynamically."""
    fields = []
    for key, value in json_obj.items():
        field = {
            "name": key,
            "type": infer_avro_type(value, parent_name, key)
        }
        fields.append(field)
    return fields


def generate_avro_schema(json_data, record_name="GeneratedRecord"):
    """Generate Avro schema from JSON data."""
    if isinstance(json_data, dict):
        schema_json = {
            "type": "record",
            "name": record_name,
            "fields": infer_avro_fields(json_data, record_name, None)
        }

        return parse(json.dumps(schema_json))
    else:
        raise ValueError("Input JSON must be a dictionary at the root.")


