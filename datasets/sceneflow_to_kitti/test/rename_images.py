import os, glob


if __name__ == "__main__":
  for folder in ["2012", "2015"]:
    files = glob.glob("./B/{}/*.png".format(folder))
    for f in files:
      os.rename(f, "./B/{}_{}".format(folder, os.path.basename(f)))
