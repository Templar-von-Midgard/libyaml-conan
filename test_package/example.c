#include <stdio.h>

#include "yaml.h"

const unsigned char yaml_content[] =
"yaml:\n"
"  [can be]:\n"
"  - successfully parsed\n"
;

int main() {
  yaml_parser_t parser;
  yaml_parser_initialize(&parser);
  yaml_parser_set_input_string(&parser, yaml_content, sizeof(yaml_content) - 1);
  int done = 0;
  while(!done) {
    yaml_event_t event;
    if (!yaml_parser_parse(&parser, &event)) {
      printf("%s\n", parser.problem);
      yaml_parser_delete(&parser);
      return 1;
    }
    done = event.type == YAML_STREAM_END_EVENT;
    yaml_event_delete(&event);
  }
  yaml_parser_delete(&parser);
  return 0;
}
