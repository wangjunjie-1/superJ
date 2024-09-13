from typing import Union
from pathlib import Path
import onnxruntime
import onnx
import click
class ONNXKit(object):
    def __init__(self, onnx_path: Union[Path,str],device:str = 'cpu') -> None:

        self.onnx_path = Path(onnx_path)
        self.set_device(device=device)
        self.onnx_model = onnx.load(str(onnx_path))
        options = onnxruntime.SessionOptions()
        self.session = onnxruntime.InferenceSession(str(onnx_path), options, providers=[f'{self.device}ExecutionProvider'])

    def show(self,info_level = 0):
        if info_level == 0:
            input_metadata = self.session.get_inputs()
            output_metadata = self.session.get_outputs()
            for input in input_metadata:
                input_name = input.name
                input_type = input.type
                input_shape = input.shape
                print(f"Input Name: {input_name}, Type: {input_type}, Shape: {input_shape}")
            for output in output_metadata:
                output_name = output.name
                output_type = output.type
                output_shape = output.shape
                print(f"Output Name: {output_name}, Type: {output_type}, Shape: {output_shape}")
            return 
        else:
            # 检查模型的元数据
            print("Model Metadata:")
            print(model.metadata_props)
            # 打印模型的图结构
            print("\nGraph Structure:")
            graph = model.graph
            print(f"Graph name: {graph.name}")
            input_metadata = graph.input
            output_metadata = graph.output
            for input in input_metadata:
                input_name = input.name
                input_type = input.type.tensor_type.elem_type
                input_shape = [_.dim_value for _ in input.type.tensor_type.shape.dim]
                print(f"Input Name: {input_name}, Type: {input_type}, Shape: {input_shape}")
            for output in output_metadata:
                output_name = output.name
                output_type = output.type.tensor_type.elem_type
                output_shape = [_.dim_value for _ in output.type.tensor_type.shape.dim]
                print(f"Output Name: {output_name}, Type: {output_type}, Shape: {output_shape}")
            if info_level == 1:
                return 
            else:
                # 遍历并打印所有的节点
                print("\nNodes:")
                for node in graph.node:
                    print(f"  - Node: {node.name} (op_type={node.op_type})")
                    print(f"    Inputs: {node.input}")
                    print(f"    Outputs: {node.output}")

                # # 如果需要，还可以打印初始化张量和值信息
                print("\nInitializers:")
                for initializer in graph.initializer:
                    data_type = initializer.data_type
                    print(f"  - Name: {initializer.name}, Shape: {initializer.dims}",end="")
                    # conv_data = np.frombuffer(initializer.raw_data, dtype=np.float32).reshape(tuple(initializer.dims))
                    # print(f"  - Conv data:{conv_data}")

                print("\nValue Infos:")
                for value_info in graph.value_info:
                    print(f"  - Name: {value_info.name}, Type: {value_info.type.tensor_type.elem_type}")

    def set_device(self,device: str) -> None:
        if device not in ['cpu', 'gpu']:
            raise ValueError("device must be either 'cpu' or 'gpu'")
        if device=='cpu':
            self.device = "CPU"
        else:
            self.device = "CUDA"
        print(f"Device set to {device}")
        return 
    
    def set_input(self,input_data):
        self.input_data = input_data
        return 
    
    def check(self):
        print(f'The model is:\n{self.onnx_path}')
        try:
            onnx.checker.check_model(self.onnx_model)
        except onnx.checker.ValidationError as e:
            print('The model is invalid: %s' % e)
        else:
            print('The model is valid!')
    
    def inference(self,input_data):
        self.input_data = input_data
        return

# 定义命令组
@click.group()
def cli():
    # click.echo("hello superJ")
    pass

# 在命令组中注册命令
@cli.command()
@click.argument('onnx_path')
def onnx_show(onnx_path:Path):
    onnxkit = ONNXKit(onnx_path = onnx_path)
    onnxkit.show()

# 在命令组中注册命令
@cli.command()
@click.argument('onnx_path')
def onnx_check(onnx_path:Path):
    onnxkit = ONNXKit(onnx_path = onnx_path)
    onnxkit.check()

   