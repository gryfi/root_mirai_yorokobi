print("Add Color Key Filter")
obs = obslua

-- Description displayed in the Scripts dialog window
function script_description()
  print("in script_description")
  return [[Add Color Key Filter
           Add Color Key Black when
            Black Square Video Detected 
           Just Simple Like that.]]
end

function script_tick(seconds)
  local current_scene_as_source = obs.obs_frontend_get_current_scene()
  if current_scene_as_source then
    local current_scene = obs.obs_scene_from_source(current_scene_as_source)
    local scene_item = obs.obs_scene_find_source_recursive(current_scene, "Media Source Test Script")
    if scene_item then
		local allSources =	obs.obs_enum_sources()
		if allSources ~= nil then
			for _, source in ipairs(allSources) do
				local filter_id = obs.obs_source_get_filter_by_name(source,"Color Key Black")
				if(filter_id ~= nil and obs.obs_source_get_type(filter_id) == obs.OBS_SOURCE_TYPE_FILTER) then
					obs.obs_source_set_enabled(filter_id, false)
				end
			end
		end
   end
    obs.obs_source_release(current_scene_as_source)
  end
  
end
