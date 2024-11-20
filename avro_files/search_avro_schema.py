avro_schema = {
  "type": "array",
  "items": {
    "type": "record",
    "name": "SearchResultItem",
    "namespace": "com.product",
    "fields": [
      {"name": "id", "type": "string"},
      {"name": "name", "type": "string"},
      {"name": "type", "type": "string"},
      {"name": "available", "type": "boolean"},
      {"name": "url", "type": "string"},
      {
        "name": "ratings",
        "type": {
          "type": "record",
          "name": "Ratings",
          "fields": [
            {"name": "total_ratings", "type": "int"},
            {"name": "average_rating", "type": "double"}
          ]
        }
      },
      {"name": "label", "type": "string"},
      {"name": "image", "type": "string"},
      {
        "name": "prices",
        "type": {
          "type": "record",
          "name": "Prices",
          "fields": [
            {"name": "mrp", "type": "string"},
            {"name": "discounted_price", "type": "string"},
            {"name": "discount", "type": "string"}
          ]
        }
      },
      {
        "name": "cta",
        "type": {
          "type": "record",
          "name": "CTA",
          "fields": [
            {"name": "text", "type": "string"},
            {"name": "action", "type": "string"},
            {
              "name": "details",
              "type": {
                "type": "record",
                "name": "CTADetails",
                "fields": [
                  {"name": "sku_id", "type": "string"},
                  {"name": "quantity", "type": "int"}
                ]
              }
            }
          ]
        }
      },
      {
        "name": "quantity_info",
        "type": {
          "type": "record",
          "name": "QuantityInfo",
          "fields": [
            {"name": "min", "type": "int"},
            {"name": "max", "type": "int"},
            {"name": "selling_quantity", "type": "int"},
            {"name": "display_text", "type": ["null", "string"]},
            {"name": "know_more", "type": ["null", "string"]}
          ]
        }
      },
      {"name": "eta", "type": "string"},
      {
        "name": "ga_data",
        "type": {
          "type": "record",
          "name": "GAData",
          "fields": [
            {
              "name": "info",
              "type": {
                "type": "record",
                "name": "GAInfo",
                "fields": [
                  {"name": "text", "type": "string"},
                  {"name": "eta", "type": "long"}
                ]
              }
            }
          ]
        }
      },
      {"name": "eta_info", "type": ["null", "string"]},
      {"name": "combo_upsell", "type": ["null", "string"]},
      {"name": "combo_experiment_eligible", "type": "boolean"},
      {
        "name": "cropped_image_urls",
        "type": {
          "type": "array",
          "items": "string"
        }
      },
      {"name": "rx_required", "type": "boolean"},
      {
        "name": "mix_panel_data",
        "type": {
          "type": "record",
          "name": "MixPanelData",
          "fields": [
            {"name": "mrp", "type": "int"},
            {"name": "discount_percent", "type": "int"},
            {"name": "position", "type": "int"},
            {"name": "eta", "type": "long"},
            {"name": "eta_text", "type": "string"},
            {"name": "sku_availability_status", "type": "string"},
            {"name": "epoch_eta", "type": "long"},
            {"name": "pincode", "type": "int"},
            {"name": "sku_sponsored", "type": "boolean"},
            {"name": "uclid", "type": ["null", "string"]}
          ]
        }
      },
      {"name": "is_infant", "type": "boolean"}
    ]
  }
}