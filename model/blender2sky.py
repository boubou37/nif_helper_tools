from pyffi.formats.nif import *
import model.nifcleaner as nc


class BlenderToSkyConverter(nc.NifCleaner):
    def __init__(self):
        super().__init__()

    def __init_shader_flags_1(bsl):
        if type(bsl) != NifFormat.BSLightingShaderProperty:
            return
        bsl.shader_flags_1.slsf_1_specular = 1
        bsl.shader_flags_1.slsf_1_skinned = 1
        bsl.shader_flags_1.slsf_1_temp_refraction = 0
        bsl.shader_flags_1.slsf_1_vertex_alpha = 0
        bsl.shader_flags_1.slsf_1_greyscale_to_palette_color = 0
        bsl.shader_flags_1.slsf_1_greyscale_to_palette_alpha = 0
        bsl.shader_flags_1.slsf_1_use_falloff = 0
        bsl.shader_flags_1.slsf_1_environment_mapping = 0
        bsl.shader_flags_1.slsf_1_recieve_shadows = 1
        bsl.shader_flags_1.slsf_1_cast_shadows = 1
        bsl.shader_flags_1.slsf_1_facegen_detail_map = 0
        bsl.shader_flags_1.slsf_1_parallax = 0
        bsl.shader_flags_1.slsf_1_model_space_normals = 0
        bsl.shader_flags_1.slsf_1_non_projective_shadows = 0
        bsl.shader_flags_1.slsf_1_landscape = 0
        bsl.shader_flags_1.slsf_1_refraction = 0
        bsl.shader_flags_1.slsf_1_fire_refraction = 0
        bsl.shader_flags_1.slsf_1_eye_environment_mapping = 0
        bsl.shader_flags_1.slsf_1_hair_soft_lighting = 0
        bsl.shader_flags_1.slsf_1_screendoor_alpha_fade = 0
        bsl.shader_flags_1.slsf_1_localmap_hide_secret = 0
        bsl.shader_flags_1.slsf_1_face_gen_rgb_tint = 0
        bsl.shader_flags_1.slsf_1_own_emit = 1
        bsl.shader_flags_1.slsf_1_projected_uv = 0
        bsl.shader_flags_1.slsf_1_multiple_textures = 0
        bsl.shader_flags_1.slsf_1_remappable_textures = 1
        bsl.shader_flags_1.slsf_1_decal = 0
        bsl.shader_flags_1.slsf_1_dynamic_decal = 0
        bsl.shader_flags_1.slsf_1_parallax_occlusion = 0
        bsl.shader_flags_1.slsf_1_external_emittance = 0
        bsl.shader_flags_1.slsf_1_soft_effect = 0
        bsl.shader_flags_1.slsf_1_z_buffer_test = 1

    def __init_shader_flags_2(bsl):
        if type(bsl) != NifFormat.BSLightingShaderProperty:
            return
        bsl.shader_flags_2.slsf_2_z_buffer_write = 1
        bsl.shader_flags_2.slsf_2_lod_landscape = 0
        bsl.shader_flags_2.slsf_2_lod_objects = 0
        bsl.shader_flags_2.slsf_2_no_fade = 0
        bsl.shader_flags_2.slsf_2_double_sided = 1
        bsl.shader_flags_2.slsf_2_vertex_colors = 1
        bsl.shader_flags_2.slsf_2_glow_map = 0
        bsl.shader_flags_2.slsf_2_assume_shadowmask = 0
        bsl.shader_flags_2.slsf_2_packed_tangent = 0
        bsl.shader_flags_2.slsf_2_multi_index_snow = 0
        bsl.shader_flags_2.slsf_2_vertex_lighting = 0
        bsl.shader_flags_2.slsf_2_uniform_scale = 0
        bsl.shader_flags_2.slsf_2_fit_slope = 0
        bsl.shader_flags_2.slsf_2_billboard = 0
        bsl.shader_flags_2.slsf_2_no_lod_land_blend = 0
        bsl.shader_flags_2.slsf_2_env_map_light_fade = 1
        bsl.shader_flags_2.slsf_2_wireframe = 0
        bsl.shader_flags_2.slsf_2_weapon_blood = 0
        bsl.shader_flags_2.slsf_2_hide_on_local_map = 0
        bsl.shader_flags_2.slsf_2_premult_alpha = 0
        bsl.shader_flags_2.slsf_2_cloud_lod = 0
        bsl.shader_flags_2.slsf_2_anisotropic_lighting = 0
        bsl.shader_flags_2.slsf_2_no_transparency_multisampling = 0
        bsl.shader_flags_2.slsf_2_unused_01 = 0
        bsl.shader_flags_2.slsf_2_multi_layer_parallax = 0
        bsl.shader_flags_2.slsf_2_soft_lighting = 0
        bsl.shader_flags_2.slsf_2_rim_lighting = 0
        bsl.shader_flags_2.slsf_2_back_lighting = 0
        bsl.shader_flags_2.slsf_2_unused_02 = 0
        bsl.shader_flags_2.slsf_2_tree_anim = 0
        bsl.shader_flags_2.slsf_2_effect_lighting = 0
        bsl.shader_flags_2.slsf_2_hd_lod_objects = 0
        return