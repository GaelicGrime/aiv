

with open("package.json", "tr") as _FDIn_:
  _result_ = ujson.load(_FDIn_)
_splitVersion_ = f"""{_result_["version"]}""".split(".")


# -j major, -n minor -p patch -z nop, reads and rewrites only
if (
    (len(sys.argv) == 2) and
    (sys.argv[1] == "-j")
):
  _splitVersion_[0] = int(_splitVersion_[0]) + 1
elif (
    (len(sys.argv) == 2) and
    (sys.argv[1] == "-n")
):
  _splitVersion_[1] = int(_splitVersion_[1]) + 1
elif (
    (len(sys.argv) == 2) and
    (sys.argv[1] == "-p")
):
  _splitVersion_[2] = int(_splitVersion_[2]) + 1
elif (
    (len(sys.argv) == 2) and
    (sys.argv[1] == "-z")
):
  pass
else:
  echo
  sys.exit(1)


_tagVersion_ = f"""{_splitVersion_[0]}.{_splitVersion_[1]}.{_splitVersion_[2]}"""
_result_["version"] = _tagVersion_
with open("package.json", "tw") as _FDOut_:
  ujson.dump(_result_, _FDOut_, indent=2, escape_forward_slashes=False)
  _FDOut_.flush()
  _FDOut_.close()

_command_ = ["gitTag", f"""'v{_tagVersion_}'"""]
subprocess.run(_command_)
