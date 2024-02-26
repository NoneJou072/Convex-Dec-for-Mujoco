# Convex Decomposition for Mujoco based V-HACD.（Convex-Dec for Mujoco）

为了解决 mujoco 仿真中，自定义的网格物体会在运行碰撞检测时自动凸优化的问题。我们可以使用 V-HACD 对网格进行分解，在 mujoco 中使用分解后的多个网格来组成碰撞体。

## Preparations
* Blender (用于将 `.stl` 转成 `.obj` 文件)
* Linux / Windows
* CMake (用于编译 V-HACD)

## Quick Start
1. 克隆本仓库，并初始化子模块（V-HACD）
```bash
git clone https://github.com/NoneJou072/Convex-Dec-for-Mujoco.git --recurse-submodules
cd Convex-Dec-for-Mujoco
```
2. 编译 V-HACD Library

On Windows, go to the `./app` directory and run `cmake -DCMAKE_GENERATOR_PLATFORM=x64 CMakeLists.txt` and then load the solution file

On Linux, use this:
```bash
cd app
cmake -S . -B build -DCMAKE_BUILD_TYPE=Release
cmake --build build
```
3. 分解网格物体

On Linux,
```bash
cd build
./TestVHACD <your .obj file>
```
会自动将 obj 物体分成 64 个子物体，并在`build`目录下将这些物体保存到同一个 obj 文件中。

## Others
可以使用 blender 将 `.stl` 转成 `.obj` 文件
