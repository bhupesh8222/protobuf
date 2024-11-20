import io

import avro.io
import avro.schema
import rec_avro
from rec_avro import to_rec_avro_destructive
from sanic import Sanic
from sanic.response import json, raw
from google.protobuf.json_format import ParseDict
import json as json_lib

from avro_files.helper import generate_avro_schema
from avro_files.search_avro_schema import avro_schema
from protobuff.generated import search_response_pb2
from protobuff.scripts.generate_proto import create_proto_files
from protobuff.search_response import search_results

app = Sanic("protobuf_poc")


@app.route("/search/json")
async def get_search_json(request):
    json_data = json_lib.dumps(search_results)
    response_size = len(json_data)

    headers = {
        "X-Response-Size": f"{response_size} bytes"
    }

    return json(search_results, headers=headers)


@app.route("/search/protobuf")
async def get_search_protobuf(request):
    protobuf_search_response = ParseDict(search_results, search_response_pb2.SearchResponse())
    protobuf_data = protobuf_search_response.SerializeToString()
    response_size = len(protobuf_data)

    headers = {
        "X-Response-Size": f"{response_size} bytes",
        "Content-Type": "application/x-protobuf"
    }

    return raw(protobuf_data, headers=headers)


@app.route("/search/avro")
async def get_search_avro(request):
    # Serialize data to Avro format
    bytes_writer = io.BytesIO()
    encoder = avro.io.BinaryEncoder(bytes_writer)
    # Initializes DatumWriter, which writes individual records based on schema.
    schema = avro.schema.parse(json_lib.dumps(avro_schema))
    datum_writer = avro.io.DatumWriter(schema)
    datum_writer.write(search_results, encoder)

    # Get serialized Avro bytes
    avro_data = bytes_writer.getvalue()
    response_size = len(avro_data)

    # Return raw response with headers
    headers = {
        "X-Response-Size": f"{response_size} bytes",
        "Content-Type": "application/avro"
    }
    return raw(avro_data, headers=headers)


def main():
    app.run(host="0.0.0.0", port=8000, debug=True)


if __name__ == "__main__":
    create_proto_files()
    main()
