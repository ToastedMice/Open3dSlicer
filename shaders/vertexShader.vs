"""
#version 330
uniform mat4 projection;
uniform mat4 view;
uniform mat4 model;
in vec3 position;
in vec4 color;
in vec3 normal;

out vec3 v_normal;
out vec4 v_color;
void main() {
    gl_Position = projection * view * model * vec4(position, 1.0);
    v_color = color;
    v_normal = normal;
}
"""