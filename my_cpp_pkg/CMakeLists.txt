cmake_minimum_required(VERSION 3.8)
project(my_cpp_pkg)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)

add_executable(cpp_node src/my_first_node.cpp)
# link dependencies
ament_target_dependencies(cpp_node rclcpp)

# install the .exe
install(TARGETS
  # create an .exe called "cpp_node"
  cpp_node
  DESTINATION lib/${PROJECT_NAME}
)

ament_package()
