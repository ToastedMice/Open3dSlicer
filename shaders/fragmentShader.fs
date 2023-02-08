"""
#version 330
out vec4 frag_color;
in vec4 v_color;

in vec3 v_normal;
void main() {
    vec4 normalizedv_normal = normalize(vec4(v_normal, 0.0));
    vec4 light_direction = normalize(vec4(0.0,-1.0,0.0,0.0));
    vec4 light_color = vec4(0.6877,0.96,0.6048,0.0); //http://www.rgbtool.com/
    float diffuse = dot(normalizedv_normal,light_direction);
    frag_color = v_color * diffuse * light_color;
}
"""