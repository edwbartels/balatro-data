-- Utility functions for proper JSON conversion
local function serialize_date(o)
    if type(o) == 'table' then
        local s = '{'
        for k, v in pairs(o) do
            if type(k) ~= 'number' then
                k = '"' .. k .. '"'
            end
            s = s .. '[' .. k .. ']:' .. serialize_date(v) .. ','
        end
        return s .. '}'
    else
        return tostring(o)
    end
end

-- Function to properly format numbers for JSON
local function format_number(n)
    if type(n) == "number" then
        if n == math.floor(n) then
            return string.format("%d", n)
        else
            return string.format("%.10g", n)
        end
    end
    return tostring(n)
end

-- Main JSON conversion function
local function to_json(obj, level)
    level = level or 0
    local indent = string.rep("  ", level)

    if type(obj) == "table" then
        local json = "{"
        local first = true

        -- Sort keys to ensure consistent output
        local keys = {}
        for k in pairs(obj) do
            table.insert(keys, k)
        end
        table.sort(keys, function(a, b)
            if type(a) == type(b) then
                return tostring(a) < tostring(b)
            else
                return type(a) < type(b)
            end
        end)

        -- Convert each key-value pair
        for _, k in ipairs(keys) do
            local v = obj[k]
            if not first then
                json = json .. ","
            end
            first = false
            json = json .. "\n" .. indent .. "  "

            -- Handle key
            -- if type(k) == "string" then
            --     json = json .. '"' .. k .. '"'
            -- else
            --     json = json .. "[" .. tostring(k) .. "]"
            -- end
            json = json .. '"' .. k .. '"'

            json = json .. ": " .. to_json(v, level + 1)
        end

        if not first then
            json = json .. "\n" .. indent
        end
        return json .. "}"
    elseif type(obj) == "string" then
        return '"' .. obj:gsub('"', '\\"'):gsub("\n", "\\n") .. '"'
    elseif type(obj) == "number" then
        return format_number(obj)
    elseif type(obj) == "boolean" then
        return tostring(obj)
    elseif obj == nil then
        return "null"
    else
        return '"' .. tostring(obj) .. '"'
    end
end

-- Main script
local function main()
    if #arg < 2 then
        print("Usage: lua save_to_json.lua <input_file> <output_file>")
        os.exit(1)
    end

    local input_file = arg[1]
    local output_file = arg[2]

    -- Read input file
    local f = io.open(input_file, "r")
    if not f then
        print("Error: Could not open input file " .. input_file)
        os.exit(1)
    end
    local content = f:read("*all")
    f:close()

    -- Execute content to get table
    local success, result = pcall(load(content))
    if not success then
        print("Error: Could not parse save file: " .. tostring(result))
        os.exit(1)
    end

    -- Convert to JSON
    local json = to_json(result)

    -- Write output
    f = io.open(output_file, "w")
    if not f then
        print("Error: Could not open output file " .. output_file)
        os.exit(1)
    end
    f:write(json)
    f:close()

    print("Successfully converted " .. input_file .. " to " .. output_file)
end

main()
