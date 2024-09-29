f = input("File name: ").split('.')
extension = f[-1].lower().strip()

match extension:
    case "jpeg" | "jpg":
        print("image/jpeg", end='')
    case "gif":
        print("image/gif", end='')
    case "png":
        print("image/png", end='')
    case "pdf":
        print("application/pdf", end='')
    case "zip":
        print("application/zip", end='')
    case "txt":
        print("text/plain", end='')
    case _:
        print("application/octet-stream", end='')
