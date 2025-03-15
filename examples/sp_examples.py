
import sys
import sply

class sp_example:
    def __init__(self,
            mode="",
            show="",
            backend="",
            model_id="",
            seed="",
            temp="",
            num_ctx="",
            ):

        self.res = 0

        sp_args = {}
        sp_args["show"] = show
        sp_args["backend"] = backend
        sp_args["model_id"] = model_id
        sp_args["seed"] = seed
        sp_args["temp"] = temp
        sp_args["num_ctx"] = num_ctx

        for arg in sys.argv[1:]:
            if arg.find("--help") == 0:
                print(f"usage: {sys.argv[0]}"\
                    f" [--help]"\
                    f" [mode=\"plain\"|\"think\" (\"{mode}\")]"\
                    f" [show=\"True|False\" ({sp_args["show"]})]"\
                    f" [backend=\"ollama\"|\"llcpp\" (\"{sp_args["backend"]}\")]"\
                    f" [model_id=\"model_id\" (\"{sp_args["model_id"]}\")]"\
                    f" [seed=\"seed\" ({sp_args["seed"]})]"\
                    f" [temp=\"temp\" ({sp_args["temp"]})]"\
                    f" [num_ctx=\"num_ctx\" ({sp_args["num_ctx"]})]"\
                    "")
                self.res = -1
                return
            elif arg.find("mode=") == 0:
                sp_args["mode"] = arg[5:]
            elif arg.find("show=") == 0:
                self.show = True if arg[5:] == "True" else False
            elif arg.find("backend=") == 0:
                sp_args["backend"] = arg[8:]
            elif arg.find("model_id=") == 0:
                sp_args["model_id"] = arg[9:]
            elif arg.find("seed=") == 0:
                sp_args["seed"] = int(arg[5:])
            elif arg.find("temp=") == 0:
                sp_args["temp"] = float(arg[5:])
            elif arg.find("num_ctx=") == 0:
                sp_args["num_ctx"] = int(arg[8:])

        if mode == "plain":
            sp_args["prompt"] = sply.sp.create_prompt_default()
        elif mode == "think":
            sp_args["prompt"] = sply.sp.create_prompt_think()

        self.sp = sply.sp(**sp_args)

        if mode == "plain":
            self.runcode = self.sp.runcode
        elif mode == "think":
            self.runcode = self.sp.runcode_think

        self.mode = mode

