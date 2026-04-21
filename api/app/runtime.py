def runtime_status() -> dict[str, str | bool]:
    data: dict[str, str | bool] = {}

    try:
        import tensorflow as tf  # type: ignore

        data["tensorflow"] = True
        data["tensorflow_version"] = tf.__version__
    except Exception:
        data["tensorflow"] = False

    try:
        import torch  # type: ignore

        data["pytorch"] = True
        data["pytorch_version"] = torch.__version__
    except Exception:
        data["pytorch"] = False

    return data
