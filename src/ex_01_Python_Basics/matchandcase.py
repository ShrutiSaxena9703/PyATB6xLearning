browser=input("enter your browser")
match browser:
    case "chrome":
      print("your browser is chrome")
    case "firefox":
      print("your browser is firefox")
    case _ :
      print("no browser found")