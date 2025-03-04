import platform
bitx = platform.architecture()[0]
if bitx == '64bit':
    import creatego
elif bitx == '32bit':
    print("[=] 32BIT NOT SUPPORTED SORRY")
