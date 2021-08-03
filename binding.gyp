{
  "targets": [
    {
      "target_name": "nroonga_bindings",
      "sources": [ "src/nroonga.cc" ],
      "include_dirs": [
        "<!(node -e \"require('nan')\")",
        "<!(echo $GROONGA_BUILD_PATH)/include",
        "<!(echo $GROONGA_INCLUDE_PATH)",
      ],
      "libraries": [
        "<!(echo $GROONGA_BUILD_PATH)/lib/libgroonga.a",
        "<!(echo $GROONGA_BUILD_PATH)/vendor/onigmo/libonigmo.a",
        "<!(echo $GROONGA_BUILD_PATH)/plugins/tokenizers/libmecab_tokenizer.a"
      ],
    }
  ]
}
