#  Copyright (c) 2022 spdx contributors
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#    http://www.apache.org/licenses/LICENSE-2.0
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
from typing import TextIO

from spdx_tools.spdx.model.relationship import Relationship
from spdx_tools.spdx.writer.tagvalue.tagvalue_writer_helper_functions import write_text_value, write_value


def write_relationship(relationship: Relationship, text_output: TextIO):
    write_value(
        "Relationship",
        " ".join(
            [
                relationship.spdx_element_id,
                relationship.relationship_type.name,
                str(relationship.related_spdx_element_id),
            ]
        ),
        text_output,
    )
    write_text_value("RelationshipComment", relationship.comment, text_output)