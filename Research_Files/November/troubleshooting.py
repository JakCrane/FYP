import ctypes


# try:
#     # Load libxsmm.so automatically from LD_LIBRARY_PATH
#     libxsmm = ctypes.CDLL("libxsmm.so")
#     print("libxsmm.so loaded successfully!")
# except OSError as e:
#     print(f"Failed to load libxsmm.so: {e}")




# Path to libxsmm.so
libxsmm_path = "/home/jack/spack/opt/spack/linux-ubuntu22.04-skylake/gcc-11.4.0/libxsmm-1.17-ikt4m66huadxh7ay3vfr34phsgdvmsl5/lib/libxsmm.so"

try:
    # Load the library
    libxsmm = ctypes.CDLL(libxsmm_path)

    # Check for a specific symbol
    symbol = "libxsmm_original_dgemv_function"
    if hasattr(libxsmm, symbol):
        print(f"Symbol '{symbol}' found in libxsmm.so!")
    else:
        print(f"Symbol '{symbol}' not found in libxsmm.so.")
except OSError as e:
    print(f"Failed to load libxsmm.so: {e}")
