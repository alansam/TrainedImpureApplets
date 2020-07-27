def main():
  print("In main()")
  a = [i for i in range(51) if i % 2 == 0]
  for e in a:
    print("%3d %03o %#04x" % (e, e, e))

if __name__ == "__main__":
  print("Running %s" % (__name__))
  main()
