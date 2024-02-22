"""
This script demonstrates the use of a simple neural network model running on either CPU or GPU, with options for single or parallel GPU execution. It allows for command-line specification of the execution mode (single GPU or parallel GPUs), the device type (CPU or GPU), and a specified duration for which to block the GPU for computation. The script uses PyTorch for model definition and execution, showcasing basic neural network operations, device management, and command-line interaction for runtime configuration.

Usage:
    python main.py [-m MODE] [-d DEVICE_TYPE] [-t BLOCK_TIME]

Options:
    -m, --mode          Mode to run the model: 'single' for a single GPU or 'parallel' for all GPUs.
    -d, --device        Device type to use: 'cpu' for CPU or 'gpu' for GPU. Default is 'gpu'.
    -t, --time          Time in seconds to block the GPU. Default is 0.
    -c, --cuda_device   Specifies the CUDA device to use by index when mode is 'single'. Default is '0'.

The script includes a simple model `SimpleModel` which consists of a single fully connected layer. The model is executed with randomly generated data to simulate workload on the specified device. Command-line arguments control the execution mode, allowing users to explore different configurations and understand the basics of GPU computation with PyTorch.
"""

import torch
import torch.nn as nn
import time
import argparse
from typing import Any, Tuple


def get_args_parser() -> argparse.Namespace:
    """
    Parses the command line arguments.

    Returns:
        argparse.Namespace: The namespace containing the arguments.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-m",
        "--mode",
        dest="mode",
        type=str,
        default="single",
        help="Mode to run the model: 'single' for a single GPU or 'parallel' for all GPUs.",
    )
    parser.add_argument(
        "-d",
        "--device",
        dest="device_type",
        type=str,
        default="gpu",
        help="Device type to use: 'cpu' for CPU or 'gpu' for GPU.",
    )
    parser.add_argument(
        "-t",
        "--time",
        dest="block_time",
        type=int,
        default=0,
        help="Time in seconds to block the GPU.",
    )
    parser.add_argument(
        "-c",
        "--cuda-device",
        dest="cuda_device",
        type=str,
        default="0",
        help="Specifies the CUDA device to use by index when mode is 'single'. Default is '0'.",
    )
    return parser.parse_args()


class SimpleModel(nn.Module):
    """
    A simple neural network model consisting of a single fully connected layer.
    """

    def __init__(self):
        super(SimpleModel, self).__init__()
        self.fc = nn.Linear(1024, 1024)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """
        Defines the computation performed at every call.

        Args:
            x (torch.Tensor): The input tensor.

        Returns:
            torch.Tensor: The output tensor.
        """
        return self.fc(x)


def run(options: argparse.Namespace, device: torch.device) -> None:
    """
    Runs the model with the specified options on the given device.

    Args:
        options (argparse.Namespace): The command line arguments.
        device (torch.device): The device to run the model on.
    """
    model = SimpleModel()
    data = torch.randn(64, 1024)  # Example input data
    data = data.to(device)
    model.to(device)

    start_time = time.time()
    print_interval = 2  # For example, print every 2 seconds
    next_print_time = start_time + print_interval
    print(f"I will now be blocking the GPU for {options.block_time:.1f}s")

    while time.time() - start_time < options.block_time:
        _ = model(data)  # Perform operations on GPU
        current_time = time.time()
        if current_time >= next_print_time:
            print(
                f"Blocking GPU, elapsed time: {current_time - start_time:.2f}/{options.block_time:.1f}s"
            )
            next_print_time += print_interval

    print(f"Completed blocking GPU for {options.block_time} seconds.")
    if options.mode == "single" or options.device_type.lower() == "cpu":
        output = model(data)
    elif (
        options.mode == "parallel"
        and device.type == "cuda"
        and torch.cuda.device_count() > 1
    ):
        print(f"Running on {torch.cuda.device_count()} GPUs in parallel : )")
        model = nn.DataParallel(model)
        output = model(data)
    else:
        raise ValueError("Invalid mode or device type selected.")

    print(f"Output size: {output.size()}")


if __name__ == "__main__":
    options = get_args_parser()

    if options.device_type.lower() == "cpu" or not torch.cuda.is_available():
        device = torch.device("cpu")
    elif options.device_type.lower() == "gpu":
        if options.mode == "single":
            # Use the specified CUDA device index
            cuda_device_index = options.cuda_device
            device = torch.device(f"cuda:{cuda_device_index}")
        elif torch.cuda.is_available():
            # Default behavior for 'gpu' device type without specifying 'single' mode
            device = torch.device("cuda:0")
        else:
            raise ValueError("Invalid device type selected. Choose 'cpu' or 'gpu'.")
    else:
        raise ValueError("Invalid device type selected. Choose 'cpu' or 'gpu'.")

    print(f"Using {device}.")
    run(options, device)
