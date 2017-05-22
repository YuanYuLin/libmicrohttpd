import ops
import iopc

def MAIN_ENV(args):
    pkg_path = args["pkg_path"]
    output_dir = args["output_path"]
    return False

def MAIN_EXTRACT(args):
    pkg_dir = args["pkg_path"]
    output_dir = args["output_path"]

    src_lib = iopc.getBaseRootFile("/usr/lib/arm-linux-gnueabihf/libmicrohttpd.so.10.27.0")
    ops.copyto(src_lib, output_dir)

    ops.ln(output_dir, "libmicrohttpd.so.10.27.0", "libmicrohttpd.so.10")
    ops.ln(output_dir, "libmicrohttpd.so.10.27.0", "libmicrohttpd.so")
    return False

def MAIN_CONFIGURE(args):
    output_dir = args["output_path"]
    return False

def MAIN_BUILD(args):
    output_dir = args["output_path"]
    return False

def MAIN_INSTALL(args):
    output_dir = args["output_path"]

    dst_includes = ops.path_join("include",args["pkg_name"])

    src_includes = iopc.getBaseRootFile("/usr/include/microhttpd.h")
    iopc.installBin(args["pkg_name"], src_includes, dst_includes)

    src_lib = ops.path_join(output_dir, ".")
    iopc.installBin(args["pkg_name"], src_lib, "usr/lib") 
    return False

def MAIN_CLEAN_BUILD(args):
    output_dir = args["output_path"]
    return False

def MAIN(args):
    output_dir = args["output_path"]

